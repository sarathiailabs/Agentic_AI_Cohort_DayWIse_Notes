# 📋 Day 6 – Assignment: Prompt-Engineered Content Generators

## 🎯 Assignment Overview

| Detail | Info |
| :--- | :--- |
| **Duration** | 4-6 Hours |
| **Difficulty** | Intermediate |
| **Objective** | Build a command-line tool that generates custom LinkedIn posts and outbound B2B emails using structured prompt templates. |
| **Submission** | Code Repository + Demonstration Logs + Output Files |

---

## 📝 Assignment Scenario

You are a Junior AI Engineer at a SaaS marketing agency. The company is building an automated content platform. Your job is to create two core python tools that use advanced prompting techniques (Role Prompting, Few-Shot Prompting, Delimiters, and Chain of Thought) to write high-converting copy:
1.  **LinkedIn Post Generator**
2.  **Email Generator**

---

## 🏗️ Project Structure

Your project folder must be organized as follows:
```
day6_assignment/
├── requirements.txt
├── .env.example
├── README.md
├── linkedin_post_generator.py
└── email_generator.py
```

---

## 📋 Detailed Requirements

### Part 1: LinkedIn Post Generator (`linkedin_post_generator.py`)
Create a Python script that takes a raw technical topic from the user and outputs a highly engaging, structured LinkedIn post.

**Requirements:**
- [ ] **Role Prompting:** Instruct the model to behave like an elite Tech Developer Advocate with a direct, insightful tone.
- [ ] **Few-Shot Prompting:** Provide at least 2 distinct few-shot examples showing the exact structure:
  *   An attention-grabbing hook (emoji-led)
  *   Context explaining why the topic matters
  *   3 bullet points for readability
  *   A tactical pro-tip
  *   An open engagement question
- [ ] **Delimiters:** Wrap user input in XML-like tags (e.g., `<topic>{topic}</topic>`).
- [ ] **Execution:** Use `openai` or `google-generativeai` direct APIs. Ensure temperature is set to `0.7` for balanced creativity.

---

### Part 2: Email Generator (`email_generator.py`)
Create a Python script that takes a prospect's name, role, company, and pain point, and drafts a professional cold outreach email.

**Requirements:**
- [ ] **Role Prompting:** Instruct the model to behave like a top-performing Sales Development Representative (SDR).
- [ ] **Chain of Thought (CoT):** Force the model to output a `REASONING:` block first, explaining why it mapped the prospect's pain point to a specific value prop, before drafting the `EMAIL:` block.
- [ ] **Few-Shot Prompting:** Include at least 1 complex few-shot example showing the reasoning step and the resulting email.
- [ ] **Temperature:** Set temperature to `0.3` to ensure the reasoning remains logical and the email is concise (under 150 words).

---

### Part 3: Environment Setup & Readme
- [ ] **requirements.txt:** Track dependencies (e.g., `openai`, `python-dotenv`).
- [ ] **.env.example:** Guide users on setting up keys.
- [ ] **README.md:** Detail instructions on how to install and run both generators.

---

## 🌟 Bonus Tasks (Optional, for extra points)

*   **Bonus 1 (5 points):** Output the post and email directly into markdown files (`output_post.md`, `output_email.md`).
*   **Bonus 2 (5 points):** Implement Token Counting using `tiktoken` to display input and output token counts and calculate estimated API cost.
*   **Bonus 3 (5 points):** Interactive CLI mode allowing users to input values recursively until they type `exit`.

---

## 📊 Evaluation Rubric

| Criterion | Points | Description |
| :--- | :--- | :--- |
| **Setup & Config** | 10 | Clean structure, `.env` file management, correct packages |
| **LinkedIn Generator** | 35 | Correct use of role prompting, few-shot examples, and delimiters |
| **Email Generator** | 35 | Integration of Chain of Thought reasoning and low-temperature parameters |
| **Documentation** | 10 | Complete README.md explaining execution and prompt engineering decisions |
| **Code Quality** | 10 | Modular code, error handling, comments, no hardcoded API keys |
| **Bonus Features** | Up to 15 | Markdown exports, token counting, cost logs, interactive loops |

**Total:** 100 Points (+15 Bonus)
