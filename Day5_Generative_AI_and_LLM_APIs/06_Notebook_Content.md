# 📓 Day 5 – Notebook Content: Generative AI & LLM APIs

> Reference content for Jupyter Notebooks. Each notebook section includes learning objectives, concept explanation, code examples, and exercises.

---

## Notebook 1: AI vs ML vs DL vs GenAI (`01_AI_vs_ML_vs_DL_vs_GenAI.ipynb`)

### Introduction

Welcome to your first AI notebook! Today we'll understand the landscape of Artificial Intelligence — from simple rule-based systems to the mind-blowing Generative AI that powers ChatGPT.

### Learning Objectives
- Understand the difference between AI, ML, DL, and GenAI
- Identify which category real-world products belong to
- Know the evolution of AI technologies

### Concept Explanation

**The Evolution of Intelligence in Machines:**

```
1950s — AI Born (Rule-based systems, chess programs)
2000s — ML Rises (Spam filters, recommendations)
2012  — DL Breakthrough (ImageNet, deep neural networks)
2017  — Transformers (Attention Is All You Need paper)
2022  — GenAI Explosion (ChatGPT launches, changes everything)
```

**Key Differences:**

| Feature       | AI          | ML              | DL               | GenAI           |
|---------------|-------------|-----------------|-------------------|-----------------|
| Learning      | May not learn| Learns from data | Learns deeply     | Learns + Creates|
| Data Needed   | None/Little | Moderate        | Massive           | Massive         |
| Example       | Calculator  | Spam Filter     | Face Recognition  | ChatGPT         |
| Output        | Decision    | Prediction      | Complex prediction| New content     |

### Real Life Examples

1. **AI (Rule-Based):** Your thermostat adjusts temperature based on rules — not learning
2. **ML:** Netflix knows you love sci-fi because it learned from your watch history
3. **DL:** Your phone recognizes your face using a deep neural network with millions of parameters
4. **GenAI:** Midjourney creates an image of "a cat astronaut on Mars" — something that never existed

### Code Example

```python
# Demonstrating the difference conceptually

# 1. Rule-Based AI — No learning
def rule_based_spam_checker(email: str) -> str:
    """Old-school AI: Check spam using hardcoded rules."""
    spam_keywords = ["free money", "click here", "lottery winner", "act now"]
    
    for keyword in spam_keywords:
        if keyword.lower() in email.lower():
            return "🚫 SPAM (Rule-Based AI)"
    return "✅ NOT SPAM (Rule-Based AI)"

# 2. Simulated ML — Learns patterns
def ml_spam_checker(email: str, trained_patterns: dict) -> str:
    """ML approach: Score based on learned patterns."""
    score = 0
    words = email.lower().split()
    for word in words:
        score += trained_patterns.get(word, 0)
    
    return f"🤖 Spam Score: {score:.1f} ({'SPAM' if score > 0.5 else 'NOT SPAM'}) (ML)"

# 3. GenAI — Would generate a complete analysis
def genai_approach():
    """GenAI: Would analyze AND generate a detailed explanation."""
    return """GenAI doesn't just classify — it can:
    - Analyze the email content
    - Explain WHY it's spam
    - Generate a safe version of the email
    - Write new email filters automatically"""

# Test
email = "Congratulations! You won free money! Click here to claim!"

print(rule_based_spam_checker(email))

trained_patterns = {"free": 0.8, "money": 0.7, "click": 0.6, "won": 0.5, "congratulations": 0.3}
print(ml_spam_checker(email, trained_patterns))

print(f"\n📝 GenAI Approach:\n{genai_approach()}")
```

### Mini Exercise
Classify these products as AI, ML, DL, or GenAI:
1. Google Translate → ?
2. Siri → ?
3. Tesla Autopilot → ?
4. DALL-E → ?
5. Excel Formulas → ?
6. GitHub Copilot → ?

**Answers:** 1-DL, 2-AI/ML, 3-DL, 4-GenAI, 5-AI, 6-GenAI

### Industry Exercise
Research and classify 5 products from your current company or university that use AI/ML/DL/GenAI.

---

## Notebook 2: How LLMs Work (`02_How_LLMs_Work.ipynb`)

### Introduction
Let's peek under the hood of ChatGPT. How does a machine generate human-like text?

### Learning Objectives
- Understand next-token prediction
- Know what the Transformer architecture does
- Understand the training pipeline

### Concept Explanation

**LLMs are Next-Token Prediction Machines:**

```
Input:  "The quick brown fox"
Output: "jumps" (with 85% probability)

The model predicts one word at a time, then uses that word to predict the next:
"The" → "quick" → "brown" → "fox" → "jumps" → "over" → "the" → "lazy" → "dog"
```

**The Transformer Architecture (Simplified):**

```
Input Text
    ↓
[Tokenizer]     → Break text into tokens
    ↓
[Embeddings]    → Convert tokens to numbers (vectors)
    ↓
[Self-Attention] → Understand relationships between words
    ↓
[Feed-Forward]  → Process and transform
    ↓
[Output Layer]  → Predict next token probabilities
    ↓
Next Token
```

### Code Example

```python
"""
Simulating how an LLM predicts the next token.
This is a simplified version to build intuition.
"""

import random

# Simplified "trained" probabilities (in real LLMs, this comes from training)
next_word_probabilities = {
    "the": {"cat": 0.3, "dog": 0.2, "quick": 0.15, "best": 0.1, "world": 0.1, "big": 0.15},
    "cat": {"sat": 0.4, "is": 0.3, "jumped": 0.2, "ran": 0.1},
    "sat": {"on": 0.6, "down": 0.3, "quietly": 0.1},
    "on": {"the": 0.5, "a": 0.3, "top": 0.2},
    "python": {"is": 0.5, "programming": 0.3, "code": 0.2},
    "is": {"a": 0.4, "the": 0.2, "great": 0.2, "very": 0.2},
}

def predict_next_token(current_word: str, temperature: float = 0.7) -> str:
    """Simulate next-token prediction like an LLM."""
    if current_word.lower() not in next_word_probabilities:
        return "[END]"
    
    probs = next_word_probabilities[current_word.lower()]
    words = list(probs.keys())
    weights = list(probs.values())
    
    # Apply temperature
    if temperature == 0:
        return words[weights.index(max(weights))]
    
    adjusted = [w ** (1/temperature) for w in weights]
    total = sum(adjusted)
    adjusted = [w/total for w in adjusted]
    
    return random.choices(words, weights=adjusted, k=1)[0]

def generate_text(start_word: str, num_tokens: int = 5, temperature: float = 0.7) -> str:
    """Generate text token by token, like an LLM."""
    text = [start_word]
    current = start_word
    
    for _ in range(num_tokens):
        next_token = predict_next_token(current, temperature)
        if next_token == "[END]":
            break
        text.append(next_token)
        current = next_token
    
    return " ".join(text)

# Generate with different temperatures
print("🤖 Simulated LLM Text Generation")
print("=" * 50)

for temp in [0.0, 0.5, 1.0, 1.5]:
    print(f"\n🌡️ Temperature: {temp}")
    for i in range(3):
        result = generate_text("the", num_tokens=4, temperature=temp)
        print(f"  Run {i+1}: {result}")
```

### Mini Exercise
Modify the `next_word_probabilities` dictionary to add your own word sequences. Try generating a sentence about "python programming".

### Industry Exercise
Research: How much does it cost to train GPT-4? What hardware is needed? Write a brief summary.

---

## Notebook 3: Tokens and Context Window (`03_Tokens_and_Context_Window.ipynb`)

### Introduction
Understanding tokens is understanding the economics of AI. Every API call, every cost calculation revolves around tokens.

### Learning Objectives
- Count tokens in any text
- Calculate API costs
- Understand context window limits
- Optimize token usage

### Code Example

```python
"""
Mastering Tokens: Count, Analyze, and Optimize
"""

# Install: pip install tiktoken
import tiktoken

# Initialize the tokenizer for GPT-4o
encoder = tiktoken.encoding_for_model("gpt-4o")

# === SECTION 1: Basic Token Counting ===
print("📊 SECTION 1: Basic Token Counting")
print("=" * 50)

texts = {
    "Simple greeting": "Hello, how are you?",
    "Python code": "def hello():\n    print('Hello World')",
    "Technical term": "Artificial Intelligence and Machine Learning",
    "Long word": "Supercalifragilisticexpialidocious",
    "Numbers": "The year 2024 has 365 days and 8760 hours",
    "URL": "https://www.openai.com/research/gpt-4",
    "Emoji": "I love coding! 🐍💻🚀",
}

for label, text in texts.items():
    tokens = encoder.encode(text)
    ratio = len(text) / len(tokens)
    print(f"\n  📝 {label}")
    print(f"     Text: {text}")
    print(f"     Characters: {len(text)} | Tokens: {len(tokens)} | Ratio: {ratio:.1f} chars/token")

# === SECTION 2: Cost Calculator ===
print("\n\n💰 SECTION 2: API Cost Calculator")
print("=" * 50)

def calculate_cost(input_text: str, output_tokens: int = 500, model: str = "gpt-4o-mini"):
    """Calculate the cost of an API call."""
    pricing = {
        "gpt-4o": {"input": 2.50, "output": 10.00},
        "gpt-4o-mini": {"input": 0.15, "output": 0.60},
        "claude-3.5-sonnet": {"input": 3.00, "output": 15.00},
        "gemini-1.5-flash": {"input": 0.075, "output": 0.30},
        "groq-llama-70b": {"input": 0.59, "output": 0.79},
    }
    
    input_tokens = len(encoder.encode(input_text))
    model_pricing = pricing.get(model, pricing["gpt-4o-mini"])
    
    input_cost = (input_tokens / 1_000_000) * model_pricing["input"]
    output_cost = (output_tokens / 1_000_000) * model_pricing["output"]
    
    return {
        "model": model,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "input_cost": input_cost,
        "output_cost": output_cost,
        "total_cost": input_cost + output_cost,
    }

# Example: A customer support message
support_message = """
Hi, I'm having trouble with my order #12345. I placed it on Monday and 
it was supposed to arrive by Wednesday but it's now Friday and I still 
haven't received it. Can you please help me track it? I've already 
checked the tracking number but it shows no updates since Tuesday.
"""

for model in ["gpt-4o-mini", "gpt-4o", "claude-3.5-sonnet", "groq-llama-70b"]:
    result = calculate_cost(support_message, output_tokens=300, model=model)
    print(f"\n  🤖 {result['model']}")
    print(f"     Input: {result['input_tokens']} tokens → ${result['input_cost']:.6f}")
    print(f"     Output: {result['output_tokens']} tokens → ${result['output_cost']:.6f}")
    print(f"     Total: ${result['total_cost']:.6f}")

# === SECTION 3: Monthly Cost Projection ===
print("\n\n📈 SECTION 3: Monthly Cost Projection")
print("=" * 50)

daily_requests = 10000
avg_input_tokens = 500
avg_output_tokens = 300

for model in ["gpt-4o-mini", "gpt-4o", "groq-llama-70b"]:
    result = calculate_cost("x" * avg_input_tokens, avg_output_tokens, model)
    daily_cost = result["total_cost"] * daily_requests
    monthly_cost = daily_cost * 30
    
    print(f"\n  🤖 {model}")
    print(f"     Daily ({daily_requests:,} requests): ${daily_cost:.2f}")
    print(f"     Monthly: ${monthly_cost:.2f}")

# === SECTION 4: Context Window Visualization ===
print("\n\n📏 SECTION 4: Context Window Usage")
print("=" * 50)

context_windows = {
    "GPT-3.5 Turbo": 16_385,
    "GPT-4o": 128_000,
    "Claude 3.5 Sonnet": 200_000,
    "Gemini 1.5 Pro": 2_000_000,
}

system_prompt_tokens = 500
avg_message_tokens = 100
avg_response_tokens = 300

for model_name, window_size in context_windows.items():
    remaining = window_size - system_prompt_tokens
    max_exchanges = remaining // (avg_message_tokens + avg_response_tokens)
    usage_percent = (system_prompt_tokens / window_size) * 100
    
    print(f"\n  🤖 {model_name} (Context: {window_size:,} tokens)")
    print(f"     System prompt uses: {usage_percent:.2f}%")
    print(f"     Max conversation exchanges: ~{max_exchanges:,}")
    bar_length = min(50, window_size // 4000)
    print(f"     Capacity: {'█' * bar_length}{'░' * (50 - bar_length)}")
```

### Mini Exercise
Calculate how much it would cost to run a chatbot for a school with 500 students, each asking 10 questions per day, using GPT-4o-mini.

### Industry Exercise
You're the CTO of a startup. You need to choose between GPT-4o, Gemini 1.5 Flash, and Groq LLaMA 70B for a customer support bot that handles 50,000 messages/day. Create a cost comparison spreadsheet and make a recommendation.

---

## Notebook 4: Temperature and Hallucinations (`04_Temperature_and_Hallucinations.ipynb`)

### Introduction
Two critical concepts every AI engineer must master: controlling creativity (temperature) and managing risks (hallucinations).

### Learning Objectives
- Use temperature effectively for different use cases
- Detect and mitigate hallucinations
- Build safer AI applications

### Code Example — Temperature Experiment

```python
"""
Temperature Deep Dive: See the effect in real-time
"""

from groq import Groq

client = Groq(api_key="your-groq-key")

def generate_with_temperature(prompt: str, temperature: float, num_samples: int = 3) -> list:
    """Generate multiple responses at a specific temperature."""
    responses = []
    for _ in range(num_samples):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=100
        )
        responses.append(response.choices[0].message.content.strip())
    return responses

# Experiment 1: Factual Question
print("🔬 EXPERIMENT 1: Factual Question")
print("Prompt: 'What is the capital of France?'")
print("=" * 50)

for temp in [0.0, 0.5, 1.0]:
    responses = generate_with_temperature("What is the capital of France?", temp)
    print(f"\n🌡️ Temperature: {temp}")
    for i, r in enumerate(responses, 1):
        print(f"  Run {i}: {r[:80]}")

# Experiment 2: Creative Question
print("\n\n🔬 EXPERIMENT 2: Creative Question")
print("Prompt: 'Write a haiku about Python programming'")
print("=" * 50)

for temp in [0.0, 0.7, 1.5]:
    responses = generate_with_temperature("Write a haiku about Python programming", temp)
    print(f"\n🌡️ Temperature: {temp}")
    for i, r in enumerate(responses, 1):
        print(f"  Run {i}: {r[:100]}")
```

### Code Example — Hallucination Detection

```python
"""
Hallucination Detection & Mitigation Strategies
"""

from groq import Groq

client = Groq(api_key="your-groq-key")

def ask_with_guardrails(question: str) -> str:
    """Ask a question with hallucination mitigation."""
    system_prompt = """You are a helpful, honest assistant.

CRITICAL RULES:
1. If you're not sure about something, say "I'm not certain about this."
2. If a fact is from before your training cutoff, mention it might be outdated.
3. Never make up citations, URLs, research papers, or statistics.
4. If asked about something that doesn't exist, say "I couldn't find information about this."
5. For math, show your work step by step.
"""
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        temperature=0.0  # Low temperature for factual accuracy
    )
    
    return response.choices[0].message.content

def ask_without_guardrails(question: str) -> str:
    """Ask the same question without guardrails."""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": question}],
        temperature=0.7
    )
    return response.choices[0].message.content

# Test questions that commonly trigger hallucinations
test_questions = [
    "Who wrote the book 'Digital Minds of Tomorrow' published in 2023?",
    "What was Apple's revenue in Q3 2025?",
    "Cite 3 research papers about quantum computing from Nature journal.",
]

print("🔍 HALLUCINATION COMPARISON: With vs Without Guardrails")
print("=" * 70)

for q in test_questions:
    print(f"\n❓ Question: {q}")
    print(f"\n  ⚠️ WITHOUT guardrails:")
    print(f"     {ask_without_guardrails(q)[:200]}...")
    print(f"\n  ✅ WITH guardrails:")
    print(f"     {ask_with_guardrails(q)[:200]}...")
    print("-" * 70)
```

### Mini Exercise
Create a function that checks if an LLM response contains potential hallucination markers (made-up URLs, suspiciously specific statistics, etc.)

### Industry Exercise
Design a hallucination mitigation system for a medical chatbot. What system prompt, temperature, and additional checks would you implement?

---

## Notebook 5: AI Career Mentor (`05_AI_Career_Mentor.ipynb`)

### Introduction
Let's build a complete AI application — an AI Career Mentor that helps students choose their tech career path.

### Learning Objectives
- Design a complete AI application from scratch
- Implement conversation memory
- Use system prompts for behavior control
- Handle edge cases and errors

### Code Example

```python
"""
🎯 AI Career Mentor — Industry Project
A complete AI-powered career guidance chatbot for tech professionals.
"""

from groq import Groq
from datetime import datetime

# Initialize
client = Groq(api_key="your-groq-key")

# Professional system prompt
SYSTEM_PROMPT = """You are CareerAI, a senior tech career mentor with 15 years of experience 
in the tech industry. You've worked at Google, Microsoft, and helped 500+ professionals 
transition into tech careers.

YOUR EXPERTISE:
- AI/ML Engineering career paths
- Software Development career paths
- Data Science and Analytics
- DevOps and Cloud Engineering
- Product Management in Tech
- Startup vs Corporate career choices

YOUR APPROACH:
1. First understand the person's background, skills, and interests
2. Ask clarifying questions before giving advice
3. Provide specific, actionable steps (not generic advice)
4. Mention real companies, job titles, and salary ranges
5. Suggest specific courses, certifications, and projects
6. Be encouraging but realistic about timelines

YOUR STYLE:
- Professional but friendly
- Use bullet points for clarity
- Give specific examples and timelines
- Mention relevant companies and roles
- Include salary ranges when relevant (in INR and USD)

IMPORTANT RULES:
- Always ask at least 2 questions before giving career advice
- If someone seems confused, break down the options clearly
- Never guarantee job placement or specific salaries
- Recommend building a portfolio and GitHub profile
- Mention that networking is as important as skills
"""

class CareerMentor:
    """AI Career Mentor with conversation management."""
    
    def __init__(self):
        self.conversation = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
        self.message_count = 0
        self.session_start = datetime.now()
    
    def chat(self, user_message: str) -> str:
        """Process user message and return AI response."""
        self.message_count += 1
        
        # Add user message to history
        self.conversation.append({
            "role": "user",
            "content": user_message
        })
        
        try:
            # Call the LLM
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=self.conversation,
                temperature=0.7,
                max_tokens=1024
            )
            
            ai_response = response.choices[0].message.content
            
            # Save to conversation history
            self.conversation.append({
                "role": "assistant",
                "content": ai_response
            })
            
            return ai_response
            
        except Exception as e:
            error_msg = f"I'm having trouble connecting right now. Error: {str(e)}"
            return error_msg
    
    def get_session_info(self) -> str:
        """Get current session statistics."""
        duration = (datetime.now() - self.session_start).seconds
        total_tokens = sum(len(m["content"].split()) for m in self.conversation)
        
        return (f"📊 Session Stats:\n"
                f"   Messages: {self.message_count}\n"
                f"   Duration: {duration // 60}m {duration % 60}s\n"
                f"   Approx. words exchanged: {total_tokens}")
    
    def reset(self):
        """Start a new conversation."""
        self.conversation = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
        self.message_count = 0
        self.session_start = datetime.now()

def main():
    """Main application loop."""
    mentor = CareerMentor()
    
    print("=" * 60)
    print("🎯 AI CAREER MENTOR")
    print("Your personal tech career guidance assistant")
    print("=" * 60)
    print("\nCommands:")
    print("  'quit'  — Exit the application")
    print("  'stats' — View session statistics")
    print("  'reset' — Start a new conversation")
    print("  'help'  — Show these commands")
    print("=" * 60)
    
    # Welcome message
    welcome = mentor.chat(
        "Introduce yourself briefly and ask the user about their "
        "current background and career interests."
    )
    print(f"\n🤖 CareerAI: {welcome}")
    
    while True:
        user_input = input("\n👤 You: ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() == 'quit':
            print(f"\n{mentor.get_session_info()}")
            print("\n🤖 CareerAI: Best of luck with your career journey! "
                  "Remember — consistency beats talent. Keep learning! 🚀")
            break
        
        if user_input.lower() == 'stats':
            print(f"\n{mentor.get_session_info()}")
            continue
        
        if user_input.lower() == 'reset':
            mentor.reset()
            print("\n🔄 Conversation reset. Starting fresh!")
            welcome = mentor.chat(
                "Introduce yourself briefly and ask about their background."
            )
            print(f"\n🤖 CareerAI: {welcome}")
            continue
        
        if user_input.lower() == 'help':
            print("\nCommands: 'quit', 'stats', 'reset', 'help'")
            continue
        
        response = mentor.chat(user_input)
        print(f"\n🤖 CareerAI: {response}")

if __name__ == "__main__":
    main()
```

### Mini Exercise
Add a feature to save the conversation to a text file when the user types 'save'.

### Industry Exercise
Extend the Career Mentor with:
1. Multi-language support (user can ask in Hindi)
2. Export conversation as PDF
3. Add a "Quick Assessment" mode that asks 5 predefined questions
4. Track which topics the user asked about most

### Summary

| Notebook | Key Concept | Practical Skill |
|----------|-------------|-----------------|
| 01 | AI/ML/DL/GenAI | Classify technologies |
| 02 | How LLMs Work | Understand prediction |
| 03 | Tokens & Context | Calculate costs |
| 04 | Temperature & Hallucinations | Build safer AI |
| 05 | AI Career Mentor | Build complete AI app |
