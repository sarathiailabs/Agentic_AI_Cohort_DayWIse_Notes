# 🎓 Day 5 Student Review & Session Recap: Generative AI & LLM APIs

Welcome to your student review and revision guide for **Day 5: Generative AI & LLM APIs**. 
Use this document to quickly recap the lecture concepts, copy starter code snippets, check common coding traps, and complete your career mentor assignment.

---

## 🎯 Session Overview

| Detail | Info |
| :--- | :--- |
| **Topic** | Generative AI & LLM APIs (AI vs ML, Tokens, Parameters, Temperature, multi-providers) |
| **Key SDKs** | `openai`, `google-generativeai`, `groq` |
| **Assignment** | Build an AI Career Mentor CLI tool with conversation memory and cost counters |
| **Reference Materials** | [Main Lecture](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day5_Generative_AI_and_LLM_APIs/Day5_Teaching_content/01_Main_Lecture.md) \| [Code Examples Notebook](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day5_Generative_AI_and_LLM_APIs/Day5_Teaching_content/07_Code_Examples.ipynb) \| [FAQs](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day5_Generative_AI_and_LLM_APIs/Day5_Teaching_content/12_FAQs.md) |

---

## 🧠 Core Concepts: Quick Revision

### 1. The AI Spectrum
Understanding the nesting of these four core fields is essential:
*   **Artificial Intelligence (AI):** The broad field of creating machines that can simulate human intelligence.
*   **Machine Learning (ML):** A subset of AI focused on algorithms that learn patterns from training data (e.g. Linear Regression, Random Forest).
*   **Deep Learning (DL):** A subset of ML utilizing multi-layer artificial neural networks (e.g. CNNs, Transformers) to process high-dimensional data.
*   **Generative AI (GenAI):** A specialized subset of DL focused on creating *new* content (text, code, images, audio) rather than classifying existing data.

```
┌────────────────────────────────────────────────────────┐
│ ARTIFICIAL INTELLIGENCE (AI)                           │
│  ┌──────────────────────────────────────────────────┐  │
│  │ MACHINE LEARNING (ML)                            │  │
│  │  ┌────────────────────────────────────────────┐  │  │
│  │  │ DEEP LEARNING (DL)                         │  │  │
│  │  │  ┌──────────────────────────────────────┐  │  │  │
│  │  │  │ GENERATIVE AI (GenAI)                │  │  │  │
│  │  │  └──────────────────────────────────────┘  │  │  │
│  │  └────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────┘
```

---

### 2. Large Language Models (LLMs) & Tokens
LLMs do not process words directly; they process text split into **tokens** (averaging 4 characters or 0.75 words).
*   **Next-Token Prediction:** LLMs are giant probability models. They calculate the probability distribution of all possible next tokens given your input context, and append the selected token to their context.
*   **Token Pricing:** API providers charge based on the number of input (prompt) and output (completion) tokens.

---

### 3. Key LLM Parameters

#### Context Window
The maximum number of tokens (input + output combined) a model can handle in a single API request. Exceeding this limit throws a rate/token exception.
> [!CAUTION]
> **Lost in the Middle:** Long contexts (e.g., 100k+ tokens) suffer from degradation where models fail to retrieve information located in the middle of long prompts.

#### Temperature
Controls the degree of randomness in selection.
*   `Temperature = 0.0` (Deterministic): The model always picks the highest-probability token. Essential for coding, math, and logical schemas.
*   `Temperature = 0.7` (Creative): The model chooses from lower-probability paths, providing varied, natural content suitable for copywriting.

#### Hallucinations
Since LLMs predict based on probability rather than checking databases, they can construct false facts with high linguistic confidence. Minimizing this requires factual constraints, grounding data, and a temperature of 0.

---

## 🛠️ API Providers Setup Cheatsheet

Install dependencies using `uv`:
```bash
uv pip install openai google-generativeai groq python-dotenv
```

### 1. OpenAI Integration
```python
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a direct, concise helper."},
        {"role": "user", "content": "Explain context windows."}
    ],
    temperature=0.2
)
print(response.choices[0].message.content)
```

### 2. Google Gemini Integration
```python
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain tokens in 1 sentence.")
print(response.text)
```

### 3. Groq (High-Speed Inference) Integration
```python
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[{"role": "user", "content": "Hello Llama3!"}],
    temperature=0
)
print(response.choices[0].message.content)
```

---

## 📋 Assignment Walkthrough: AI Career Mentor

Your assignment is to build a command-line **AI Career Mentor** for college students, implementing conversational memory, multi-provider switching (e.g. OpenAI vs Gemini), and analytics.

### Project Setup
```
day5_assignment/
├── requirements.txt
├── .env
├── .env.example
└── career_mentor.py
```

### Scaffold for `career_mentor.py`
Use this clean scaffolding to start implementing your solution. It manages memory and token tracking:

```python
import os
import sys
import json
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai as genai

# Load environment configuration
load_dotenv()

# Verify baseline keys
if not os.getenv("OPENAI_API_KEY") or not os.getenv("GEMINI_API_KEY"):
    print("Warning: Missing OPENAI_API_KEY or GEMINI_API_KEY in .env config.")

class CareerMentor:
    def __init__(self):
        self.provider = "openai"  # Current provider (openai / gemini)
        self.history = []        # Session conversation memory
        
        # System instructions constraining the AI profile
        self.system_prompt = """
        You are a senior tech career mentor at EduNext. 
        You specialize in guiding students toward roles in AI, Data Science, Web Dev, and Cloud.
        Your tone is professional, encouraging, and data-driven.
        Always suggest concrete tech stacks and reference real-world salaries.
        Ask clarifying questions about their background before issuing direct roadmap advice.
        """
        
        # Simple stats counters
        self.total_tokens_used = 0
        self.message_count = 0
        
    def switch_provider(self):
        if self.provider == "openai":
            self.provider = "gemini"
        else:
            self.provider = "openai"
        print(f"\n🔄 Switched provider to: {self.provider.upper()}")

    def get_openai_response(self, user_message: str) -> str:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        # Format messages combining system instructions + history + current input
        messages = [{"role": "system", "content": self.system_prompt}]
        for turn in self.history:
            messages.append(turn)
        messages.append({"role": "user", "content": user_message})
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.3
            )
            # Track approximate token metrics
            self.total_tokens_used += response.usage.total_tokens
            self.message_count += 2
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"OpenAI API Error: {str(e)}"

    def get_gemini_response(self, user_message: str) -> str:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=self.system_prompt
        )
        
        # Assemble chat session context
        chat = model.start_chat(history=[])
        # Send history as context
        # (For Gemini, simple string summation or direct chat history works. Here we pass the current input)
        try:
            response = chat.send_message(user_message)
            self.message_count += 2
            # Estimate token size (4 characters ~ 1 token)
            self.total_tokens_used += len(user_message + response.text) // 4
            return response.text.strip()
        except Exception as e:
            return f"Gemini API Error: {str(e)}"

    def ask_mentor(self, message: str) -> str:
        if self.provider == "openai":
            reply = self.get_openai_response(message)
        else:
            reply = self.get_gemini_response(message)
            
        # Append turns to history list
        self.history.append({"role": "user", "content": message})
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def save_session(self, filepath="exports/conversation.json"):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        data = {
            "stats": {"messages": self.message_count, "tokens": self.total_tokens_used},
            "history": self.history
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"✅ Session successfully saved to {filepath}")

def main():
    mentor = CareerMentor()
    print("🎓 Welcome to EduNext's AI Career Mentor CLI!")
    print("Commands: 'switch' (swap API), 'save' (write history), 'stats' (view costs), 'quit' (exit)\n")
    
    while True:
        user_input = input("\nYou: ").strip()
        if not user_input:
            continue
            
        if user_input.lower() == "quit":
            print("Exiting. Good luck with your studies!")
            break
        elif user_input.lower() == "switch":
            mentor.switch_provider()
            continue
        elif user_input.lower() == "save":
            mentor.save_session()
            continue
        elif user_input.lower() == "stats":
            cost = (mentor.total_tokens_used / 1000) * 0.0015
            print(f"\n📊 Session Statistics:")
            print(f"- Messages exchanged: {mentor.message_count}")
            print(f"- Approximate tokens: {mentor.total_tokens_used}")
            print(f"- Estimated session cost: ${cost:.5f}")
            continue
            
        # Standard query routing
        reply = mentor.ask_mentor(user_input)
        print(f"\nMentor: {reply}")

if __name__ == "__main__":
    main()
```

---

## ⚠️ Common Pitfalls to Avoid

1.  **Exposing API Keys in Git:** Never hardcode your API key strings. Storing your keys directly in `career_mentor.py` exposes them publicly. Always read keys from your environment using `dotenv` and double-check that your `.env` is listed in your `.gitignore`.
2.  **Omitting system_instruction on Gemini:** The Gemini SDK requires system prompts to be specified during the `GenerativeModel` constructor initialization. Passing it inside message history can confuse the attention boundaries.
3.  **Cost Blindness:** In production pipelines, failing to parse API response payloads to log exact token metrics can result in uncontrolled billing loops. Always inspect the `usage` metadata block in API response outputs.
4.  **Rate Limit Failures:** High-frequency prompt inputs will throw a `RateLimitError`. Build standard Python `try-except` wrappers around your network requests to capture exceptions gracefully.

---

## 💬 Interview Preparation Q&A

### Q1: What are tokens, and why can't LLMs directly process letters or raw string characters?
*   **Answer:** LLMs are mathematical vector prediction engines. They cannot process unstructured raw strings efficiently due to dimensionality constraints. Instead, texts are split into token sequences (sub-word character chunks). These tokens are mapped to high-dimensional embedding vectors that representing semantic meaning, allowing neural nodes to perform calculations.

### Q2: Why is setting `temperature=0` essential when outputting specific formatting, such as JSON schemas?
*   **Answer:** LLMs are auto-regressive probability models. At high temperatures (e.g. 0.8), the model selects randomly from a broader curve of possible next tokens. For syntax-critical structures like JSON, this randomness leads to missing brackets or illegal punctuation. Setting temperature to `0` makes token choices deterministic, selecting only the highest-probability keyword.

### Q3: What is a Context Window limit, and what occurs when a conversation exceeds it?
*   **Answer:** The context window is the absolute limit of tokens a model can process in a single request (sum of prompt tokens + completion tokens). When a session history grows too large and exceeds this limit, the provider API throws a runtime exception and rejects the call. Developers handle this by sliding/summarizing older memory turns.

Good luck completing your career mentor assignment! If you face issues, check the [FAQs](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day5_Generative_AI_and_LLM_APIs/Day5_Teaching_content/12_FAQs.md) and [Common Mistakes](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day5_Generative_AI_and_LLM_APIs/Day5_Teaching_content/11_Common_Mistakes.md) files in this directory.
