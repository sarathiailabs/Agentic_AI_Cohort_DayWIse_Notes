# 🎓 Day 6 Student Review & Session Recap: Prompt Engineering

Welcome to your study and review guide for **Day 6: Prompt Engineering**! 
This document contains the core concepts, code templates, assignment details, and interview questions to help you master the art of instructing LLMs.

---

## 🎯 Session Overview

| Detail | Info |
| :--- | :--- |
| **Topic** | Prompt Engineering (Zero-Shot, Few-Shot, Role Prompting, CoT, ReAct) |
| **Core API** | OpenAI Chat Completions API |
| **Assignment** | Build LinkedIn Post Generator & B2B Outbound Email Generator |
| **Reference Materials** | [Main Lecture](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day6_Prompt_Engineering/Day6_Teaching_content/01_Main_Lecture.md) \| [Code Examples](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day6_Prompt_Engineering/Day6_Teaching_content/07_Code_Examples.ipynb) \| [Assignment Solution](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day6_Prompt_Engineering/Day6_Teaching_content/14_Assignment_Solution.md) |

---

## 🧠 Core Concepts: Quick Revision

### 1. Zero-Shot vs. Few-Shot Prompting
*   **Zero-Shot:** You ask the model to perform a task without giving it any examples. Useful for simple tasks.
*   **Few-Shot:** You provide **3 to 5 examples** of the task inside the prompt to guide the model's formatting, style, and classification labels. Few-shot prompting works via **in-context learning** using the model's attention mechanism.

### 2. Role Prompting
Assigning a specific persona (e.g. "You are an elite cyber security auditor") restricts the model's target token distribution, making its output significantly more professional and tailored.

### 3. Chain of Thought (CoT) Prompting
Forcing the model to output its intermediate reasoning steps (e.g., using `"Let's think step-by-step"`) creates a scratchpad memory in the output context, ensuring calculations and logic are correct before outputting the final answer.

---

## 🛠️ Code Cheatsheet & Setup

### Dependencies Installation (Using `uv`)
```bash
uv pip install openai python-dotenv
```

### Complete Code Template (Few-Shot & Role Prompting)
```python
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load env variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

role_prompt = "You are a professional technical copywriter."
few_shot_prompt = """
Input: Python virtual environment
Output: 📦 Stop installing global packages! Use virtual envs to isolate dependency trees.
---
Input: Git branch merging
Output: 🔀 Keep commit history clean by using git rebase for linear logs.
---
Input: SQL indexes
Output:
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": role_prompt},
        {"role": "user", "content": few_shot_prompt}
    ],
    temperature=0.7
)
print(response.choices[0].message.content.strip())
```

---

## 📋 Assignment Overview: Build Custom Copy Generators

Your task is to build two command-line tools in python under `Day6_Prompt_Engineering/day6_assignment/`:
1.  **LinkedIn Post Generator:** Prompts the model as a Developer Advocate to generate viral, structured tech posts.
2.  **Outbound Email Generator:** Uses Role Prompting and Chain of Thought to write highly targeted sales emails based on pain points.

Use the provided [Assignment Solution](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day6_Prompt_Engineering/Day6_Teaching_content/14_Assignment_Solution.md) as a reference guide.

---

## ⚠️ Common Mistakes to Avoid

1.  **High Temperature on Logic Tasks:** Set `temperature=0` for logic, math, and structured JSON generation.
2.  **Negative Prompts:** Avoid "Do not write about politics." Rephrase positively: "Focus exclusively on tech topics."
3.  **Vague Personas:** Use detailed, context-rich role prompts rather than simple phrases like "Act as a writer."

---

## 💬 Interview Preparation Q&A

### Q1: Why does Chain of Thought prompting improve LLM performance on arithmetic tasks?
*   **Answer:** LLMs generate text token-by-token. Without CoT, they must output the final answer in a single forward pass, which often fails for multi-step math. CoT prompts the model to write out the mathematical operations sequentially, saving intermediate steps in its active context.

### Q2: What is the main difference between few-shot prompting and fine-tuning?
*   **Answer:** Few-shot prompting works dynamically in the forward pass by passing examples in the input context (in-context learning) without changing the neural network's weights. Fine-tuning permanently alters model weights by training the model on a dataset using gradient descent.
