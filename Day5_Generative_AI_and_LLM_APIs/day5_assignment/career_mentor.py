"""
🎯 Day 5 Student Assignment Solution: AI Career Mentor
A feature-complete, production-grade CLI Chatbot that helps students and professionals
discover and navigate tech career pathways. 

Core Features:
- System prompt design with localized salary ranges
- Multi-turn conversation history
- Dual-provider system (Groq LLaMA 3.3 and Google Gemini 1.5 Flash)
- Automatic failover / fallback logic if the primary provider crashes
- Retry logic with exponential backoff for network resilience
- Command router (/assess, /switch, /mode, /lang, /stats, /save, /clear, /quit)

Bonus Features:
1. Quick Assessment Mode (/assess): 5 structured questions generating a 90-day learning roadmap.
2. Markdown Session Export: Beautiful outputs with metadata.
3. Cost Comparison Engine: Live API pricing grid shown after each query.
4. Multi-Language Indian Support: Toggle between English, Hindi, and Hinglish.
5. Personality Styles Switcher: Switch between Friendly, Professional, and Strict.
"""

import os
import sys
import time
import json
from datetime import datetime
from dotenv import load_dotenv

# Try importing dependencies; print a friendly warning if they are missing
try:
    from groq import Groq
    import google.generativeai as genai
    import tiktoken
except ImportError as e:
    print(f"\033[91m❌ Missing dependency: {e.name}. Please run 'pip install -r requirements.txt' first!\033[0m")
    sys.exit(1)

# Load environment variables
load_dotenv()

# ANSI Color Codes for Premium CLI Styling
class Colors:
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    MAGENTA = "\033[95m"

# -----------------------------------------------------------------------------
# 1. CORE PERSONA & PROMPT CONFIGURATIONS
# -----------------------------------------------------------------------------

BASE_PERSONA = """You are CareerAI, a senior tech career mentor with 15+ years of experience 
across Google, Microsoft, Amazon, and multiple successful startups in India and Silicon Valley.
You have personally guided over 500 professionals into highly successful tech roles.

YOUR SPECIALIZATION & INDUSTRY BENCHMARKS:
- AI/ML Engineering: Specialized in NLP, CV, Agentic Workflows.
  * Salary: India ₹8L - ₹50L+ | Global $80K - $300K+
- Full-Stack Development: React, Node, FastAPI, system design.
  * Salary: India ₹5L - ₹40L+ | Global $70K - $250K+
- Data Science & Analytics: Pandas, SQL, ML modelling, business intelligence.
  * Salary: India ₹6L - ₹45L+ | Global $75K - $250K+
- DevOps & Cloud Engineering: Docker, Kubernetes, CI/CD, AWS/GCP, infrastructure as code.
  * Salary: India ₹6L - ₹35L+ | Global $80K - $260K+
- Product Management & Tech Startup Founder track.

YOUR MENTORING WORKFLOW:
1. Discovery: Ask about the user's background, existing skills, timelines, and primary goals.
2. Direct Guidance: Give extremely specific, step-by-step 90-day roadmaps. Recommend actual packages, certifications, and portfolio project ideas.
3. Realistic Support: Be encouraging, but highly realistic. Stress that consistency and a strong GitHub profile matter more than academic pedigree.

CRITICAL LAWS:
- NEVER guarantee placement or specific salaries. Use terms like "industry averages" and "target ranges".
- Always ask at least 2 highly relevant clarifying questions before giving career transition advice.
- Cite GitHub portfolio creation and building in public as crucial pillars of developer success.
- If asked about non-career topics (e.g., general cooking, politics), politely redirect them.
"""

PERSONALITY_MODES = {
    "friendly": "Write in a highly supportive, warm, casual, and encouraging tone. Use conversational warmth, and insert friendly emojis (e.g., 😊, 🚀, 💻, 🎯) where appropriate. Treat the user like a close peer who you want to see succeed.",
    "professional": "Write in a formal, authoritative, data-driven, and highly structured tone. Use professional bullet points, clear headings, and logical transitions. Avoid emojis entirely. Focus on facts, objective industry benchmarks, and professional standards.",
    "strict": "Write in a no-nonsense, direct, demanding, and highly challenging tone. Act like a tough but caring coach. Challenge the user's assumptions and dedication. Ask difficult, critical questions about their timeline, commitment level, and effort. No emojis, no sugarcoating."
}

LANGUAGE_MODES = {
    "english": "Always respond in standard English.",
    "hindi": "Always respond in Hindi (हिंदी) using the Devanagari script. Make sure the technical terminology (e.g., 'API', 'Docker', 'Machine Learning') remains in English characters or clear phonetics, but all conversational explanations, instructions, and mentoring details are in perfect Hindi.",
    "hinglish": "Always respond in Hinglish (Hindi written in the Roman/Latin alphabet). Use natural, conversational Hinglish as used by software developers in India (e.g., 'Aapko basic Python se start karna chahiye, phir hum advanced libraries pe move karenge. Deep Learning ke liye portfolio build karna bahut important hai.'). Keep tech/coding terms in standard English."
}

# -----------------------------------------------------------------------------
# 2. TOKEN CONTROLLER & COST ESTIMATION ENGINE
# -----------------------------------------------------------------------------

class CostCalculator:
    """Estimates the execution cost across various API providers."""
    # Pricing per 1,000,000 tokens
    PRICING = {
        "groq": {"input": 0.59, "output": 0.79, "name": "Groq LLaMA 3.3 (70B)"},
        "gemini": {"input": 0.075, "output": 0.30, "name": "Google Gemini Flash"},
        "openai": {"input": 0.15, "output": 0.60, "name": "OpenAI GPT-4o mini"}
    }

    def __init__(self):
        # Initialize standard tiktoken encoding (using GPT-4 encoding as a close approximation)
        try:
            self.encoder = tiktoken.encoding_for_model("gpt-4o")
        except Exception:
            self.encoder = None

    def count_tokens(self, text: str) -> int:
        """Count tokens in a text block."""
        if not text:
            return 0
        if self.encoder:
            return len(self.encoder.encode(text))
        # Simple word fallback if tiktoken isn't loaded correctly
        return len(text.split()) + int(len(text) * 0.25)

    def print_cost_grid(self, input_tokens: int, output_tokens: int):
        """Prints a visual cost grid comparing providers for this exchange."""
        print(f"\n{Colors.DIM}💰 API TRANSACTION COST COMPARISON (Actual size: {input_tokens} In, {output_tokens} Out tokens){Colors.RESET}")
        print(f"{Colors.DIM}┌─────────────────────────┬──────────────┬──────────────┬──────────────┐{Colors.RESET}")
        print(f"{Colors.DIM}│ Provider                │ Input Cost   │ Output Cost  │ Total Cost   │{Colors.RESET}")
        print(f"{Colors.DIM}├─────────────────────────┼──────────────┼──────────────┼──────────────┤{Colors.RESET}")
        
        for key, rates in self.PRICING.items():
            in_cost = (input_tokens / 1_000_000) * rates["input"]
            out_cost = (output_tokens / 1_000_000) * rates["output"]
            tot_cost = in_cost + out_cost
            
            # Formatting highlight for active provider
            color = Colors.RESET
            print(f"{Colors.DIM}│{Colors.RESET} {color}{rates['name']:<23}{Colors.RESET} {Colors.DIM}│{Colors.RESET} ${in_cost:.6f}     {Colors.DIM}│{Colors.RESET} ${out_cost:.6f}     {Colors.DIM}│{Colors.RESET} ${tot_cost:.6f}     {Colors.DIM}│{Colors.RESET}")
            
        print(f"{Colors.DIM}└─────────────────────────┴──────────────┴──────────────┴──────────────┘{Colors.RESET}")

# -----------------------------------------------------------------------------
# 3. LLM API CONNECTION MANAGER WITH AUTOMATIC FAILOVER & EXPONENTIAL BACKOFF
# -----------------------------------------------------------------------------

class LLMManager:
    """Manages connections to Groq and Gemini APIs with graceful retry logic and fallbacks."""
    def __init__(self):
        self.groq_key = os.getenv("GROQ_API_KEY")
        self.gemini_key = os.getenv("GEMINI_API_KEY")
        
        self.groq_client = None
        self.gemini_client_configured = False
        
        # Initialize Groq client if key exists
        if self.groq_key and not self.groq_key.endswith("_key_here"):
            try:
                self.groq_client = Groq(api_key=self.groq_key)
            except Exception as e:
                print(f"{Colors.YELLOW}⚠️ Failed to initialize Groq client: {e}{Colors.RESET}")
        
        # Configure Gemini client if key exists
        if self.gemini_key and not self.gemini_key.endswith("_key_here"):
            try:
                genai.configure(api_key=self.gemini_key)
                self.gemini_client_configured = True
            except Exception as e:
                print(f"{Colors.YELLOW}⚠️ Failed to configure Gemini: {e}{Colors.RESET}")
                
        # Fallback provider logic
        if not self.groq_client and not self.gemini_client_configured:
            print(f"{Colors.RED}❌ Error: No valid API keys found in your .env file!{Colors.RESET}")
            print(f"Please check your keys or copy .env.example to .env and input your GROQ_API_KEY or GEMINI_API_KEY.")
            sys.exit(1)

    def execute_chat_with_retry(self, provider: str, system_prompt: str, history: list, temp: float = 0.7, max_retries: int = 3) -> tuple:
        """Executes API call. Retries on failure, and automatically redirects if primary provider dies."""
        # 1. Groq Completion Call
        if provider == "groq":
            if not self.groq_client:
                print(f"{Colors.YELLOW}⚠️ Groq is selected but client is not initialized. Falling back to Gemini!{Colors.RESET}")
                return self.execute_chat_with_retry("gemini", system_prompt, history, temp, max_retries)
            
            # Format messages payload
            messages = [{"role": "system", "content": system_prompt}]
            messages.extend(history)
            
            for attempt in range(max_retries):
                try:
                    response = self.groq_client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=messages,
                        temperature=temp,
                        max_tokens=1524
                    )
                    ai_content = response.choices[0].message.content
                    in_t = response.usage.prompt_tokens
                    out_t = response.usage.completion_tokens
                    return ai_content, in_t, out_t, "groq"
                except Exception as e:
                    wait_time = 2 ** attempt
                    if attempt < max_retries - 1:
                        print(f"{Colors.YELLOW}⚠️ API Connection failed: {e}. Retrying {attempt + 1}/{max_retries} in {wait_time}s...{Colors.RESET}")
                        time.sleep(wait_time)
                    else:
                        print(f"{Colors.RED}💥 Primary Provider Groq failed after {max_retries} retries!{Colors.RESET}")
                        if self.gemini_client_configured:
                            print(f"{Colors.GREEN}🔄 Automatically failing over to Google Gemini...{Colors.RESET}")
                            return self.execute_chat_with_retry("gemini", system_prompt, history, temp, max_retries)
                        raise e

        # 2. Gemini Completion Call
        elif provider == "gemini":
            if not self.gemini_client_configured:
                print(f"{Colors.YELLOW}⚠️ Gemini is selected but config is missing. Falling back to Groq!{Colors.RESET}")
                return self.execute_chat_with_retry("groq", system_prompt, history, temp, max_retries)
            
            # Gemini models set System Instructions during construction
            for attempt in range(max_retries):
                try:
                    model = genai.GenerativeModel(
                        "gemini-1.5-flash",
                        system_instruction=system_prompt,
                        generation_config={"temperature": temp, "max_output_tokens": 1524}
                    )
                    
                    # Convert OpenAI standard history history list to Gemini's history structure
                    gemini_history = []
                    for item in history:
                        role = "user" if item["role"] == "user" else "model"
                        gemini_history.append({"role": role, "parts": [item["content"]]})
                    
                    # Run content generation
                    response = model.generate_content(gemini_history)
                    ai_content = response.text
                    
                    # Read usage metrics
                    in_t = response.usage_metadata.prompt_token_count
                    out_t = response.usage_metadata.candidates_token_count
                    return ai_content, in_t, out_t, "gemini"
                except Exception as e:
                    wait_time = 2 ** attempt
                    if attempt < max_retries - 1:
                        print(f"{Colors.YELLOW}⚠️ API Connection failed: {e}. Retrying {attempt + 1}/{max_retries} in {wait_time}s...{Colors.RESET}")
                        time.sleep(wait_time)
                    else:
                        print(f"{Colors.RED}💥 Primary Provider Gemini failed after {max_retries} retries!{Colors.RESET}")
                        if self.groq_client:
                            print(f"{Colors.GREEN}🔄 Automatically failing over to Meta LLaMA on Groq...{Colors.RESET}")
                            return self.execute_chat_with_retry("groq", system_prompt, history, temp, max_retries)
                        raise e

        return "Error: Invalid Provider", 0, 0, provider

# -----------------------------------------------------------------------------
# 4. CHATBOT APPLICATION ENGINE & CLI LAYER
# -----------------------------------------------------------------------------

class CareerMentorApp:
    """Orchestrates CLI loops, commands, parameters, and saved session exports."""
    def __init__(self):
        self.llm = LLMManager()
        self.costs = CostCalculator()
        
        # Application Settings (Defaults)
        self.provider = "groq" if self.llm.groq_client else "gemini"
        self.personality = "friendly"
        self.language = "english"
        
        # State Arrays
        self.conversation_history = []  # Contains dicts: {"role": "user"|"assistant", "content": "..."}
        
        # Session Analytics State
        self.session_start = datetime.now()
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.messages_count = 0
        self.switches_count = 0
        
        # Ensure exports directory exists
        os.makedirs("exports", exist_ok=True)

    def print_welcome_banner(self):
        """Prints a beautiful visual introduction for the student."""
        print(f"\n{Colors.CYAN}{Colors.BOLD}╔════════════════════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.CYAN}{Colors.BOLD}║                   🎯 CAREERAI MENTOR BOT                   ║{Colors.RESET}")
        print(f"{Colors.CYAN}{Colors.BOLD}║         Senior Tech Career Mentor & Roadmap Builder        ║{Colors.RESET}")
        print(f"{Colors.CYAN}{Colors.BOLD}║     Powered by Groq LLaMA 3.3 & Google Gemini 1.5 Flash    ║{Colors.RESET}")
        print(f"{Colors.CYAN}{Colors.BOLD}╚════════════════════════════════════════════════════════════╝{Colors.RESET}")
        print(f"\n{Colors.GREEN}👋 Welcome to CareerAI! Ready to map your path into the tech industry.{Colors.RESET}")
        print(f"{Colors.DIM}Type your questions freely. Enter control commands at any time:{Colors.RESET}")
        self.print_help_menu()

    def print_help_menu(self):
        """Prints the table of active CLI shortcuts."""
        print(f"\n{Colors.BOLD}📋 SYSTEM SHORTCUT COMMANDS:{Colors.RESET}")
        print(f"  {Colors.YELLOW}/assess{Colors.RESET}   : Start the structured 5-question career diagnostic wizard")
        print(f"  {Colors.YELLOW}/switch{Colors.RESET}   : Toggle LLM model between {Colors.BOLD}Groq LLaMA{Colors.RESET} & {Colors.BOLD}Gemini Flash{Colors.RESET}")
        print(f"  {Colors.YELLOW}/mode{Colors.RESET}     : Toggle personality styles ({Colors.GREEN}Friendly{Colors.RESET} | {Colors.GREEN}Professional{Colors.RESET} | {Colors.GREEN}Strict{Colors.RESET})")
        print(f"  {Colors.YELLOW}/lang{Colors.RESET}     : Toggle language ({Colors.CYAN}English{Colors.RESET} | {Colors.CYAN}Hindi (हिंदी){Colors.RESET} | {Colors.CYAN}Hinglish{Colors.RESET})")
        print(f"  {Colors.YELLOW}/stats{Colors.RESET}    : Display session token details, cost charts, and runtimes")
        print(f"  {Colors.YELLOW}/save{Colors.RESET}     : Save conversation records (JSON + formatted Markdown)")
        print(f"  {Colors.YELLOW}/clear{Colors.RESET}    : Wipe chat logs and start a new session")
        print(f"  {Colors.YELLOW}/help{Colors.RESET}     : Display this instruction menu")
        print(f"  {Colors.YELLOW}/quit{Colors.RESET}     : Export session stats and shut down safely\n")

    def compile_system_prompt(self) -> str:
        """Assembles prompt layers dynamically based on language and personality settings."""
        prompt_parts = [
            BASE_PERSONA,
            f"═══ ACTIVE PERSONALITY STYLE INSTRUCTION ═══\n{PERSONALITY_MODES[self.personality]}",
            f"═══ ACTIVE LANGUAGE INSTRUCTION ═══\n{LANGUAGE_MODES[self.language]}"
        ]
        return "\n\n".join(prompt_parts)

    def handle_api_request(self, user_message: str):
        """Pushes user message into queue, invokes the active provider, and updates stats."""
        # Append user message
        self.conversation_history.append({"role": "user", "content": user_message})
        
        # System instructions
        system_prompt = self.compile_system_prompt()
        
        # Display elegant waiting dots
        print(f"\n{Colors.DIM}⏳ CareerAI is thinking (Active model: {self.provider.upper()})...{Colors.RESET}", end="", flush=True)
        
        try:
            # Query active LLM Client with fallbacks
            ai_response, in_tokens, out_tokens, actual_provider = self.llm.execute_chat_with_retry(
                provider=self.provider,
                system_prompt=system_prompt,
                history=self.conversation_history
            )
            
            # If failover swapped the active model, update our local pointer
            if actual_provider != self.provider:
                self.provider = actual_provider
                self.switches_count += 1
            
            # Strip response whitespace
            ai_response = ai_response.strip()
            
            # Erase think line & print response
            sys.stdout.write("\r\033[K")
            print(f"\n{Colors.GREEN}{Colors.BOLD}🤖 CareerAI:{Colors.RESET}\n{ai_response}")
            
            # Save response to history
            self.conversation_history.append({"role": "assistant", "content": ai_response})
            
            # Update analytics metrics
            self.total_input_tokens += in_tokens
            self.total_output_tokens += out_tokens
            self.messages_count += 1
            
            # Display cost grids
            self.costs.print_cost_grid(in_tokens, out_tokens)
            
        except Exception as e:
            # Erase think line
            sys.stdout.write("\r\033[K")
            print(f"\n{Colors.RED}❌ Error generating response: {e}. Failed to query LLM clients.{Colors.RESET}")
            # Pop off the user message that failed to ensure conversational integrity
            self.conversation_history.pop()

    def run_structured_assessment(self):
        """Bonus Feature 1: Runs a structured 5-question assessment wizard."""
        print(f"\n{Colors.CYAN}{Colors.BOLD}🎯 STARTING QUICK CAREER DIAGNOSTIC WIZARD{Colors.RESET}")
        print(f"{Colors.DIM}Answer the following questions to help CareerAI formulate a personalized 90-day learning path.{Colors.RESET}")
        print(f"{Colors.DIM}Type /back at any point to cancel the wizard and return to chat.{Colors.RESET}")
        
        questions = [
            "What is your current background? (e.g., student, working professional, or career transitioner)",
            "What coding languages or tech frameworks are you familiar with? (e.g., Python basics, SQL, HTML, none)",
            "Which tech field excites you most? (e.g., AI/ML, Full-Stack development, DevOps, Data Science, Product Management)",
            "What is your target timeline for a transition or career launch? (e.g., 3 months, 6 months, 1 year)",
            "What is your ultimate goal? (e.g., land a job, build a startup, secure a pay raise, make your first project)"
        ]
        
        answers = []
        for i, q in enumerate(questions, 1):
            print(f"\n{Colors.BOLD}❓ Question {i}/5:{Colors.RESET} {q}")
            user_ans = input(f"   {Colors.CYAN}Your Answer:{Colors.RESET} ").strip()
            
            if user_ans.lower() == "/back":
                print(f"\n{Colors.YELLOW}↩️ Assessment wizard cancelled.{Colors.RESET}")
                return
            
            if not user_ans:
                user_ans = "Not specified"
            
            answers.append(f"Q{i}: {q}\nA{i}: {user_ans}")
        
        # Assemble structured payload
        compiled_profile = "\n\n".join(answers)
        assessment_query = (
            "I have completed the career assessment checklist. Please formulate a highly targeted "
            "career guidance blueprint using my responses below:\n\n"
            f"{compiled_profile}\n\n"
            "PROVIDE THE FOLLOWING SECTIONS IN YOUR RESPONSE:\n"
            "1. RECOMMENDED ROLES & RATIONALE: State 1-2 key career directions that perfectly fit my profile.\n"
            "2. 90-DAY ACTION TIMELINE: A specific calendar breakdown (Days 1-30, 31-60, 61-90) to learn, practice, and build.\n"
            "3. KEY CURRICULUM: Toolkits, core libraries, and exact resources to study.\n"
            "4. HIGH-IMPACT PORTFOLIO PROJECT: 1 specific, non-trivial project idea to showcase on GitHub.\n"
            "5. SALARY PROJECTIONS: Average ranges for this role in India & globally.\n"
            "6. ACTION STEP FOR TODAY: 1 simple action I can take right now to launch this journey."
        )
        
        # Run chat completion
        self.handle_api_request(assessment_query)

    def display_session_stats(self):
        """Displays formatted session token summaries and costs."""
        runtime = datetime.now() - self.session_start
        mins, secs = divmod(runtime.seconds, 60)
        tot_tok = self.total_input_tokens + self.total_output_tokens
        
        # Compute session cost based on active ratios
        tot_cost = (
            (self.total_input_tokens / 1_000_000) * CostCalculator.PRICING[self.provider]["input"] +
            (self.total_output_tokens / 1_000_000) * CostCalculator.PRICING[self.provider]["output"]
        )
        
        print(f"\n{Colors.CYAN}{Colors.BOLD}📊 CAREERAI SESSION STATISTICS:{Colors.RESET}")
        print(f"  ⏱️  Active Session Duration : {mins}m {secs}s")
        print(f"  💬  Total Message Exchanges : {self.messages_count}")
        print(f"  🔌  Active API Provider    : {self.provider.upper()} (Switched: {self.switches_count} times)")
        print(f"  🎭  Mentor Personality Mode: {self.personality.upper()}")
        print(f"  🇮🇳  Selected Language Mode : {self.language.upper()}")
        print(f"  📝  Total Tokens Transacted: {tot_tok:,}")
        print(f"      ├─ Prompt Input Tokens : {self.total_input_tokens:,}")
        print(f"      └─ Response Completion : {self.total_output_tokens:,}")
        print(f"  💰  Estimated Session Cost : ${tot_cost:.6f}")

    def save_session_exports(self):
        """Bonus Feature 2: Exports logs as structured JSON and Markdown files."""
        if not self.conversation_history:
            print(f"{Colors.YELLOW}⚠️ No active conversation history to save!{Colors.RESET}")
            return
            
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        json_file = f"exports/career_session_{timestamp}.json"
        md_file = f"exports/career_session_{timestamp}.md"
        
        tot_tok = self.total_input_tokens + self.total_output_tokens
        tot_cost = (
            (self.total_input_tokens / 1_000_000) * CostCalculator.PRICING[self.provider]["input"] +
            (self.total_output_tokens / 1_000_000) * CostCalculator.PRICING[self.provider]["output"]
        )
        
        # 1. Generate JSON Export
        export_payload = {
            "metadata": {
                "session_start": self.session_start.isoformat(),
                "export_time": datetime.now().isoformat(),
                "provider": self.provider,
                "personality": self.personality,
                "language": self.language,
                "total_messages": self.messages_count,
                "total_tokens": tot_tok,
                "total_cost_usd": tot_cost
            },
            "conversation": [
                {"role": m["role"], "content": m["content"]}
                for m in self.conversation_history
            ]
        }
        
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(export_payload, f, indent=2, ensure_ascii=False)
            
        # 2. Generate Markdown Export
        md_lines = [
            f"# 🎯 CareerAI Mentoring Session Report",
            f"\n*Exported on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*",
            f"\n## 📊 Session Metrics",
            f"- **Active Provider**: {self.provider.upper()}",
            f"- **Personality Style**: {self.personality.upper()}",
            f"- **Language Mode**: {self.language.upper()}",
            f"- **Total Messages**: {self.messages_count}",
            f"- **Total Token Footprint**: {tot_tok:,} ({self.total_input_tokens:,} In / {self.total_output_tokens:,} Out)",
            f"- **Estimated Cost**: ${tot_cost:.6f}",
            f"\n## 💬 Conversation Log\n",
            f"---"
        ]
        
        for msg in self.conversation_history:
            role_label = "👤 User" if msg["role"] == "user" else "🤖 CareerAI"
            md_lines.append(f"\n### {role_label}")
            md_lines.append(msg["content"])
            md_lines.append("\n---")
            
        with open(md_file, "w", encoding="utf-8") as f:
            f.write("\n".join(md_lines))
            
        print(f"\n{Colors.GREEN}💾 Session exported successfully!{Colors.RESET}")
        print(f"   ├─ JSON Data Log: {Colors.BOLD}{json_file}{Colors.RESET}")
        print(f"   └─ Markdown Study Report: {Colors.BOLD}{md_file}{Colors.RESET}")

    def main_loop(self):
        """Runs the main terminal thread and routes user shortcuts."""
        self.print_welcome_banner()
        
        # Initial greeting from the AI to seed the chat context
        initial_greeting_prompt = (
            "Introduce yourself briefly as CareerAI. Welcome the user warmly and "
            "ask them about their current situation and what they're looking to build "
            "or achieve in tech. Keep it to 3 sentences."
        )
        self.handle_api_request(initial_greeting_prompt)
        
        while True:
            try:
                # Capture clean user input
                prompt_symbol = f"\n{Colors.CYAN}{Colors.BOLD}👤 You [{self.provider.upper()}]:{Colors.RESET} "
                user_raw = input(prompt_symbol).strip()
                
                # Check for empty inputs
                if not user_raw:
                    continue
                
                # ---------------------------------------------------------------------
                # ROUTER: COMMAND SYSTEM
                # ---------------------------------------------------------------------
                if user_raw.startswith("/"):
                    cmd = user_raw.lower().split()[0]
                    
                    if cmd == "/quit":
                        print(f"\n{Colors.CYAN}Leaving chat... Here are your session highlights:{Colors.RESET}")
                        self.display_session_stats()
                        if self.conversation_history:
                            save_prompt = input(f"\n💾 Save conversation transcripts before exit? (y/n): ").strip().lower()
                            if save_prompt == 'y':
                                self.save_session_exports()
                        print(f"\n{Colors.GREEN}🤖 CareerAI: Best of luck on your coding voyage! Consistency beats talent. Keep learning! 🚀{Colors.RESET}")
                        break
                        
                    elif cmd == "/help":
                        self.print_help_menu()
                        continue
                        
                    elif cmd == "/clear":
                        self.conversation_history = []
                        self.total_input_tokens = 0
                        self.total_output_tokens = 0
                        self.messages_count = 0
                        self.session_start = datetime.now()
                        print(f"\n{Colors.GREEN}🔄 Conversation history wiped! Seeding new session...{Colors.RESET}")
                        self.handle_api_request(initial_greeting_prompt)
                        continue
                        
                    elif cmd == "/stats":
                        self.display_session_stats()
                        continue
                        
                    elif cmd == "/save":
                        self.save_session_exports()
                        continue
                        
                    elif cmd == "/assess":
                        self.run_structured_assessment()
                        continue
                        
                    elif cmd == "/switch":
                        self.switches_count += 1
                        if self.provider == "groq":
                            if self.llm.gemini_client_configured:
                                self.provider = "gemini"
                                print(f"\n{Colors.GREEN}🔌 Switched active provider to {Colors.BOLD}Google Gemini 1.5 Flash{Colors.RESET}.")
                            else:
                                print(f"\n{Colors.YELLOW}⚠️ Gemini key not configured. Keeping active model on Groq LLaMA.{Colors.RESET}")
                        else:
                            if self.llm.groq_client:
                                self.provider = "groq"
                                print(f"\n{Colors.GREEN}🔌 Switched active provider to {Colors.BOLD}Meta LLaMA 3.3 (Groq){Colors.RESET}.")
                            else:
                                print(f"\n{Colors.YELLOW}⚠️ Groq key not configured. Keeping active model on Google Gemini.{Colors.RESET}")
                        continue
                        
                    elif cmd == "/mode":
                        modes = ["friendly", "professional", "strict"]
                        next_idx = (modes.index(self.personality) + 1) % len(modes)
                        self.personality = modes[next_idx]
                        print(f"\n{Colors.GREEN}🎭 Personality switched to: {Colors.BOLD}{self.personality.upper()}{Colors.RESET}")
                        print(f"{Colors.DIM}Next prompt will render in this style.{Colors.RESET}")
                        continue
                        
                    elif cmd == "/lang":
                        langs = ["english", "hindi", "hinglish"]
                        next_idx = (langs.index(self.language) + 1) % len(langs)
                        self.language = langs[next_idx]
                        print(f"\n{Colors.GREEN}🇮🇳 Language toggled to: {Colors.BOLD}{self.language.upper()}{Colors.RESET}")
                        print(f"{Colors.DIM}Next response will generate in this tongue.{Colors.RESET}")
                        continue
                        
                    else:
                        print(f"\n{Colors.RED}❌ Unknown command: {cmd}. Type /help to see all commands.{Colors.RESET}")
                        continue
                
                # ---------------------------------------------------------------------
                # STANDARD DIALOGUE LOOP
                # ---------------------------------------------------------------------
                self.handle_api_request(user_raw)
                
            except KeyboardInterrupt:
                # Handle Ctrl+C gracefully
                print(f"\n\n{Colors.YELLOW}⚠️ Keyboard Interrupt detected. Typing /quit to shut down safely...{Colors.RESET}")
                self.save_session_exports()
                print(f"\n{Colors.GREEN}🤖 CareerAI: Goodbye! Happy coding! 🚀{Colors.RESET}")
                break
            except Exception as e:
                print(f"\n{Colors.RED}🔥 Critical runtime error in main loop: {e}{Colors.RESET}")

# -----------------------------------------------------------------------------
# 5. SCRIPT ENTRY POINT
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    app = CareerMentorApp()
    app.main_loop()
