# 📖 Day 6 Complete Guide: Prompt Engineering

## Master Reference Document

**Day:** 6 of 20  
**Topic:** Prompt Engineering  
**Duration:** 2-3 hours of content  
**Difficulty Level:** Beginner to Intermediate  
**Prerequisites:** Generative AI & LLM APIs (Day 5)

---

## 🎯 Executive Summary
Prompt Engineering is the core engineering discipline of interacting with Large Language Models (LLMs). This guide provides the complete, end-to-end curriculum for Day 6 of the Bootcamp, teaching students how to move from simple unstructured queries to structured, programmatic prompt templates using **Zero-Shot, Few-Shot, Role Prompting, Chain of Thought (CoT)**, and **ReAct Prompting**.

---

## 🗺️ Detailed Syllabus & Learning Map

```
┌────────────────────────────────────────────────────────────────────────┐
│                        DAY 6 LEARNING ROADMAP                          │
├──────────────────┬──────────────────┬──────────────────┬───────────────┤
│  1. Problem      │  2. Few-Shot     │  3. Personas     │  4. Reasoning │
│  Raw queries     │  In-context      │  Role prompting  │  CoT & ReAct  │
│  fail in prod    │  learning        │  constrains vocabulary│  loop mechanics│
└──────────────────┴──────────────────┴──────────────────┴───────────────┘
```

---

## 📚 Section 1: The Core Concepts

### 1. The Mind Reading Fallacy
LLMs do not understand intent; they calculate mathematical probabilities. A prompt is the boundary condition that restricts their vocabulary space to generate the desired result.

### 2. Prompting Techniques Breakdown

#### Zero-Shot Prompting
*   **Definition:** Requesting a task without providing examples.
*   **Use case:** Common knowledge queries, translations.

#### Few-Shot Prompting
*   **Definition:** Providing input-output examples in the context.
*   **Use case:** Structuring JSON data, teaching custom classifications, style alignment.

#### Role Prompting (Personas)
*   **Definition:** Telling the model to act as a specific expert.
*   **Use case:** Writing articles in a specific brand tone, security auditing.

#### Chain of Thought (CoT)
*   **Definition:** Prompting the model to write calculations or thoughts before outputting the final answer.
*   **Use case:** Solving math equations, logic puzzles, coding design decisions.

#### ReAct Prompting
*   **Definition:** Combining reasoning thoughts with programmatic tool calls in an alternating sequence.
*   **Use case:** The foundation of autonomous AI agents.

---

## 🎨 Section 2: Whiteboard Drawings (ASCII)

```
LLM Reasoning Space with Chain of Thought:
┌────────────────────────────────────────────────────────┐
│ USER QUERY:                                            │
│ "A store starts with 100 apples. Monday they sell 10.  │
│  Tuesday they sell double Monday's. How many left?"    │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ LLM INTERMEDIATE REASONING SCRATCHPAD:                 │
│ - Monday starting count = 100                          │
│ - Monday sold = 10                                     │
│ - Monday remaining = 100 - 10 = 90                     │
│ - Tuesday sold = 10 * 2 = 20                           │
│ - Tuesday remaining = 90 - 20 = 70                     │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ FINAL RESPONSE:                                        │
│ "They have 70 apples left."                            │
└────────────────────────────────────────────────────────┘
```

---

## 💻 Section 3: Live Demos & Code Snippets

### Sentiment Triage Demo
```python
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

few_shot_prompt = """
Classify into tags: [PROD-BUG], [BILLING], [SUPPORT].
Feedback: "Can I get a refund for my subscription?" -> Tag: [BILLING]
Feedback: "The checkout button is broken on Firefox." -> Tag: [PROD-BUG]
Feedback: "My account login doesn't work on mobile." -> Tag:
"""
# Set temperature to 0 for deterministic categorization
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": few_shot_prompt}],
    temperature=0
)
print("Tag:", response.choices[0].message.content.strip())
```

---

## ⚠️ Section 4: Common Mistakes & FAQs

### The Top 3 Mistakes:
1.  **High Temperature for Coding/Logic:** High temperature introduces random token paths, violating syntax rules. Set `temperature=0` for coding.
2.  **Negative Constraints:** Models focus on the nouns in negative instructions (e.g., "Do not write code" might trigger code generation). Frame rules positively.
3.  **Prompt Leakage:** Failing to guard system instructions against user jailbreaks.

---

## 📋 Section 5: Student Assignment Overview

Students will build two production-grade utilities:
1.  **LinkedIn Post Generator:** Using role prompting and few-shot formatting to write professional social posts.
2.  **Outbound Email Generator:** Using Chain of Thought to write structured business emails mapping pain points to value propositions.
Reference code is provided in [14_Assignment_Solution.md](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day6_Prompt_Engineering/Day6_Teaching_content/14_Assignment_Solution.md).
