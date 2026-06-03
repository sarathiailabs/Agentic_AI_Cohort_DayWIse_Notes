# 🚀 Day 6 Assignment: Prompt-Engineered Content Generators

This project contains two command-line utilities designed to generate optimized tech copy:
1.  `linkedin_post_generator.py`: Creates structured LinkedIn posts from topics.
2.  `email_generator.py`: Generates personalized cold sales outreach emails using Chain of Thought reasoning.

---

## 🛠️ Setup Instructions

### 1. Prerequisite: Install `uv`
If you do not have `uv` installed, run:
```bash
# Windows PowerShell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Set Up Virtual Environment & Dependencies
Initialize your virtual environment and install the required libraries:
```bash
# Create and activate virtual environment
uv venv
.venv\Scripts\activate

# Install requirements
uv pip install -r requirements.txt
```

### 3. Add API Keys
Copy the example environment file:
```bash
copy .env.example .env
```
Open `.env` and paste your actual `OPENAI_API_KEY`.

---

## 💻 Running the Tools

### 1. LinkedIn Post Generator
To run the LinkedIn generator:
```bash
python linkedin_post_generator.py
```
*Enter a topic (e.g. "Git Merge vs Git Rebase") and get a structured, professional, emoji-hooked post.*

### 2. B2B Email Generator
To run the Email generator:
```bash
python email_generator.py
```
*Enter prospect details (Name, Role, Company, and Pain Point). The tool will output its reasoning steps before drafting the email.*
