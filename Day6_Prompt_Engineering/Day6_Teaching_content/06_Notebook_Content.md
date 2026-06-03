# 📓 Day 6 – Notebook Content: Prompt Engineering

This document outlines the markdown narratives and code segments contained in the Day 6 Jupyter Notebooks:
*   [07_Code_Examples.ipynb](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day6_Prompt_Engineering/Day6_Teaching_content/07_Code_Examples.ipynb)
*   [08_Mini_Project.ipynb](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day6_Prompt_Engineering/Day6_Teaching_content/08_Mini_Project.ipynb)
*   [09_Industry_Project.ipynb](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day6_Prompt_Engineering/Day6_Teaching_content/09_Industry_Project.ipynb)

---

## 📕 Notebook 1: Code Examples (`07_Code_Examples.ipynb`)

### 1. Introduction
"This notebook teaches the core prompting strategies programmatically using python-dotenv and the OpenAI API. We will implement Zero-Shot, Few-Shot, Role Prompting, and Chain of Thought."

### 2. Dependency Setup
```python
# Import libraries
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load env variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

### 3. Concept 1: Zero-Shot vs Few-Shot
*   **Zero-Shot Prompt:**
    ```python
    prompt = "Convert 'I want to cancel my ticket' to SQL."
    ```
*   **Few-Shot Prompt:**
    ```python
    prompt = """
    Convert English user requests to SQL queries.
    
    Request: "Show all users from India"
    SQL: SELECT * FROM users WHERE country = 'India';
    
    Request: "Find the count of products with price above 100"
    SQL: SELECT COUNT(*) FROM products WHERE price > 100;
    
    Request: "Show names of employees hired in 2023"
    SQL: SELECT name FROM employees WHERE hire_year = 2023;
    
    Request: "Get all records of users who registered last month"
    SQL:
    """
    ```

---

## 📗 Notebook 2: Mini Project (`08_Mini_Project.ipynb`)

### 1. Project Goal: LinkedIn Post Generator
"Build a LinkedIn Post Generator that converts raw ideas into high-performing, niche-specific, and formatted updates. We will write prompts containing role instructions and few-shot formatting examples."

### 2. Prompt Template Formulation
```python
role_prompt = """
You are a top-performing developer advocate and tech copywriter. 
Your target audience is developers, startup founders, and technical leads.
Your posts use a hook, bullet points for readability, bold headings, and a single call-to-action. No generic fluff.
"""

few_shot_examples = """
Topic: Setting up virtual envs in Python
Post:
📦 Stop installing Python packages globally! 

Here is why you need a virtual environment today:
- Prevents dependency conflicts between projects
- Makes deployment reproducible (pip freeze > requirements.txt)
- Keeps your base system system pristine

💡 Pro-tip: Use 'uv venv' to create environments in less than 0.1 seconds.

What is your preferred environment manager? Let me know below! 👇
---
"""
```

---

## 📘 Notebook 3: Industry Project (`09_Industry_Project.ipynb`)

### 1. Project Goal: Smart Email Writer
"Build an automated business email generator that drafts outbound cold emails and follow-ups based on prospects' business data (e.g. company name, industry, paint points). We will implement a multi-stage prompt combining Role Prompting, Few-Shot structures, and Chain of Thought planning."

### 2. Multi-Stage Reasoning Email Code
```python
def generate_email(prospect_data):
    prompt = f"""
    You are an elite Sales Development Representative (SDR) at Stripe. 
    Write an outbound sales email to the following prospect:
    
    PROSPECT DETAILS:
    Name: {prospect_data['name']}
    Role: {prospect_data['role']}
    Company: {prospect_data['company']}
    Pain Point: {prospect_data['pain_point']}
    
    INSTRUCTIONS:
    First, think step-by-step about what value proposition Stripe offers to solve this specific pain point.
    Write your reasoning under the section "REASONING:".
    Then, write the email under the section "EMAIL:". Keep it under 150 words.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content
```
