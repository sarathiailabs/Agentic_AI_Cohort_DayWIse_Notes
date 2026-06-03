# 🎬 Day 6 – Live Demonstrations: Prompt Engineering

This document contains executable code examples and demo scripts to run live during the class.

---

## Setup & Environment

Ensure you have a `.env` file in your workspace containing your OpenAI API Key:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

Activate the virtual environment and install packages:
```bash
uv pip install openai python-dotenv
```

---

## Demo 1: Zero-Shot vs. Few-Shot Sentiment Classification

This demo showcases how a zero-shot prompt fails on custom taxonomy or specific formatting rules, and how a few-shot prompt corrects it immediately.

### Code Setup (`demo_few_shot.py`)
```python
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. Zero-Shot Prompt
zero_shot_prompt = """
Classify the sentiment of the following customer feedback. 
Feedback: "The delivery arrived late, but the customer support representative refunded my delivery fee immediately."
Sentiment:
"""

# 2. Few-Shot Prompt (Using custom tags)
few_shot_prompt = """
Classify customer feedback into one of these tags: [SUPPORT-EXCELLENT], [DELIVERY-DELAY], [PRODUCT-DEFECT], [BILLING-ISSUE].

Feedback: "My package was left in the rain and the box was soaked."
Tag: [DELIVERY-DELAY]

Feedback: "They billed my card twice for the subscription."
Tag: [BILLING-ISSUE]

Feedback: "The screen has a visible scratch right out of the box."
Tag: [PRODUCT-DEFECT]

Feedback: "The delivery arrived late, but the customer support representative refunded my delivery fee immediately."
Tag:
"""

def test_prompts():
    print("--- Running Zero-Shot Sentiment Tagger ---")
    response_zs = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": zero_shot_prompt}],
        temperature=0
    )
    print("Response:\n", response_zs.choices[0].message.content.strip())
    print("\n" + "="*50 + "\n")
    
    print("--- Running Few-Shot Sentiment Tagger ---")
    response_fs = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": few_shot_prompt}],
        temperature=0
    )
    print("Response:\n", response_fs.choices[0].message.content.strip())

if __name__ == "__main__":
    test_prompts()
```

### Instructor Verification Checkpoints:
*   Show that the zero-shot response outputs sentence-style explanations (e.g., "Mixed sentiment: Negative for delivery, positive for support").
*   Show that the few-shot response outputs exactly `[DELIVERY-DELAY]` or `[SUPPORT-EXCELLENT]`, matching the target custom tag formatting perfectly.

---

## Demo 2: Chain of Thought (CoT) Reasoning Test

This demo shows how an LLM fails a logic puzzle when asked to answer immediately (zero-shot), and how it solves it when prompted to write out its reasoning steps (CoT).

### Code Setup (`demo_cot.py`)
```python
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

puzzle = """
A farmer has 15 sheep. All but 8 die. How many sheep are left alive?
"""

# 1. Standard Prompt
standard_prompt = f"{puzzle} Answer with only the final number."

# 2. Chain of Thought Prompt
cot_prompt = f"{puzzle} Let's think step-by-step to find the answer. Explain your math steps before outputting the final number."

def run_demos():
    print("--- Standard Prompt (No Reasoning) ---")
    response_std = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": standard_prompt}],
        temperature=0
    )
    print("Output:", response_std.choices[0].message.content.strip())
    print("\n" + "="*50 + "\n")
    
    print("--- Chain of Thought Prompt ---")
    response_cot = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": cot_prompt}],
        temperature=0
    )
    print("Output:\n", response_cot.choices[0].message.content.strip())

if __name__ == "__main__":
    run_demos()
```

### Instructor Verification Checkpoints:
*   The puzzle "All but 8 die" means exactly 8 are left.
*   Many standard zero-shot model completions outputs `7` (subtracting 8 from 15 because they rush to calculate subtraction).
*   The CoT model outputs the correct answer `8` by reasoning through the literal meaning of the phrase "All but 8 die."
