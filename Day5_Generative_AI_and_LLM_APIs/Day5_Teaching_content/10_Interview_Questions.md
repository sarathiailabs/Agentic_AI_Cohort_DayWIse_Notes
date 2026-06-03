# ❓ Day 5 – Interview Questions: Generative AI & LLM APIs

> 30 Questions across Beginner, Intermediate, and Advanced levels with detailed answers.

---

## 🟢 Beginner Questions (10)

### Q1: What is the difference between AI, ML, DL, and Generative AI?

**Answer:**

| Term | Definition | Example |
|------|-----------|---------|
| **AI** | Any system that mimics human intelligence | Calculator, Chess engine |
| **ML** | AI that learns from data without explicit programming | Spam filter, Netflix recommendations |
| **DL** | ML using deep neural networks with multiple layers | Face recognition, self-driving cars |
| **GenAI** | AI that creates new content (text, images, code) | ChatGPT, DALL-E, GitHub Copilot |

The relationship: GenAI ⊂ DL ⊂ ML ⊂ AI

**Key difference:** Traditional AI analyzes and classifies. Generative AI **creates** new content.

---

### Q2: What is an LLM? Give 3 examples.

**Answer:**
LLM stands for **Large Language Model** — a massive neural network trained on enormous amounts of text data that can understand and generate human language.

- **Large:** Billions of parameters (GPT-4 has ~1.8 trillion)
- **Language:** Processes and generates human language
- **Model:** A trained neural network

**Examples:**
1. **GPT-4o** (OpenAI)
2. **Claude 3.5** (Anthropic)
3. **Gemini 1.5** (Google)
4. **LLaMA 3** (Meta)
5. **Mistral** (Mistral AI)

---

### Q3: What is a token in the context of LLMs?

**Answer:**
A token is a piece of text that the LLM processes. It's not exactly a word or a character — it's something in between.

**Rules of thumb:**
- 1 token ≈ 4 characters in English
- 1 token ≈ ¾ of a word
- 100 tokens ≈ 75 words

**Example:**
```
"Hello world" → ["Hello", " world"] → 2 tokens
"ChatGPT" → ["Chat", "G", "PT"] → 3 tokens
```

**Why it matters:** You pay per token. Token count affects cost, speed, and context window usage.

---

### Q4: What is a Context Window?

**Answer:**
The context window is the **maximum number of tokens an LLM can process in a single request**, including the input (system prompt + all messages) and the output.

**Common sizes:**
- GPT-4o: 128,000 tokens (~300 pages)
- Claude 3.5: 200,000 tokens (~500 pages)
- Gemini 1.5 Pro: 2,000,000 tokens (~5,000 pages)

**What fits inside:**
```
System prompt + All conversation messages + Space for response = Must be ≤ Context Window
```

**When exceeded:** The model either truncates old messages or returns an error.

---

### Q5: What is Temperature in LLM APIs?

**Answer:**
Temperature controls the **randomness/creativity** of the LLM's output.

| Temperature | Behavior | Use Case |
|------------|----------|----------|
| 0.0 | Always same answer (deterministic) | Code, math, facts |
| 0.3 | Slight variation, mostly consistent | Customer support |
| 0.7 | Good balance of variety (default) | Content writing |
| 1.0 | High creativity, varied outputs | Brainstorming |
| >1.0 | Very random, potentially incoherent | Rarely used |

**Technical:** Temperature modifies the probability distribution of next-token predictions. Lower values sharpen the distribution (pick the most likely token). Higher values flatten it (more random selection).

---

### Q6: What is an API key and why is it important?

**Answer:**
An API key is a unique string that:
1. **Identifies** you to the API provider
2. **Authenticates** your requests
3. **Bills** usage to your account
4. **Rate limits** your requests

**Security rules:**
- ❌ Never commit API keys to GitHub
- ❌ Never share API keys publicly
- ✅ Use environment variables: `os.getenv("OPENAI_API_KEY")`
- ✅ Use `.env` files with `.gitignore`
- ✅ Rotate keys if compromised

---

### Q7: What is a hallucination in AI?

**Answer:**
A hallucination is when an LLM generates **information that sounds correct but is factually wrong, fabricated, or misleading**.

**Types:**
1. **Factual:** Wrong dates, statistics ("Python was created in 2005" — wrong, it was 1991)
2. **Citation:** Made-up research papers, fake URLs
3. **Logical:** Incorrect reasoning that sounds convincing
4. **Fabrication:** Entirely invented events or people

**Why it happens:** LLMs predict the most **probable** next token, not the most **true** next token. They have no built-in fact-checking mechanism.

**Famous case:** In 2023, a lawyer was fined $5,000 for submitting ChatGPT-generated fake court citations.

---

### Q8: What is the difference between OpenAI and open-source LLMs?

**Answer:**

| Feature | OpenAI (Closed) | Open-Source (LLaMA, Mistral) |
|---------|-----------------|------------------------------|
| Access | API only | Download and run locally |
| Cost | Pay per token | Free (but need compute) |
| Privacy | Data sent to cloud | Data stays local |
| Customization | Limited | Full fine-tuning possible |
| Quality | Generally higher | Catching up rapidly |
| Speed | Depends on servers | Depends on your hardware |

**Open-source examples:** Meta LLaMA 3, Mistral, Phi (Microsoft), Gemma (Google)

---

### Q9: What does the `messages` parameter look like in an LLM API call?

**Answer:**
```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "Python is a programming language..."},
    {"role": "user", "content": "Show me an example."}
]
```

**Three roles:**
- **system:** Instructions for the AI (personality, rules, constraints)
- **user:** The human's messages
- **assistant:** The AI's previous responses

The entire message list is sent with every API call. That's how the model "remembers" the conversation.

---

### Q10: Name 3 LLM API providers and their key strengths.

**Answer:**

| Provider | Key Strength | Best For |
|----------|-------------|----------|
| **OpenAI** | Highest quality models (GPT-4o) | Production apps needing best quality |
| **Google Gemini** | 2M context window, generous free tier | Long document processing, budget apps |
| **Groq** | Blazing fast (500+ tokens/sec) | Real-time apps, low latency needs |
| **Anthropic Claude** | Best reasoning, strong safety | Complex analysis, sensitive content |
| **Ollama** | 100% free, runs locally | Privacy-sensitive apps, learning |
| **HuggingFace** | Largest model hub (500K+ models) | Research, open-source exploration |

---

## 🟡 Intermediate Questions (10)

### Q11: Explain how the Transformer architecture works at a high level.

**Answer:**
The Transformer (introduced in 2017 paper "Attention Is All You Need") has these key components:

1. **Tokenizer:** Breaks text into tokens
2. **Embedding Layer:** Converts tokens to numerical vectors
3. **Positional Encoding:** Adds position information (word order matters)
4. **Self-Attention Mechanism:** Each token "attends" to all other tokens to understand relationships
5. **Feed-Forward Network:** Processes the attention output
6. **Multiple Layers:** Steps 4-5 repeat many times (GPT-4 has 96 layers)
7. **Output Layer:** Produces probability distribution over vocabulary

**Key innovation:** Self-attention allows the model to process all tokens in parallel (unlike RNNs which process sequentially), making training much faster.

---

### Q12: What is BPE tokenization and why is it used?

**Answer:**
**BPE (Byte Pair Encoding)** is the tokenization algorithm used by GPT models.

**How it works:**
1. Start with individual characters as the vocabulary
2. Find the most frequent pair of adjacent tokens
3. Merge them into a new token
4. Repeat until desired vocabulary size is reached

**Example:**
```
"lowest" → Initially: ['l', 'o', 'w', 'e', 's', 't']
After merging 'l'+'o' → ['lo', 'w', 'e', 's', 't']
After merging 'lo'+'w' → ['low', 'e', 's', 't']
After merging 'e'+'s' → ['low', 'es', 't']
After merging 'es'+'t' → ['low', 'est']
```

**Why BPE:** It handles rare/new words by breaking them into known subwords, avoiding the "unknown word" problem.

---

### Q13: How would you implement conversation memory management for a production chatbot?

**Answer:**
```python
def manage_context(conversation: list, max_tokens: int = 100000) -> list:
    """Keep conversation within context window limits."""
    
    # Strategy 1: Sliding window — keep last N messages
    if count_tokens(conversation) > max_tokens:
        # Always keep system prompt
        system_msg = conversation[0]
        
        # Summarize old messages
        old_messages = conversation[1:-10]  # All but last 10
        summary = summarize_messages(old_messages)
        
        # Reconstruct
        conversation = (
            [system_msg] + 
            [{"role": "system", "content": f"Previous conversation summary: {summary}"}] +
            conversation[-10:]  # Keep last 10 messages
        )
    
    return conversation
```

**Strategies:**
1. **Sliding Window:** Keep only the last N messages
2. **Summarization:** Summarize older messages and keep the summary
3. **Smart Truncation:** Remove the oldest user messages but keep important ones
4. **Hybrid:** Summarize older context + keep recent messages in full

---

### Q14: Compare the cost of running 1 million requests across different providers.

**Answer:**
Assuming 500 input tokens + 300 output tokens per request:

| Provider | Cost per Request | Cost for 1M Requests | Monthly (at 33K/day) |
|----------|-----------------|---------------------|---------------------|
| GPT-4o mini | $0.000255 | $255 | $255 |
| GPT-4o | $0.004250 | $4,250 | $4,250 |
| Gemini 1.5 Flash | $0.000128 | $128 | $128 |
| Claude 3.5 Sonnet | $0.006000 | $6,000 | $6,000 |
| Groq LLaMA 70B | $0.000532 | $532 | $532 |

**Key insight:** The difference between cheapest (Gemini Flash) and most expensive (Claude Sonnet) is ~47x. Provider selection dramatically impacts costs.

---

### Q15: What is RLHF and why is it important?

**Answer:**
**RLHF = Reinforcement Learning from Human Feedback**

It's the process that makes LLMs helpful, harmless, and honest (after pre-training).

**Steps:**
1. **Supervised Fine-Tuning (SFT):** Train on human-written example conversations
2. **Reward Model Training:** Humans rank multiple model outputs; train a reward model on these preferences
3. **PPO Training:** Use the reward model to fine-tune the LLM using reinforcement learning

**Why important:**
- Without RLHF, models give unhelpful, rambling, or dangerous responses
- RLHF is what makes ChatGPT "feel" helpful vs the raw GPT-3 model
- It's the difference between a pre-trained model and a chat model

---

### Q16: How would you handle rate limiting in a production AI application?

**Answer:**
```python
import time
from groq import Groq, RateLimitError

def call_with_backoff(client, messages, max_retries=5):
    """Exponential backoff for rate limits."""
    for attempt in range(max_retries):
        try:
            return client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages
            )
        except RateLimitError:
            wait = min(2 ** attempt, 60)  # Max 60 second wait
            print(f"Rate limited. Waiting {wait}s (attempt {attempt+1})")
            time.sleep(wait)
    raise Exception("Max retries exceeded")
```

**Strategies:**
1. **Exponential backoff:** Wait 1s, 2s, 4s, 8s...
2. **Token bucket:** Limit requests per second/minute
3. **Queue system:** Queue requests and process at provider's rate
4. **Multi-provider fallback:** Switch to backup provider on rate limit

---

### Q17: What is the difference between `max_tokens` and the context window?

**Answer:**

| Feature | `max_tokens` | Context Window |
|---------|-------------|----------------|
| **What** | Max output tokens for ONE response | Total capacity for input + output |
| **Controls** | How long the AI's response can be | How much the model can "see" |
| **Set by** | Developer (in API call) | Model architecture (fixed) |
| **Example** | `max_tokens=500` limits response to 500 tokens | GPT-4o: 128K total capacity |

**Relationship:**
```
Input tokens + max_tokens ≤ Context Window

If context window = 128,000 and input = 125,000:
   Max possible output = 3,000 tokens
```

---

### Q18: Explain the difference between streaming and non-streaming API responses.

**Answer:**

**Non-streaming (default):**
```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[...],
    stream=False  # Wait for complete response
)
# User waits 5 seconds... then gets everything at once
```

**Streaming:**
```python
stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[...],
    stream=True  # Get tokens as they're generated
)
for chunk in stream:
    print(chunk.choices[0].delta.content, end="")
    # User sees text appear word by word (like ChatGPT)
```

**When to use:**
- **Non-streaming:** Background tasks, batch processing, when latency isn't critical
- **Streaming:** User-facing chatbots, real-time interfaces (better perceived performance)

---

### Q19: How do you store API keys securely in a Python project?

**Answer:**
```python
# Method 1: Environment variables (BEST for production)
import os
api_key = os.getenv("OPENAI_API_KEY")

# Method 2: .env file with python-dotenv (good for development)
# .env file:
# OPENAI_API_KEY=sk-xxx
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Method 3: Config file (NOT in version control)
# config.yaml (add to .gitignore!)
```

**Security checklist:**
- ✅ Add `.env` to `.gitignore`
- ✅ Use environment variables in production
- ✅ Use secrets management (AWS Secrets Manager, Vault) in enterprise
- ❌ Never hardcode keys in source code
- ❌ Never commit keys to Git

---

### Q20: What are system prompts and how do they affect model behavior?

**Answer:**
System prompts are instructions sent with `role: "system"` that define the AI's behavior, personality, and constraints.

**Impact on behavior:**
```python
# Without system prompt — Generic, unfocused responses
messages = [{"role": "user", "content": "Tell me about Python"}]

# With system prompt — Focused, role-specific responses
messages = [
    {"role": "system", "content": "You are a senior Python developer at Google. "
     "Give concise, production-quality advice. Use code examples."},
    {"role": "user", "content": "Tell me about Python"}
]
```

**Best practices:**
1. Be specific about the role/persona
2. Define response format (bullet points, code, etc.)
3. Set constraints (what NOT to do)
4. Include examples of ideal responses
5. Keep it concise (long system prompts waste tokens)

---

## 🔴 Advanced Questions (10)

### Q21: Explain the self-attention mechanism in Transformers.

**Answer:**
Self-attention computes how much each token should "attend to" every other token in the sequence.

**Steps:**
1. For each token, compute three vectors: **Query (Q)**, **Key (K)**, **Value (V)**
2. Compute attention scores: `score = Q · K^T / √d_k`
3. Apply softmax to get weights
4. Multiply weights by Values to get output

**Example:**
```
"The cat sat on the mat because it was tired"

For token "it":
  Attention to "cat":  0.72 (strongest — "it" refers to "the cat")
  Attention to "mat":  0.15
  Attention to "sat":  0.08
  Attention to others: 0.05
```

**Multi-Head Attention:** Run multiple attention computations in parallel (different "heads" learn different relationships — syntactic, semantic, positional).

---

### Q22: How would you implement a multi-provider fallback system?

**Answer:**
```python
class MultiProviderLLM:
    def __init__(self):
        self.providers = [
            {"name": "groq", "client": Groq(api_key="..."), "model": "llama-3.3-70b-versatile"},
            {"name": "openai", "client": OpenAI(api_key="..."), "model": "gpt-4o-mini"},
            {"name": "gemini", "client": None, "model": "gemini-1.5-flash"},
        ]
    
    def chat(self, messages, max_retries=2):
        for provider in self.providers:
            for attempt in range(max_retries):
                try:
                    if provider["name"] == "gemini":
                        return self._call_gemini(messages)
                    else:
                        response = provider["client"].chat.completions.create(
                            model=provider["model"],
                            messages=messages
                        )
                        return response.choices[0].message.content
                except Exception as e:
                    print(f"Provider {provider['name']} failed: {e}")
                    time.sleep(2 ** attempt)
            print(f"All retries failed for {provider['name']}, trying next...")
        raise Exception("All providers failed")
```

---

### Q23: What is the difference between fine-tuning and RAG? When would you use each?

**Answer:**

| Feature | Fine-Tuning | RAG |
|---------|------------|-----|
| **What** | Retrain the model on your data | Retrieve relevant documents + feed to model |
| **Changes model?** | Yes — modifies weights | No — model stays the same |
| **Cost** | High ($100–$10K+) | Low (just API costs + vector DB) |
| **Data freshness** | Static (retrain needed) | Dynamic (update documents anytime) |
| **Best for** | Changing model behavior/style | Adding knowledge/facts |
| **Example** | Make model write in company tone | Answer questions from company docs |

**When to use:**
- **Fine-tuning:** When you need to change HOW the model responds (style, format, domain expertise)
- **RAG:** When you need to change WHAT the model knows (company data, recent information)
- **Both:** For enterprise production systems

---

### Q24: How do LLMs handle multilingual text? What are the implications?

**Answer:**
LLMs tokenize non-English text less efficiently because their tokenizers are primarily trained on English data.

**Implications:**
```
English: "Hello, how are you?" → 6 tokens
Hindi:   "नमस्ते, आप कैसे हैं?" → 18 tokens (3x more!)
Japanese: "こんにちは、お元気ですか？" → 12 tokens (2x more!)
```

**Impact:**
1. **Cost:** Non-English conversations cost 2-3x more per message
2. **Speed:** More tokens = slower processing
3. **Context:** Non-English text fills the context window faster
4. **Quality:** Models perform best in English; quality may degrade in other languages

**Solutions:**
- Use models specifically trained for target languages
- Use multilingual models (Gemini, GPT-4o are strong multilingual)
- Consider local models fine-tuned for specific languages

---

### Q25: Design a production architecture for an AI customer support system.

**Answer:**
```
                    ┌───────────────────────────────────────┐
                    │          LOAD BALANCER                 │
                    └──────────────┬────────────────────────┘
                                   │
                    ┌──────────────▼────────────────────────┐
                    │          API GATEWAY                    │
                    │  (Auth, Rate Limiting, Logging)        │
                    └──────────────┬────────────────────────┘
                                   │
          ┌────────────────────────┼────────────────────────┐
          │                        │                         │
   ┌──────▼──────┐     ┌──────────▼──────────┐    ┌────────▼────────┐
   │  ROUTER     │     │  CONTEXT ENGINE      │    │  SAFETY FILTER  │
   │  (Intent    │     │  (RAG: retrieve      │    │  (Toxicity,     │
   │   detection)│     │   relevant docs)     │    │   PII removal)  │
   └──────┬──────┘     └──────────┬──────────┘    └────────┬────────┘
          │                        │                         │
          └────────────────────────┼─────────────────────────┘
                                   │
                    ┌──────────────▼────────────────────────┐
                    │          LLM ORCHESTRATOR               │
                    │  (Primary: GPT-4o, Fallback: Claude)   │
                    └──────────────┬────────────────────────┘
                                   │
                    ┌──────────────▼────────────────────────┐
                    │  POST-PROCESSING                       │
                    │  (Hallucination check, format,         │
                    │   escalation rules)                    │
                    └──────────────┬────────────────────────┘
                                   │
                    ┌──────────────▼────────────────────────┐
                    │  RESPONSE + ANALYTICS                   │
                    │  (Log to DB, track satisfaction)        │
                    └───────────────────────────────────────┘
```

---

### Q26: What are the security risks of LLM APIs and how do you mitigate them?

**Answer:**

| Risk | Description | Mitigation |
|------|------------|------------|
| **Prompt Injection** | User manipulates the system prompt | Input validation, output filtering |
| **Data Leakage** | Model reveals training data or system prompt | Don't put secrets in prompts |
| **API Key Exposure** | Keys leaked in code/logs | Environment variables, secrets management |
| **PII in Prompts** | Sensitive data sent to cloud APIs | PII scrubbing before API calls |
| **Jailbreaking** | User bypasses safety guardrails | Multiple safety layers, monitoring |
| **Denial of Service** | Excessive API calls | Rate limiting, authentication |

---

### Q27: How does temperature mathematically affect token probabilities?

**Answer:**
Temperature divides the logits (raw model outputs) before applying softmax:

```
P(token_i) = exp(logit_i / T) / Σ exp(logit_j / T)

Where T = temperature

When T → 0: argmax (always picks highest probability)
When T = 1: Standard softmax (original distribution)
When T > 1: Flatter distribution (more random)
```

**Example with logits [2.0, 1.0, 0.5]:**

| Temperature | P(token1) | P(token2) | P(token3) |
|------------|-----------|-----------|-----------|
| 0.1 | 0.9999 | 0.0001 | 0.0000 |
| 0.5 | 0.8756 | 0.1065 | 0.0179 |
| 1.0 | 0.5065 | 0.3072 | 0.1863 |
| 2.0 | 0.3908 | 0.3268 | 0.2824 |

---

### Q28: Explain the trade-offs between using Ollama locally vs cloud APIs.

**Answer:**

| Factor | Ollama (Local) | Cloud APIs |
|--------|---------------|------------|
| **Cost** | Free (electricity only) | Pay per token |
| **Privacy** | 100% private | Data sent to provider |
| **Speed** | Depends on GPU | Consistently fast |
| **Model Size** | Limited by VRAM (7B-70B) | Access to largest models |
| **Quality** | Good (open-source models) | Best (GPT-4o, Claude) |
| **Reliability** | Depends on your hardware | 99.9%+ uptime |
| **Maintenance** | You manage everything | Provider handles everything |
| **Scaling** | Limited to one machine | Auto-scales |

**Use local when:** Privacy is critical, experimenting, no budget, offline needed
**Use cloud when:** Quality is critical, need to scale, production deployment

---

### Q29: How would you evaluate and compare LLM outputs for quality?

**Answer:**

**Automated metrics:**
1. **BLEU score:** Compare generated text to reference text (word overlap)
2. **ROUGE score:** Recall-based metric for summarization
3. **Perplexity:** How "surprised" the model is by the text (lower = better)
4. **BERTScore:** Semantic similarity using embeddings

**Human evaluation:**
1. **Relevance:** Does the answer address the question?
2. **Accuracy:** Are facts correct?
3. **Helpfulness:** Is the response useful?
4. **Coherence:** Is the text logically structured?
5. **Safety:** Is the response harmful or biased?

**LLM-as-Judge:**
```python
# Use one LLM to evaluate another's output
evaluation_prompt = f"""
Rate this response on a scale of 1-10 for:
1. Accuracy
2. Helpfulness  
3. Clarity

Question: {question}
Response: {response}
"""
```

---

### Q30: Design a token-efficient prompt for a customer support chatbot handling 100K messages/day.

**Answer:**
```python
# INEFFICIENT (wastes tokens) — 250 tokens for system prompt
system_prompt_bad = """
You are a helpful customer support agent for TechCorp. TechCorp is a technology
company that sells software products. You have been trained to help customers
with their questions about products, billing, technical issues, and general
inquiries. You should always be polite, professional, and helpful. When you
don't know the answer, you should tell the customer that you'll escalate their
issue to a human agent. Please provide clear and concise responses...
[... continues for 250 tokens ...]
"""

# EFFICIENT (same behavior) — 80 tokens
system_prompt_good = """You are TechCorp's support agent.
Rules: Be concise. Use bullet points. If unsure, escalate to human.
Scope: Products, billing, technical issues.
Format: Acknowledge → Solution → Next steps.
Tone: Professional, friendly."""

# Savings per day:
# Bad: 250 tokens × 100K msgs = 25M extra tokens/day
# At $0.15/1M tokens = $3.75/day wasted = $112/month saved!
```

**Token optimization strategies:**
1. Minimize system prompt length
2. Summarize conversation history (don't send full history)
3. Use shorter model names and parameters
4. Batch similar requests
5. Cache common responses
6. Use smaller models for simple queries (GPT-4o mini vs GPT-4o)
