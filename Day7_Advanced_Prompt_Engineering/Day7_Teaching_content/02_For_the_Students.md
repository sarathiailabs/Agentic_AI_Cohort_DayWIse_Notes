# 🎓 Day 7 Student Review & Session Recap: Advanced Prompt Engineering

Welcome to your study and review guide for **Day 7: Advanced Prompt Engineering**! 
This document contains key concepts, code templates, common pitfalls, and interview preparation questions to help you review the concepts covered in our session.

---

## 🎯 Session Overview

| Detail | Info |
| :--- | :--- |
| **Topic** | Advanced Prompt Engineering (System Prompts, Structured Outputs, JSON mode, Function Calling, Evaluation) |
| **Core API** | Gemini API & OpenAI SDK compatibility |
| **Assignment** | Build a Command-Line Resume Analyzer |
| **Reference Materials** | [Instructor Complete Guide](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day7_Advanced_Prompt_Engineering/Day7_Teaching_content/01_Complete_Guide.md) \| [Coding Notebook](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day7_Advanced_Prompt_Engineering/Day7_Teaching_content/03_Coding_Notebook.ipynb) \| [Assignment Solution](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day7_Advanced_Prompt_Engineering/Day7_Teaching_content/05_Assignment_Solution.ipynb) |

---

## 🧠 Core Concepts: Quick Revision

### 1. System Prompts (Instructions)
- **What**: Global constraints passed outside the conversation history to configure model persona and boundaries.
- **Why**: Helps separate code (instructions) from data (user inputs), which dramatically reduces the chance of prompt injection.

### 2. Structured Outputs & JSON Mode
- **JSON Mode**: Forces the LLM to output a valid JSON string (otherwise it throws an error). It does not guarantee the *keys* match your schema.
- **Schema Enforcement**: Pass a JSON Schema or Pydantic model. The API uses logit masking (constrained decoding) so that the LLM *physically cannot* generate a token that violates your structure.

### 3. Function Calling (Tool Calling)
- **The Protocol**: A structured way to let the LLM connect to external systems. 
- **Important**: The LLM **does not run your code**. It only reads the schemas of your functions and outputs: *"Please run function X with parameters Y"*. Your local Python runtime executes the function and sends the result back to the model.

### 4. Prompt Evaluation
- Programmatically running test cases on your prompts to prevent regression (ensuring edits to fix a bug do not break other outputs).
- Uses simple validation checks, semantic distance, or a larger model acting as a grader (**LLM-as-a-Judge**).

---

## 🛠️ Code Cheatsheet & Setup

### Package Installation (Using `uv`)
```bash
uv pip install google-generativeai pydantic python-dotenv
```

### 1. Structured Outputs with Pydantic (Gemini API)
```python
import os
from pydantic import BaseModel, Field
from google import generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Step 1: Define the schema contract using Pydantic
class TicketDetails(BaseModel):
    category: str = Field(description="One of: billing, technical, sales")
    priority: str = Field(description="low, medium, or high")
    summary: str = Field(description="A 5-word summary of the ticket issue")

# Step 2: Request model with schema constraints
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(
    "My database crashed and the app won't boot up!",
    generation_config=genai.types.GenerationConfig(
        response_mime_type="application/json",
        response_schema=TicketDetails
    )
)
print("Valid JSON Output:", response.text)
```

### 2. Function Calling Example (Gemini API)
```python
import os
from google import generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Step 1: Define local Python function with clean typings & docstrings
def search_product_inventory(sku: str) -> str:
    """Queries the stock level for a product given its SKU.
    
    Args:
        sku: The unique product identifier string (e.g. 'PROD-101').
    """
    db = {"PROD-101": "12 items in warehouse A", "PROD-102": "Out of stock"}
    return db.get(sku, "SKU not found in database")

# Step 2: Register tools and start chat with automatic function calling enabled
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    tools=[search_product_inventory]
)

chat = model.start_chat(enable_automatic_function_calling=True)
response = chat.send_message("Is product PROD-101 available?")
print("Answer:", response.text)
```

---

## ⚠️ Common Pitfalls to Avoid

1. **Missing Parameter Descriptions**: If your functions lack docstrings or type hints, the LLM will guess the parameters and make mistakes. Always add detailed explanations to function inputs.
2. **Infinite Loops**: In custom function-calling loops, always set a `max_iterations = 5` counter. If the model gets stuck calling tools, this stops it from burning your API credits.
3. **Regexing Markdown Ticks**: Never use `response.text.replace('```json', '')`. Instruct the model using the API's `response_mime_type="application/json"` or use Pydantic validation directly.
4. **Trusting Model Output Directly**: Never execute raw code or SQL queries generated by the LLM in your production database. Always parameterize queries.

---

## 💬 Interview Preparation Q&A

### Q1: What is constrained decoding and how does it relate to Structured Outputs?
*   **Answer**: Constrained decoding is a decoding-level technique where the grammar parser (JSON Schema) masks the probabilities of the model's vocabulary at each token prediction step. The model is forced to only select tokens that comply with the JSON syntax structure, ensuring 100% syntactically correct JSON outputs from the LLM.

### Q2: What are the security risks associated with Function Calling, and how do we mitigate them?
*   **Answer**: The primary risk is Remote Code Execution (RCE) or SQL injection if the LLM generates parameters that are directly evaluated in a shell or database. We mitigate this by validating parameters using Pydantic, executing tools in sandbox environments, utilizing parameterized DB drivers, and enforcing strict user access controls (least privilege).
