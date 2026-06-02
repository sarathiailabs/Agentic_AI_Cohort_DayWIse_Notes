# 📅 Day 5 – Generative AI & LLM APIs

## 🎯 Session Overview

| Detail           | Info                                    |
| ---------------- | --------------------------------------- |
| **Day**          | 5 of 20                                 |
| **Topic**        | Generative AI & LLM APIs               |
| **Duration**     | 2 Hours                                 |
| **Level**        | Beginner to Intermediate                |
| **Prerequisites**| Python Fundamentals (Day 1–3), Git (Day 4) |

### 🎯 Learning Objectives

By the end of this session, students will:

1. ✅ Understand the difference between AI, ML, DL, and Generative AI
2. ✅ Know what an LLM is and how it works internally
3. ✅ Understand Tokens, Context Windows, Temperature, and Hallucinations
4. ✅ Know how to use APIs from OpenAI, Gemini, Claude, Groq, HuggingFace, and Ollama
5. ✅ Build a working AI Chatbot using LLM APIs
6. ✅ Build an AI Career Mentor as an industry project

---

# 📚 Topic 1: AI vs ML vs DL vs GenAI

## 🔴 Problem — What Problem Existed Before?

Before AI, every software system was **rule-based**. If you wanted a spam filter, you had to write 500+ rules manually:

```
if "free money" in email → spam
if "lottery winner" in email → spam
if "click here now" in email → spam
...
```

**The Problem?**
- Spammers changed one word and your rules broke
- You needed a human to update rules every week
- It didn't scale — 1000 new spam patterns every day
- It couldn't learn from mistakes

Companies like **Gmail** were drowning in spam. Manual rules couldn't keep up.

**What if** the computer could **learn** from examples instead of following rules?

That's exactly what **Machine Learning** solved. And then **Deep Learning** made it even smarter. And then **Generative AI** made machines creative.

---

## 📖 Story — The Netflix Recommendation Journey

**2005 — Netflix DVD Era (Rule-Based)**

Netflix used simple rules: "If user watched Action Movie A, recommend Action Movie B."

Result? Terrible recommendations. Users got bored.

**2006 — Netflix Prize (Machine Learning)**

Netflix offered $1 million to anyone who could improve recommendations by 10%. Teams used ML algorithms that **learned** from user watching patterns.

Result? Way better! But still couldn't understand WHY users liked certain movies.

**2016 — Deep Learning Era**

Netflix started using deep neural networks that could analyze:
- Watch history
- Time of day
- Device used
- How long you paused
- What you skipped

Result? Netflix saves **$1 billion/year** from better recommendations.

**2023 — Generative AI Era**

Netflix now uses GenAI to:
- Generate personalized thumbnails for each user
- Create personalized show descriptions
- Generate trailer variations
- Write marketing copy

**The evolution: Rules → ML → Deep Learning → Generative AI**

---

## 🟢 Beginner Explanation

Think of it like learning to cook:

| Level            | Cooking Analogy                                      | Tech Equivalent      |
| ---------------- | ---------------------------------------------------- | -------------------- |
| **AI**           | Any machine that does something "smart"              | Calculator, Alexa    |
| **ML**           | Learning recipes from examples (not written rules)   | Spam filter, Netflix |
| **DL**           | A master chef who understands flavors deeply          | Self-driving cars    |
| **GenAI**        | A chef who **invents new recipes** never seen before  | ChatGPT, DALL-E      |

### Simple Way to Remember:

```
AI    = Machine acts smart
ML    = Machine learns from data
DL    = Machine learns deeply (like a brain)
GenAI = Machine creates new things
```

### The Subset Relationship:

```
┌──────────────────────────────────────────────┐
│              ARTIFICIAL INTELLIGENCE          │
│    ┌────────────────────────────────────┐     │
│    │         MACHINE LEARNING           │     │
│    │    ┌──────────────────────────┐    │     │
│    │    │      DEEP LEARNING       │    │     │
│    │    │   ┌──────────────────┐   │    │     │
│    │    │   │  GENERATIVE AI   │   │    │     │
│    │    │   └──────────────────┘   │    │     │
│    │    └──────────────────────────┘    │     │
│    └────────────────────────────────────┘     │
└──────────────────────────────────────────────┘
```

GenAI ⊂ DL ⊂ ML ⊂ AI

---

## 🔵 Technical Explanation

### Artificial Intelligence (AI)
- **Definition**: Any system that mimics human intelligence
- **Approach**: Rule-based OR learning-based
- **Examples**: Chess engines (1997), Siri, Alexa
- **Key**: Doesn't necessarily learn — can be hardcoded rules

### Machine Learning (ML)
- **Definition**: Algorithms that learn patterns from data without being explicitly programmed
- **Approach**: Statistical learning from labeled/unlabeled data
- **Types**: Supervised, Unsupervised, Reinforcement Learning
- **Examples**: Email spam detection, loan approval, fraud detection
- **Key Algorithms**: Linear Regression, Decision Trees, Random Forest, SVM

### Deep Learning (DL)
- **Definition**: ML using artificial neural networks with multiple layers
- **Approach**: Learns hierarchical features automatically
- **Architecture**: Neural networks with 3+ hidden layers
- **Examples**: Image recognition, speech recognition, self-driving cars
- **Key**: Requires massive data + GPU compute

### Generative AI (GenAI)
- **Definition**: AI that creates NEW content (text, images, code, audio, video)
- **Approach**: Learned patterns used to GENERATE, not just classify
- **Architecture**: Transformers, Diffusion Models, GANs
- **Examples**: ChatGPT, DALL-E, Midjourney, GitHub Copilot, Suno AI
- **Key**: Doesn't just analyze — it CREATES

### The Critical Difference:

```
Traditional AI:  Input → Analysis → Classification/Prediction
Generative AI:   Input → Understanding → NEW CONTENT CREATION

Example:
Traditional: "Is this email spam?" → Yes/No
Generative:  "Write me an email about..." → Complete new email
```

---

## 🌍 Real World Examples

### Example 1: Google Search vs ChatGPT
- **Google (Traditional AI/ML)**: Takes your query → Finds matching web pages → Returns links
- **ChatGPT (GenAI)**: Takes your query → Understands it → Generates a complete answer

### Example 2: Amazon Product Recommendations
- **ML Phase**: "People who bought X also bought Y" (pattern matching)
- **GenAI Phase**: Generates personalized product descriptions and marketing copy

### Example 3: Uber Route Optimization
- **ML**: Predicts demand, surge pricing, ETA calculation
- **GenAI**: Could generate natural language ride summaries, driver feedback analysis

### Example 4: Swiggy/Zomato
- **ML**: Restaurant recommendations, delivery time prediction
- **GenAI**: AI-generated menu descriptions, review summaries, chatbot support

### Example 5: GitHub Copilot
- **Before (Traditional)**: Autocomplete suggested variable names
- **GenAI (Copilot)**: Writes entire functions, understands context, generates tests

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    AI LANDSCAPE                              │
├──────────────┬──────────────┬───────────────┬───────────────┤
│  RULE-BASED  │   ML         │  DEEP LEARNING│ GENERATIVE AI │
│  AI          │              │               │               │
├──────────────┼──────────────┼───────────────┼───────────────┤
│ If-Else      │ Learn from   │ Neural        │ Create new    │
│ Rules        │ data         │ Networks      │ content       │
├──────────────┼──────────────┼───────────────┼───────────────┤
│ Chess Engine │ Spam Filter  │ Image Recog.  │ ChatGPT       │
│ Expert       │ Netflix Recs │ Self-driving  │ DALL-E        │
│ Systems      │ Fraud Det.   │ Voice Assist  │ Copilot       │
├──────────────┼──────────────┼───────────────┼───────────────┤
│ 1950s-1990s  │ 2000s-2010s  │ 2012-2020     │ 2022-Present  │
└──────────────┴──────────────┴───────────────┴───────────────┘
```

---

## 🎤 Teaching Script

**Instructor says:**

> "Before we start — quick question. How many of you have used ChatGPT this week?"
> *(Wait for hands)*
>
> "Great! Now, how many of you know what's actually happening behind the scenes when you type a message and get a response?"
> *(Fewer hands)*
>
> "That's exactly what we'll learn today. By the end of this session, you won't just USE AI — you'll BUILD with it."
>
> "Let's start with a simple question: What's the difference between AI and Machine Learning? Are they the same thing?"
> *(Let students answer — expected: 'ML is part of AI' or confusion)*
>
> "Think of it like vehicles. AI is the general concept — like 'vehicles.' ML is a specific type — like 'cars.' Deep Learning is like 'electric cars.' And Generative AI is like 'self-driving electric cars.' Each one is more specific and more powerful."

**Discussion Point:**
> "Can anyone give me an example of AI that is NOT Machine Learning?"
> Expected: Calculator, basic chatbot with rules, thermostat
> Follow-up: "Exactly! A thermostat is AI — it makes decisions. But it doesn't LEARN from data."

---

---

# 📚 Topic 2: What is an LLM?

## 🔴 Problem

Before LLMs, building a chatbot meant:

```python
# Old way — Rule-based chatbot (2015)
if "hello" in user_input:
    return "Hi there!"
elif "weather" in user_input:
    return "I don't know the weather."
elif "help" in user_input:
    return "How can I help?"
else:
    return "I don't understand."
```

**Problems:**
- You had to predict EVERY possible user input
- The chatbot couldn't handle new questions
- No understanding of context or meaning
- Adding new capabilities meant writing MORE rules
- Couldn't handle different languages
- Couldn't generate creative responses

**What if** there was a single model that could understand ANY text and generate intelligent responses?

That's what **Large Language Models (LLMs)** are.

---

## 📖 Story — The ChatGPT Moment

**November 30, 2022** — OpenAI released ChatGPT.

Within **5 days**, it had **1 million users** (Instagram took 2.5 months for the same).

Why? Because for the first time:
- You could ask ANY question in natural language
- It understood context from previous messages
- It could write code, essays, poems, emails
- It felt like talking to a knowledgeable human

**Behind ChatGPT** was GPT-3.5 — a Large Language Model trained on billions of text documents from the internet.

Companies that had spent years building rule-based chatbots suddenly realized: one LLM replaced thousands of rules.

---

## 🟢 Beginner Explanation

**An LLM is like a super-intelligent autocomplete.**

When you type on your phone and it suggests the next word? That's a tiny language model.

```
You type: "Good ___"
Phone suggests: "morning" / "evening" / "night"
```

Now imagine that, but:
- Trained on the entire internet
- Understands context of full conversations
- Can write paragraphs, not just one word
- Has billions of parameters (knowledge connections)

That's an LLM.

### Simple Definition:
> **LLM = A massive neural network trained on enormous amounts of text data that can understand and generate human language.**

### Key Characteristics:

| Feature          | Details                                  |
| ---------------- | ---------------------------------------- |
| **Large**        | Billions of parameters (GPT-4: ~1.8T)   |
| **Language**     | Understands and generates human language |
| **Model**        | A trained neural network                 |

---

## 🔵 Technical Explanation

### Architecture: The Transformer

LLMs are built on the **Transformer architecture** (introduced in the 2017 paper "Attention Is All You Need" by Google).

```
                    ┌─────────────────────────┐
                    │     OUTPUT LAYER         │
                    │  (Next Token Prediction) │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │    DECODER LAYERS        │
                    │  (96 layers in GPT-4)    │
                    │                          │
                    │  ┌────────────────────┐  │
                    │  │ Self-Attention      │  │
                    │  │ (Understanding      │  │
                    │  │  relationships)     │  │
                    │  └────────────────────┘  │
                    │  ┌────────────────────┐  │
                    │  │ Feed-Forward        │  │
                    │  │ (Processing)        │  │
                    │  └────────────────────┘  │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │    EMBEDDING LAYER       │
                    │  (Words → Numbers)       │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │    TOKENIZER             │
                    │  (Text → Tokens)         │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │    INPUT TEXT             │
                    │  "What is Python?"        │
                    └─────────────────────────┘
```

### How LLMs Are Built:

**Step 1: Data Collection**
- Billions of web pages, books, code repositories, Wikipedia

**Step 2: Tokenization**
- Break text into tokens (words/subwords)

**Step 3: Pre-training**
- Train the model to predict the next token
- Requires 1000s of GPUs, months of training, millions of dollars

**Step 4: Fine-tuning (RLHF)**
- Human feedback to make responses helpful, harmless, honest
- Reinforcement Learning from Human Feedback

**Step 5: Deployment**
- Serve via API for developers

### Popular LLMs:

| Model         | Company    | Parameters | Release  |
| ------------- | ---------- | ---------- | -------- |
| GPT-4o        | OpenAI     | ~1.8T      | 2024     |
| Claude 3.5    | Anthropic  | Undisclosed| 2024     |
| Gemini 1.5    | Google     | Undisclosed| 2024     |
| LLaMA 3       | Meta       | 8B–405B    | 2024     |
| Mistral       | Mistral AI | 7B–8x22B  | 2024     |

---

## 🌍 Real World Examples

1. **ChatGPT** — Conversational AI (100M+ users)
2. **GitHub Copilot** — Code generation (1.3M+ paying users)
3. **Jasper AI** — Marketing content generation ($80M revenue)
4. **Grammarly** — Writing assistance powered by LLMs
5. **Perplexity AI** — AI-powered search engine

---

---

# 📚 Topic 3: How LLMs Work

## 🔴 Problem

> "How does ChatGPT know what to say? Is it searching the internet? Does it have a database of answers?"

**Common Misconceptions:**
- ❌ LLMs search Google for answers
- ❌ LLMs store a database of Q&A pairs
- ❌ LLMs truly "understand" language like humans
- ❌ LLMs remember your previous conversations forever

**Reality:** LLMs are sophisticated **next-token prediction machines**.

---

## 📖 Story — The World's Best Autocomplete

Imagine you've read every book ever written, every Wikipedia page, every website, every code repository.

Now someone says: "The capital of France is ___"

You'd instantly say "Paris" because you've seen that pattern thousands of times.

That's exactly what an LLM does — but at a massive scale with mathematical precision.

---

## 🟢 Beginner Explanation

### LLMs work in 3 simple steps:

**Step 1: Read the input (your prompt)**
```
You: "Write a poem about coding"
```

**Step 2: Predict the next word, one at a time**
```
"In"  → probability 0.15
"Code" → probability 0.22  ← highest!
"The"  → probability 0.12
```

**Step 3: Keep predicting until done**
```
"Code" → "flows" → "like" → "a" → "river" → "through" → "the" → "night" → ...
```

### It's like filling in blanks:
```
"The cat sat on the ___"  → "mat" (most likely)
"Python is a ___ language" → "programming" (most likely)
"To be or not to ___"     → "be" (most likely)
```

**Key Insight:** The LLM doesn't "know" things. It calculates the most probable next word based on patterns it learned during training.

---

## 🔵 Technical Explanation

### The Next-Token Prediction Process:

```
Input: "What is machine"

Step 1: Tokenize
["What", "is", "machine"] → [2061, 374, 5780]

Step 2: Embedding
[2061, 374, 5780] → [[0.12, -0.34, ...], [0.56, 0.78, ...], [0.91, -0.23, ...]]

Step 3: Self-Attention (96 layers)
Each token attends to all other tokens
"machine" pays attention to "What" and "is" to understand context

Step 4: Output Probability Distribution
{
    "learning": 0.85,
    "vision": 0.05,
    "translation": 0.03,
    "intelligence": 0.02,
    ...other words: 0.05
}

Step 5: Select token
Selected: "learning" (highest probability)

Step 6: Repeat from Step 1 with "What is machine learning"
```

### Self-Attention Mechanism:

```
Sentence: "The cat sat on the mat because it was tired"

What does "it" refer to?
Self-attention calculates:
  "it" → "cat"  : attention score 0.72  ← strongest connection
  "it" → "mat"  : attention score 0.15
  "it" → "sat"  : attention score 0.08
  "it" → others : attention score 0.05

The model learns that "it" refers to "the cat"
```

### Training Process:

```
┌─────────────────────────────────────────────┐
│         LLM TRAINING PIPELINE                │
├─────────────────────────────────────────────┤
│                                              │
│  1. DATA COLLECTION                          │
│     └── Internet, Books, Code, Wikipedia     │
│         (Trillions of tokens)                │
│                                              │
│  2. PRE-TRAINING                             │
│     └── Next-token prediction                │
│     └── 1000s of GPUs                        │
│     └── Months of training                   │
│     └── Cost: $10M - $100M+                  │
│                                              │
│  3. SUPERVISED FINE-TUNING (SFT)             │
│     └── Human-written examples               │
│     └── Q&A pairs, Instructions              │
│                                              │
│  4. RLHF (Reinforcement Learning)            │
│     └── Human ranks model outputs            │
│     └── Model learns to be helpful           │
│                                              │
│  5. DEPLOYMENT                               │
│     └── API serving                          │
│     └── Safety filters                       │
│                                              │
└─────────────────────────────────────────────┘
```

---

---

# 📚 Topic 4: Tokens

## 🔴 Problem

When you use ChatGPT or any LLM API:
- You're charged **per token**, not per word
- Your input has a **token limit**
- Longer inputs = more expensive

But what IS a token?

---

## 📖 Story

**Amazon's Cost Shock:**

A startup built a customer support chatbot using GPT-4. They expected $500/month in API costs.

First month's bill? **$15,000!**

Why? They were sending entire customer history (5000 words) with every message. That's ~7,500 tokens per request × 10,000 requests/day = 75M tokens/month.

**Lesson:** Understanding tokens = understanding your AI costs.

---

## 🟢 Beginner Explanation

**Tokens are pieces of words.** Not exactly words, not exactly characters — something in between.

```
"Hello world"    → ["Hello", " world"]           → 2 tokens
"ChatGPT"        → ["Chat", "G", "PT"]           → 3 tokens
"I'm happy"      → ["I", "'m", " happy"]         → 3 tokens
"Tokenization"   → ["Token", "ization"]           → 2 tokens
```

### Rule of Thumb:
- **1 token ≈ 4 characters** in English
- **1 token ≈ ¾ of a word**
- **100 tokens ≈ 75 words**
- **1 page of text ≈ 400-500 tokens**

### Why not just use words?

```
"unhappiness" → If we used whole words, every new word needs its own entry
                 With tokens: ["un", "happiness"] → Reuse "un" for "unhappy", "undo", "unfair"
```

**Tokens let the model handle ANY word, even ones it hasn't seen, by breaking them into familiar pieces.**

---

## 🔵 Technical Explanation

### Tokenization Algorithms:

**BPE (Byte Pair Encoding)** — Used by GPT models
1. Start with individual characters
2. Find most frequent pair, merge them
3. Repeat until vocabulary size reached

```
Training corpus: "low lower lowest"

Iteration 1: Most frequent pair = ('l', 'o') → merge to 'lo'
Iteration 2: Most frequent pair = ('lo', 'w') → merge to 'low'
Iteration 3: Most frequent pair = ('e', 'r') → merge to 'er'
...
```

### Token Pricing (as of 2024):

| Model         | Input (per 1M tokens) | Output (per 1M tokens) |
| ------------- | --------------------- | ---------------------- |
| GPT-4o        | $2.50                 | $10.00                 |
| GPT-4o mini   | $0.15                 | $0.60                  |
| Claude 3.5    | $3.00                 | $15.00                 |
| Gemini 1.5 Pro| $1.25                 | $5.00                  |
| Groq (LLaMA)  | $0.05                 | $0.08                  |

---

## 🌍 Real World Examples

1. **OpenAI** charges per token — understanding tokenization saves companies thousands
2. **Google Translate** uses subword tokenization to handle 100+ languages
3. **GitHub Copilot** tokenizes code differently than natural language
4. **Grammarly** uses token-efficient prompts to keep costs low
5. **Stripe** optimizes token usage in their fraud detection LLM system

---

---

# 📚 Topic 5: Context Window

## 🔴 Problem

You're chatting with ChatGPT about a complex project. After 30 messages, it suddenly "forgets" what you said at the beginning.

Why? Because every LLM has a **Context Window** — a maximum number of tokens it can process at once.

---

## 📖 Story — The Exam Hall Analogy

Imagine you're in an exam hall with a small desk. You can only keep 10 pages on your desk at a time.

If someone gives you 50 pages of notes and asks a question about page 3 — you can't answer because page 3 fell off your desk long ago.

**Context Window = Your desk size.**

- GPT-3.5 desk = 4,096 tokens (~3 pages)
- GPT-4 desk = 128,000 tokens (~300 pages)
- Gemini 1.5 Pro desk = 2,000,000 tokens (~5,000 pages!) — You could read an entire textbook!

---

## 🟢 Beginner Explanation

```
Context Window = Maximum memory of the LLM during one conversation

┌─────────────────────────────────────────┐
│           CONTEXT WINDOW (128K)         │
│                                          │
│  ┌──────────┐  ┌──────────────────────┐ │
│  │ System    │  │ Conversation History │ │
│  │ Prompt    │  │ (All messages)       │ │
│  │           │  │                      │ │
│  │ ~500      │  │ ~100,000 tokens      │ │
│  │ tokens    │  │                      │ │
│  └──────────┘  └──────────────────────┘ │
│                                          │
│  ┌──────────────────────────────────┐   │
│  │ Space for Response (~27,500)     │   │
│  └──────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

### Context Window Sizes:

| Model           | Context Window   | Equivalent          |
| --------------- | ---------------- | ------------------- |
| GPT-3.5 Turbo   | 16,385 tokens    | ~25 pages           |
| GPT-4o          | 128,000 tokens   | ~300 pages          |
| Claude 3.5      | 200,000 tokens   | ~500 pages          |
| Gemini 1.5 Pro  | 2,000,000 tokens | ~5,000 pages        |

---

## 🔵 Technical Explanation

The context window includes EVERYTHING sent to the model:

```python
# Everything inside the context window:
messages = [
    {"role": "system", "content": "You are a helpful assistant..."},  # ~100 tokens
    {"role": "user", "content": "First question..."},                  # ~50 tokens
    {"role": "assistant", "content": "First answer..."},               # ~200 tokens
    {"role": "user", "content": "Follow-up question..."},              # ~30 tokens
    # ... all previous messages ...
    {"role": "user", "content": "Latest question..."},                 # ~50 tokens
]
# Total: System + All messages must fit in context window
# PLUS: Space needed for the model's response
```

### Why it matters:

```
If context window = 128,000 tokens:
  - System prompt:       500 tokens
  - Conversation so far: 120,000 tokens
  - Remaining for response: 7,500 tokens
  
If you send 130,000 tokens → ERROR! Exceeds context window.
```

---

---

# 📚 Topic 6: Temperature

## 🔴 Problem

Ask ChatGPT "What is 2+2?" ten times — you always get "4."

Ask "Write a poem about love" ten times — you get 10 different poems!

Why? **Temperature** controls how creative or deterministic the LLM is.

---

## 📖 Story — The Chef Analogy

**Temperature 0 (Focused Chef):**
"Make me pasta" → Always makes spaghetti with tomato sauce. Same dish. Every time. Reliable.

**Temperature 0.7 (Creative Chef):**
"Make me pasta" → Sometimes spaghetti, sometimes penne, maybe adds mushrooms, tries new spices. Usually good, occasionally surprising.

**Temperature 1.0+ (Experimental Chef):**
"Make me pasta" → Might put chocolate on pasta. Could be genius. Could be terrible. Very unpredictable.

---

## 🟢 Beginner Explanation

```
Temperature = Creativity dial for the LLM

    🎯 Focused                           🎨 Creative
    ◄────────────────────────────────────────►
    0.0        0.3        0.7        1.0    2.0

    │          │          │          │       │
    Exact      Safe       Balanced   Random  Chaos
    Same       Slight     Good mix   Wild    Nonsense
    answer     variety                       
```

### When to Use What:

| Temperature | Use Case                    | Example                        |
| ----------- | --------------------------- | ------------------------------ |
| **0.0**     | Facts, Math, Code          | "What is the capital of India?" |
| **0.3**     | Customer Support, Q&A      | Chatbot responses               |
| **0.7**     | Creative writing, Content  | Blog posts, marketing copy      |
| **1.0**     | Brainstorming, Poetry      | "Give me wild startup ideas"    |

---

## 🔵 Technical Explanation

Temperature modifies the probability distribution of the next token:

```
Prompt: "The sky is ___"

Without temperature (raw logits):
  "blue":     0.60
  "clear":    0.20
  "gray":     0.10
  "beautiful": 0.05
  "falling":  0.05

Temperature = 0.0 (argmax):
  Always picks "blue" (highest probability)

Temperature = 0.7:
  "blue":     0.70  (boosted)
  "clear":    0.18
  "gray":     0.08
  "beautiful": 0.03
  "falling":  0.01

Temperature = 1.5:
  "blue":     0.35  (flattened)
  "clear":    0.22
  "gray":     0.18
  "beautiful": 0.13
  "falling":  0.12
```

### Formula:
```
P(token) = softmax(logits / temperature)

Low temperature → Sharper distribution → More deterministic
High temperature → Flatter distribution → More random
```

---

---

# 📚 Topic 7: Hallucinations

## 🔴 Problem

> "Hey ChatGPT, who won the 2028 Olympics?"
> ChatGPT: "The 2028 Olympics were held in Los Angeles. The USA topped the medal tally with 142 medals..."

**The 2028 Olympics haven't happened yet!** But the model confidently generated a detailed, completely fabricated answer.

This is a **hallucination** — when an LLM generates information that sounds correct but is factually wrong.

---

## 📖 Story — The Lawyer Who Got Caught

In 2023, a New York lawyer used ChatGPT to prepare a legal brief. ChatGPT cited several court cases to support the argument.

**Problem?** The cases were completely made up. They didn't exist.

The lawyer submitted the brief to court. The judge checked. The cases were fake.

**Result:** The lawyer was fined $5,000 and publicly sanctioned.

**Lesson:** Never blindly trust LLM output. Always verify.

---

## 🟢 Beginner Explanation

**Why do LLMs hallucinate?**

Remember: LLMs predict the **most probable** next word. They don't "know" facts — they predict what **sounds right**.

```
LLM thinking process:
"The book 'The Great Gatsby' was written by ___"
→ "F. Scott Fitzgerald" (correct! Pattern learned from training data)

"The book 'The Azure Chronicles' was written by ___"
→ "James Patterson" (WRONG! The book doesn't exist, but the pattern
   "book was written by [famous author]" is strong)
```

**It's like a confident student who makes up answers instead of saying "I don't know."**

### Types of Hallucinations:

| Type                | Example                                           |
| ------------------- | ------------------------------------------------- |
| **Factual**         | Wrong dates, fake statistics                      |
| **Citation**        | Made-up research papers, fake URLs                |
| **Logical**         | Incorrect reasoning that sounds logical           |
| **Fabrication**     | Entirely invented events, people, or products     |

---

## 🔵 Technical Explanation

### Why Hallucinations Happen:

1. **Training Data Gaps**: Model fills gaps with plausible-sounding content
2. **Probability Over Truth**: Model optimizes for "likely next token" not "true next token"
3. **No Verification Layer**: No built-in fact-checking mechanism
4. **Conflicting Data**: Model trained on contradictory information
5. **Outdated Knowledge**: Training data has a cutoff date

### Mitigation Strategies:

```
1. RAG (Retrieval Augmented Generation)
   → Ground responses in real documents

2. Temperature = 0
   → Reduce randomness for factual queries

3. System Prompt Instructions
   → "Only answer based on provided context. Say 'I don't know' if unsure."

4. Human Review
   → Always verify critical information

5. Structured Output
   → Force model to cite sources
```

---

---

# 📚 Topic 8: API Providers

## 🔴 Problem

You want to build an AI application. But training your own LLM costs **$10M–$100M+** and takes months.

**Solution:** Use pre-trained LLMs via APIs! Just send a request, get a response. Pay per token.

---

## 📖 Story

In 2022, if you wanted AI in your app:
- Option A: Train your own model ($10M+, 6 months, team of ML engineers)
- Option B: Use OpenAI's API ($0.002 per 1K tokens, 5 minutes to set up)

Every startup chose Option B. OpenAI's API revenue went from $0 to **$2B+ ARR** in under 2 years.

Now there are many providers, each with different strengths, pricing, and models.

---

## 🟢 Beginner Explanation

Think of LLM API providers like cloud services:
- You don't build your own server — you use AWS
- You don't train your own model — you use OpenAI/Gemini/Claude APIs

```
Your App                    API Provider
┌──────────┐    HTTP     ┌──────────────┐
│          │  ──────►    │              │
│  Python  │  Request    │  LLM Model   │
│  Code    │             │  (GPT-4,     │
│          │  ◄──────    │   Gemini,    │
│          │  Response   │   Claude)    │
└──────────┘             └──────────────┘
```

---

## 🔵 API Provider Deep Dive

### 1. OpenAI (GPT Models)

```python
# Installation: pip install openai
from openai import OpenAI

client = OpenAI(api_key="your-api-key")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Python?"}
    ],
    temperature=0.7,
    max_tokens=500
)

print(response.choices[0].message.content)
```

**Strengths:** Best overall quality, huge ecosystem, GPT-4o is state-of-the-art
**Pricing:** GPT-4o mini: $0.15/$0.60 per 1M input/output tokens

---

### 2. Google Gemini

```python
# Installation: pip install google-generativeai
import google.generativeai as genai

genai.configure(api_key="your-api-key")
model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("What is Python?")
print(response.text)
```

**Strengths:** Massive 2M context window, multimodal, generous free tier
**Pricing:** Gemini 1.5 Flash: Free tier available, then $0.075/$0.30 per 1M tokens

---

### 3. Anthropic Claude

```python
# Installation: pip install anthropic
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "What is Python?"}
    ]
)

print(message.content[0].text)
```

**Strengths:** Best for long context (200K), very safe, excellent reasoning
**Pricing:** Claude 3.5 Sonnet: $3/$15 per 1M tokens

---

### 4. Groq (Ultra-Fast Inference)

```python
# Installation: pip install groq
from groq import Groq

client = Groq(api_key="your-api-key")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "What is Python?"}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
```

**Strengths:** Blazing fast (500+ tokens/sec), cheap, runs open-source models
**Pricing:** LLaMA 3.3 70B: $0.59/$0.79 per 1M tokens

---

### 5. HuggingFace

```python
# Installation: pip install huggingface_hub
from huggingface_hub import InferenceClient

client = InferenceClient(api_key="your-api-key")

response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct",
    messages=[
        {"role": "user", "content": "What is Python?"}
    ],
    max_tokens=500
)

print(response.choices[0].message.content)
```

**Strengths:** Largest model hub (500K+ models), open-source focus, community
**Pricing:** Pay-per-use or free tier for many models

---

### 6. Ollama (Run Locally)

```python
# First: Install Ollama from ollama.ai
# Then: ollama pull llama3.2
# Then: ollama serve

import requests

response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "llama3.2",
        "messages": [
            {"role": "user", "content": "What is Python?"}
        ],
        "stream": False
    }
)

print(response.json()["message"]["content"])
```

**Strengths:** 100% free, runs locally, no API key needed, privacy
**Requirements:** Good GPU (8GB+ VRAM) for larger models

---

### Provider Comparison Table:

```
┌──────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
│   Provider   │  Best For    │    Speed     │    Cost      │   Privacy    │
├──────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
│   OpenAI     │ Quality      │ Medium       │ Medium       │ Cloud        │
│   Gemini     │ Context Size │ Fast         │ Cheap/Free   │ Cloud        │
│   Claude     │ Reasoning    │ Medium       │ Expensive    │ Cloud        │
│   Groq       │ Speed        │ Ultra Fast   │ Cheap        │ Cloud        │
│   HuggingFace│ Open Source  │ Varies       │ Free/Cheap   │ Cloud/Local  │
│   Ollama     │ Privacy      │ Depends GPU  │ Free         │ 100% Local   │
└──────────────┴──────────────┴──────────────┴──────────────┴──────────────┘
```

---

---

# 📚 Topic 9: Building AI Applications Using LLM APIs

## 🔴 Problem

You now know what LLMs are, how they work, and how to call APIs. But how do you build a **real AI application**?

---

## 📖 Story

A startup founder asks you: "Build me an AI chatbot for our EdTech platform that helps students choose their career path."

You need to:
1. Choose the right API provider
2. Design the system prompt
3. Handle conversation flow
4. Manage token costs
5. Handle errors gracefully
6. Make it production-ready

---

## 🟢 Application Architecture

```
┌─────────────────────────────────────────────────────┐
│                 AI APPLICATION                       │
│                                                      │
│  ┌──────────┐     ┌──────────────┐    ┌──────────┐  │
│  │  User     │────►│  Application │───►│  LLM     │  │
│  │  Input    │     │  Logic       │    │  API     │  │
│  │          │◄────│  (Python)    │◄───│  (Cloud) │  │
│  │  Terminal │     │              │    │          │  │
│  │  or Web   │     │  - Prompt    │    │  OpenAI  │  │
│  │           │     │  - History   │    │  Gemini  │  │
│  │           │     │  - Error     │    │  Claude  │  │
│  │           │     │    Handling  │    │  Groq    │  │
│  └──────────┘     └──────────────┘    └──────────┘  │
│                                                      │
└─────────────────────────────────────────────────────┘
```

## 🔵 Building Blocks of an AI App

### 1. System Prompt Design

```python
system_prompt = """
You are an AI Career Mentor for an EdTech platform.

Your role:
- Help students explore career paths in technology
- Provide actionable advice based on their skills and interests
- Suggest learning resources and roadmaps
- Be encouraging but realistic

Rules:
- Always ask clarifying questions before giving advice
- Provide specific, actionable steps
- Mention real companies and job roles
- If unsure, say "I'm not sure, but here's what I'd suggest..."
"""
```

### 2. Conversation Management

```python
conversation_history = [
    {"role": "system", "content": system_prompt}
]

def chat(user_message):
    conversation_history.append({"role": "user", "content": user_message})
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history,
        temperature=0.7
    )
    
    assistant_message = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": assistant_message})
    
    return assistant_message
```

### 3. Error Handling

```python
import time

def safe_chat(user_message, max_retries=3):
    for attempt in range(max_retries):
        try:
            return chat(user_message)
        except openai.RateLimitError:
            wait_time = 2 ** attempt
            print(f"Rate limited. Waiting {wait_time}s...")
            time.sleep(wait_time)
        except openai.APIError as e:
            print(f"API Error: {e}")
            if attempt == max_retries - 1:
                return "Sorry, I'm having trouble connecting. Please try again."
    return "Service temporarily unavailable."
```

---

## 🎤 Session Closing Script

**Instructor says:**

> "Today we went from zero to building AI applications. Let me recap what you now know:
>
> 1. AI vs ML vs DL vs GenAI — You understand the evolution
> 2. LLMs — You know what they are and how they work
> 3. Tokens — You understand the currency of AI
> 4. Context Window — You know the memory limits
> 5. Temperature — You can control creativity
> 6. Hallucinations — You know the dangers and mitigations
> 7. API Providers — You can call 6 different LLM APIs
> 8. Building Apps — You built a working AI chatbot!
>
> Tomorrow in Day 6, we'll learn Prompt Engineering — how to make these LLMs do exactly what you want with carefully crafted prompts."

---

# 🎯 Session Summary

| Topic                      | Key Takeaway                                           |
| -------------------------- | ------------------------------------------------------ |
| AI vs ML vs DL vs GenAI    | GenAI creates new content, others analyze/classify     |
| LLMs                       | Massive neural networks trained on text data            |
| How LLMs Work              | Next-token prediction using Transformer architecture    |
| Tokens                     | Pieces of words; you pay per token                     |
| Context Window             | Max memory during conversation                          |
| Temperature                | Creativity dial (0=focused, 1=creative)                |
| Hallucinations             | LLMs can generate confident but wrong information       |
| API Providers              | OpenAI, Gemini, Claude, Groq, HuggingFace, Ollama     |
| Building AI Apps           | System prompt + conversation loop + error handling      |
