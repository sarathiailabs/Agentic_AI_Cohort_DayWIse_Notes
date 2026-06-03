# 📜 Day 6 – Common Mistakes: Prompt Engineering

This document lists the top 15 prompt engineering mistakes, why they happen, and how to avoid them in production.

---

## 1. Vague Instructions ("Be Creative")
*   **Why it happens:** Developers treat the LLM like a human and use subjective instructions (e.g. "make the post sound cool" or "write a smart email").
*   **How to avoid it:** Define concrete metrics. Instead of "make it punchy," write "Use short sentences (under 15 words), write in the active voice, and limit paragraphs to 3 sentences maximum."

---

## 2. Poor or Vague Few-Shot Examples
*   **Why it happens:** Injecting poor, inconsistent, or syntactically broken few-shot examples into the prompt context.
*   **How to avoid it:** Ensure every few-shot example is clean, follows the exact schema you want, and has been tested for consistency.

---

## 3. High Temperature on Structural Outputs (JSON/YAML)
*   **Why it happens:** Setting temperature to 0.7 or above when generating structured code or JSON, leading to random syntax errors.
*   **How to avoid it:** Set `temperature=0` for any task requiring logical accuracy, JSON formatting, or math calculation.

---

## 4. Prompt Starvation (Missing Input Context)
*   **Why it happens:** You ask the model to generate content without providing enough raw data (e.g. "write an email about our product" without explaining what the product does).
*   **How to avoid it:** Inject comprehensive reference data under headings like `CONTEXT:` or `PRODUCT_SPECS:` inside your prompt template.

---

## 5. Hardcoding Variables in Prompt Strings
*   **Why it happens:** Writing prompts as single, hardcoded strings, making it impossible to scale or dynamically update values.
*   **How to avoid it:** Use Python string formatting templates or orchestration models to load and compile prompts dynamically.

---

## 6. Over-Promoting with Too Many Rules
*   **Why it happens:** Writing a massive, 2000-word prompt containing 50 conflicting rules. The model gets confused and starts ignoring constraints (instruction drift).
*   **How to avoid it:** Keep rules focused. If a task requires too many constraints, split it into a multi-stage pipeline (e.g., Stage 1: Generate Draft, Stage 2: Audit & Format).

---

## 7. Ignoring Token Limits of Prompt Context
*   **Why it happens:** Appending massive few-shot examples without checking the model's input token boundaries, leading to truncated messages.
*   **How to avoid it:** Count tokens programmatically using packages like `tiktoken` before firing the API call.

---

## 8. Storing API Keys Directly in the Prompt or Script
*   **Why it happens:** Hardcoding `api_key = "sk-..."` directly inside the script or prompt file.
*   **How to avoid it:** Use `dotenv` and call `os.getenv("OPENAI_API_KEY")`. Never commit `.env` files to git.

---

## 9. Lack of Clear Delimiters
*   **Why it happens:** Blending user input text with system instructions, allowing the model to confuse user text for instructions (prompt injection).
*   **How to avoid it:** Wrap user inputs in clear delimiters like triple backticks (```) or XML tags (e.g., `<user_review>{review}</user_review>`).

---

## 10. Assuming the Model Knows the Current Year
*   **Why it happens:** Prompts like "Write news about today" fail because the model's training cutoff has passed.
*   **How to avoid it:** Dynamically inject the current system date and time into the prompt context at runtime.

---

## 11. Overpaying for Token Volume using CoT unnecessarily
*   **Why it happens:** Using Chain of Thought prompting for simple, deterministic classification tasks where the model already has 99% accuracy.
*   **How to avoid it:** Only use CoT for complex reasoning, math, and multi-step logic. Use Zero-Shot or simple Few-Shot for standard classification.

---

## 12. Negative Constraints ("Do Not Write About X")
*   **Why it happens:** LLMs struggle to process negative constraints (e.g., "Do not write about politics" often makes the model write about politics due to semantic attention weight).
*   **How to avoid it:** Rephrase instructions positively. Instead of "Do not use passive voice," write "Write exclusively in the active voice."

---

## 13. Not Handling Parsing Exceptions on Structured Code
*   **Why it happens:** Assuming the LLM will always output valid JSON or markdown, leading to runtime failures when a bracket is missing.
*   **How to avoid it:** Wrap JSON decoding or regex parsing in `try-except` blocks with solid fallbacks.

---

## 14. Placing Crucial Instructions in the Middle ("Lost in the Middle")
*   **Why it happens:** Placing formatting rules or critical variables in the middle of a long text prompt, causing the LLM to skip them.
*   **How to avoid it:** Put core instructions and constraints at the very beginning or the very end of the prompt context.

---

## 15. Ignoring Model Version Drift
*   **Why it happens:** Designing a prompt template optimized for `gpt-3.5-turbo-0613` that breaks when the provider updates the model version.
*   **How to avoid it:** Version-control your prompt templates and continuously test them against new model releases.
