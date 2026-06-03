# 🎯 Industry Project Reference Solution: AI Career Mentor

Welcome to the reference solution for the **Day 5 Assignment: AI Career Mentor**! This directory contains a production-quality, feature-complete command-line chatbot engineered to help students and software professionals discover and navigate tech career pathways in India and globally.

This solution demonstrates an advanced, enterprise-grade AI integration that goes far beyond a basic "hello world" chatbot. It satisfies all core rubric guidelines and implements **all 5 bonus requirements**, making it an exceptional reference model for the cohort.

---

## ✨ Features Implemented

### 1. Core Requirements (100% Covered)
- **🧠 Expert Career Persona (`CareerAI`)**: Pre-trained system prompts guiding the bot to act as a seasoned mentor with 15+ years of experience across Google, Microsoft, and tech startups. Specialized in:
  - **AI/ML Engineering** (Salary ranges: ₹8L - ₹50L+ | $80K - $300K+)
  - **Full-Stack Development** (Salary ranges: ₹5L - ₹40L+ | $70K - $250K+)
  - **Data Science & Analytics** (Salary ranges: ₹6L - ₹45L+ | $75K - $250K+)
  - **DevOps & Cloud Engineering** (Salary ranges: ₹6L - ₹35L+ | $80K - $260K+)
  - **Product Management & Founder tracks**
- **💬 Dual-Turn Conversation Memory**: A persistent conversation stack sent to LLM APIs, enabling the model to remember student details across multi-turn interactions.
- **🔌 Multi-Provider Engine**: Supports **Groq (LLaMA-3.3-70B)** as the ultra-fast primary engine and **Google Gemini 1.5 Flash** as the secondary engine. Switchable instantly with the `/switch` command.
- **🛡️ Resilience & Failover Logic**: Includes safe retry handling using exponential backoff. If the primary provider (Groq) is down or encounters rate-limiting, the app **automatically fails over** to Gemini without interrupting the session.
- **📊 Interactive Commands**:
  - `/stats`: View detailed session analytics, message tallies, connection time, and total token usage.
  - `/clear`: Clear conversation logs and start a fresh mentoring session.
  - `/save`: Save conversation records both in JSON and beautifully formatted Markdown.
  - `/quit`: Gracefully close the terminal loop.

### 2. Bonus Features (All 5 Implemented)
- **📋 1. Quick Career Assessment (`/assess` command)**: A structured 5-question discovery wizard prompting the student for their educational background, current coding skills, excitement areas, timeframe, and goals. Generates a comprehensive, tailored 90-day learning roadmap!
- **📝 2. Markdown Conversation Export**: Conversation saves are exported as rich, clean Markdown files, fully formatted with code blocks, tables, and cost breakdowns in a student-readable format.
- **💰 3. Live Token Cost Comparison Table**: After every single AI response, the app prints a neat cost comparison table showing estimated transaction costs for **Groq LLaMA**, **Gemini Flash**, and **OpenAI GPT-4o mini** based on actual prompt/response token counts.
- **🇮🇳 4. Multi-Language Indian Support (`/lang` command)**: Toggle between **English**, **Hindi (हिंदी)** in Devanagari script, and **Hinglish** (Hindi written in Roman text).
- **🎭 5. Personality Mode Switcher (`/mode` command)**: Instantly switch mentoring styles to see how prompt engineering shapes LLM outputs:
  - `Friendly` (default): Casual, extremely encouraging, uses supportive emojis.
  - `Professional`: Formal, data-centric, detailed, and direct.
  - `Strict`: No-nonsense, highly demanding, challenges the student with critical questions.

---

## 📁 Repository Structure
```
day5_assignment/
├── career_mentor.py          # Main application (interactive CLI)
├── requirements.txt          # Package dependencies
├── .env.example              # Template environment file
├── .gitignore                # Credentials and cache exclusion
├── README.md                 # This file
└── exports/                  # Directory where saved sessions are stored
    ├── sample_conversation.json
    └── sample_conversation.md
```

---

## 🚀 Setup & Installation

### Step 1: Install Python & Package Manager
Ensure you have Python 3.10+ installed. We highly recommend using `uv` for lightning-fast, sandboxed dependency execution:
```bash
# Install uv (if not already installed)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows
```

### Step 2: Clone & Navigate
Navigate to this directory in your terminal:
```bash
cd Day5_Generative_AI_and_LLM_APIs/day5_assignment
```

### Step 3: Configure API Keys
Create your local environment file:
```bash
# Windows Command Prompt / PowerShell:
copy .env.example .env
```
Open the `.env` file in your text editor and insert your keys:
- **Groq API Key**: Get it for free at [console.groq.com](https://console.groq.com/)
- **Gemini API Key**: Get it for free at [aistudio.google.com](https://aistudio.google.com/)

*Note: The app will run perfectly even if you only have one of these keys! If one key is missing, it will use the other as primary.*

### Step 4: Run the Application
You can run the application directly using `uv run`, which automatically handles virtualenvs and installs dependencies:
```bash
uv run career_mentor.py
```
Alternatively, using standard `pip`:
```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate      # Windows PowerShell: .venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt

# Run the program
python career_mentor.py
```

---

## 🎮 How to Play with the CLI

When you run the app, you will be welcomed by a clean ASCII interface:

```
╔════════════════════════════════════════════════════════════╗
║                   🎯 CAREERAI MENTOR BOT                   ║
║         Senior Tech Career Mentor & Roadmap Builder        ║
║     Powered by Groq LLaMA 3.3 & Google Gemini 1.5 Flash    ║
╚════════════════════════════════════════════════════════════╝
```

### Command Console
At any time in the chat loop, type one of these commands to control the mentor:
- `/assess` : Start the structured 5-question career assessment wizard.
- `/switch` : Toggles the active model between Groq LLaMA and Google Gemini.
- `/mode`   : Switch personality styles (`Friendly`, `Professional`, `Strict`).
- `/lang`   : Change language (`English`, `Hindi`, `Hinglish`).
- `/stats`  : Show token counts, message history, elapsed time, and cost metrics.
- `/save`   : Export the active conversation logs to JSON & formatted Markdown.
- `/clear`  : Clear history and reset.
- `/help`   : Show the help menu.
- `/quit`   : Safely exit.
