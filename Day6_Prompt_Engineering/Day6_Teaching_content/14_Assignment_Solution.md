# ✅ Day 6 – Assignment Solution Reference

This document provides a comprehensive solution guide for the Day 6 Assignment: Prompt-Engineered Content Generators.

---

## 🏗️ Solution Architecture

The solution implements two separate Python scripts leveraging the official OpenAI API and the `python-dotenv` package to load keys securely.

```
day6_assignment/
├── requirements.txt
├── .env.example
├── README.md
├── linkedin_post_generator.py
└── email_generator.py
```

---

## 🛠️ Code Implementation Reference

### 1. LinkedIn Post Generator (`linkedin_post_generator.py`)

This implementation demonstrates **Role Prompting**, **Few-Shot Examples**, and **Delimiters** with a creative temperature setting (`0.7`).

```python
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Initialize Client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY is not set in environment.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

SYSTEM_PROMPT = """
You are an expert Tech Developer Advocate and copywriter who writes viral, highly engaging LinkedIn updates.
Your tone is technical, insightful, and clear. Avoid standard corporate jargon like 'thrilled to announce'.

Always format every post using this structure:
1. Hook: An attention-grabbing first line (starts with an emoji).
2. Context: 2 sentences explaining why the topic is vital.
3. Bullets: 3 punchy, bulleted takeaways (using '-' as bullet point).
4. Pro-tip: A tactical '💡 Pro-tip:' line.
5. CTA: An open question to start a discussion in comments.
"""

FEW_SHOT_EXAMPLES = """
Example 1:
Topic: Stop using global pip installations
Post:
📦 Stop installing Python packages globally!

Every time you run 'pip install' without a virtual environment, you risk breaking your system path.

Here is why virtual environments are non-negotiable:
- Keeps dependency trees isolated per project
- Avoids version conflicts on shared system libraries
- Makes local builds identical to production environments

💡 Pro-tip: Use 'uv venv' to create virtualenvs in less than 0.1 seconds.

Are you still using global installations, or have you switched? Let's discuss below! 👇
---
Example 2:
Topic: Git Rebase vs Git Merge
Post:
🔀 Git Merge or Git Rebase? Stop arguing and learn when to use which.

Choosing the wrong branch strategy can clutter your history or delete valuable commit context.

Key guidelines for developers:
- Use 'git merge' to preserve the complete history of feature branches
- Use 'git rebase' to keep your main branch commit history linear
- Never rebase commits that have been pushed to a public repository

💡 Pro-tip: Run 'git log --graph --oneline' to visualize your commit tree.

What's your team's branching policy? Let's discuss in the comments! 👇
---
"""

def generate_linkedin_post(topic: str) -> str:
    user_prompt = f"""
    {FEW_SHOT_EXAMPLES}
    
    Topic: <topic>{topic}</topic>
    Post:
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"API Error: {str(e)}"

if __name__ == "__main__":
    print("--- LinkedIn Post Generator ---")
    topic = input("Enter the topic for your LinkedIn post: ")
    if not topic:
        topic = "Learning Git workflows"
    
    print("\nGenerating post...")
    post = generate_linkedin_post(topic)
    print("\n" + "="*50)
    print(post)
    print("="*50)
```

---

### 2. Email Generator (`email_generator.py`)

This implementation demonstrates **Chain of Thought (CoT) prompting**, **Role Prompting**, and a low temperature (`0.3`) parameter.

```python
import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Initialize Client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY is not set in environment.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

SYSTEM_PROMPT = """
You are an elite Sales Development Representative (SDR). Your outbound emails are highly personalized, clear, and under 150 words.
You avoid generic buzzwords like 'synergy', 'disruptive', or 'cutting-edge'.

For every prospect input, you must think through their pain point first. 

Your output format MUST be:
REASONING:
- [bullet point analyzing their pain point]
- [bullet point mapping pain point to value proposition]

EMAIL:
Subject: [Short, clear subject line]
Hi [Name],

[Hook connecting to their role or company]
[Value prop directly solving their pain point]
[Call to Action proposing a brief discussion]

Best,
[Your Name]
"""

FEW_SHOT_EXAMPLES = """
PROSPECT DETAILS:
Name: Jane Smith
Role: VP of Engineering
Company: FinTechCorp
Pain Point: API response times are slowing down checkout conversions.

Output:
REASONING:
- Prospect is a tech leader concerned with checkout conversion speeds.
- Stripe offers a optimized payment gateway API with 99.99% uptime and <100ms response times.
- Hook should reference checkout latency.

EMAIL:
Subject: Reducing checkout latency at FinTechCorp
Hi Jane,

I notice FinTechCorp has been scaling customer transactions, but checkout page latency can easily cost up to 1% of conversion revenue.

Stripe's payment APIs are built to handle high volume under 100ms, helping engineering teams speed up payments without adding infrastructure.

Do you have 5 minutes this Wednesday for a quick discussion on payment performance benchmarks?

Best,
Alex
---
"""

def generate_email(name: str, role: str, company: str, pain: str) -> str:
    user_prompt = f"""
    {FEW_SHOT_EXAMPLES}
    
    PROSPECT DETAILS:
    Name: {name}
    Role: {role}
    Company: {company}
    Pain Point: {pain}
    
    Output:
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"API Error: {str(e)}"

if __name__ == "__main__":
    print("--- Outbound B2B Email Generator ---")
    p_name = input("Prospect Name: ")
    p_role = input("Prospect Role: ")
    p_comp = input("Prospect Company: ")
    p_pain = input("Prospect Pain Point: ")
    
    if not p_name:
        p_name, p_role, p_comp, p_pain = "David Miller", "VP of Operations", "LogisticsHub", "High package tracking error rate."
        
    print("\nGenerating email with Chain of Thought reasoning...")
    email = generate_email(p_name, p_role, p_comp, p_pain)
    print("\n" + "="*50)
    print(email)
    print("="*50)
```
