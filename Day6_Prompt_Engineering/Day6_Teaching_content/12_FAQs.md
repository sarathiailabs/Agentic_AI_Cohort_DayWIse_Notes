# 📜 Day 6 – FAQs: Prompt Engineering

This document lists the 20 most common student questions regarding Prompt Engineering with detailed answers.

---

### Q1: What is the optimal number of few-shot examples to include in a prompt?
*   **Answer:** Typically, **3 to 5 examples** are sufficient to teach a model a style or pattern. Adding more examples increases input token costs and latency without yielding significant gains in accuracy (diminishing returns).

### Q2: Will few-shot examples permanently train the LLM?
*   **Answer:** No. Few-shot examples are processed "in-context" within the model's active attention window for that single API transaction. Once the call completes, the model retains no memory of the examples.

### Q3: Why does "Let's think step-by-step" help LLMs solve logic puzzles?
*   **Answer:** LLMs calculate the probability of the next word. When forced to output only the final answer, they must predict that answer in a single forward pass. By writing "Let's think step-by-step", they output their reasoning steps first, storing calculations in the context window to guide the final token generation.

### Q4: Should I use XML/HTML tags as delimiters or just markdown headings?
*   **Answer:** Modern LLMs (especially Claude and GPT-4) are highly trained on XML structure. Using tags like `<context>` and `</context>` or `<review>` is extremely effective because it completely isolates inputs from instructions, preventing prompt injection.

### Q5: Is Prompt Engineering a temporary skill that will disappear?
*   **Answer:** No. Even as models improve, structured communication, context specification, and output formatting constraints will always be required to build reliable software pipelines around probabilistic LLM engines.

### Q6: What is the difference between Few-Shot prompting and RAG (Retrieval-Augmented Generation)?
*   **Answer:** Few-shot prompting provides static examples of how to do a task. RAG fetches dynamic external facts (like database records or PDF search chunks) and injects them into the prompt to provide the LLM with grounded information to answer user queries.

### Q7: Can I use different API providers with the same prompt template?
*   **Answer:** Yes, but different models respond differently to prompts. A template optimized for OpenAI might fail on Gemini. You should test and tweak instruction weights when switching providers.

### Q8: What does "Lost in the Middle" mean?
*   **Answer:** Research shows that LLMs are best at retrieving information at the very beginning and very end of their input context. Information in the middle is often ignored. Always place critical rules and inputs at the edges of your prompts.

### Q9: How does system instructions differ from role prompting?
*   **Answer:** System instructions are metadata commands built into the API (e.g. system messages in ChatCompletions) that define the LLM's behavioral rules. Role prompting is the specific text inside the prompt telling the model who to pretend to be.

### Q10: Why should I set temperature=0 for coding and math?
*   **Answer:** A temperature of 0 forces the model to select the highest-probability token at each step, making the output deterministic and eliminating random syntax variations that lead to code bugs.

### Q11: What is Prompt Injection?
*   **Answer:** It is a security vulnerability where user-submitted data overrides the developer's system instructions, forcing the model to perform unauthorized actions or leak system details.

### Q12: How do I write a prompt to generate valid JSON?
*   **Answer:** Instruct the model to return *only* the JSON block, provide a clear few-shot schema example, set `temperature=0`, use delimiters, and parse the output. If the API supports it, enable native `response_format={"type": "json_object"}`.

### Q13: Does punctuation matter in prompt engineering?
*   **Answer:** Yes. Clear punctuation, bullet points, line breaks, and capitalization make it easier for the attention mechanism to parse instructions from variables.

### Q14: How does few-shot prompting affect latency?
*   **Answer:** Few-shot prompting increases the input token size. While LLMs process input tokens in parallel (pre-fill phase), a massive input prompt still adds slight latency compared to a zero-shot query.

### Q15: Can I prompt a model to be 100% accurate?
*   **Answer:** No. LLMs are probabilistic neural networks that predict the next token based on training statistics. You can minimize hallucinations using grounding data, CoT, and temperature tuning, but you cannot guarantee 100% accuracy.

### Q16: What is the "System Prompt" in OpenAI's API?
*   **Answer:** It is the first dictionary in the `messages` array, with `{"role": "system", "content": "..."}`. It serves as the baseline operating system instruction for the entire conversation.

### Q17: What is DSPy?
*   **Answer:** DSPy is a programming framework that automatically compiles and optimizes prompts based on a small training dataset, treating prompts as trainable parameters.

### Q18: Why did the model ignore my negative constraint ("Do NOT use emojis")?
*   **Answer:** LLMs pay attention to nouns. Seeing "emojis" increases its attention weight. Instead, write positive constraints: "Write exclusively in plain text. Avoid all emojis."

### Q19: How do I handle token usage costs during prototyping?
*   **Answer:** Start with cheaper models (like GPT-3.5-Turbo, Gemini Flash, or Groq) during prompt development. Once the prompt works, test and evaluate it on larger models if higher accuracy is needed.

### Q20: Can LLMs learn new facts from few-shot prompting?
*   **Answer:** Yes, but only temporarily within that specific conversation turn. The model does not write these facts to its permanent weights. This is called in-context learning.
