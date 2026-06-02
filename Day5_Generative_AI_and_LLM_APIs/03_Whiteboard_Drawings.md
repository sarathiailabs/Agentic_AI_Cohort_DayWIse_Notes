# 🖊️ Day 5 – Whiteboard Drawings: Generative AI & LLM APIs

> These diagrams are designed for live whiteboard teaching. Draw them step-by-step while explaining concepts.

---

## Drawing 1: AI ⊃ ML ⊃ DL ⊃ GenAI (Nested Circles)

### When to Draw: Start of Topic 1 (0:05)

```
Step 1: Draw outer circle
┌──────────────────────────────────────────────────┐
│                                                   │
│                ARTIFICIAL INTELLIGENCE            │
│                                                   │
│    Examples: Calculator, Chess Engine, Siri        │
│    Key: Machine acts smart                         │
│                                                   │
└──────────────────────────────────────────────────┘

Step 2: Add ML circle inside
┌──────────────────────────────────────────────────┐
│              ARTIFICIAL INTELLIGENCE              │
│                                                   │
│    ┌──────────────────────────────────────┐       │
│    │         MACHINE LEARNING             │       │
│    │                                      │       │
│    │   Examples: Spam Filter, Netflix     │       │
│    │   Key: Machine LEARNS from data      │       │
│    │                                      │       │
│    └──────────────────────────────────────┘       │
│                                                   │
└──────────────────────────────────────────────────┘

Step 3: Add DL circle inside ML
┌──────────────────────────────────────────────────┐
│              ARTIFICIAL INTELLIGENCE              │
│    ┌──────────────────────────────────────┐       │
│    │         MACHINE LEARNING             │       │
│    │    ┌────────────────────────────┐    │       │
│    │    │       DEEP LEARNING        │    │       │
│    │    │                            │    │       │
│    │    │  Examples: Face ID, Alexa  │    │       │
│    │    │  Key: Neural Networks      │    │       │
│    │    │                            │    │       │
│    │    └────────────────────────────┘    │       │
│    └──────────────────────────────────────┘       │
└──────────────────────────────────────────────────┘

Step 4: Add GenAI circle inside DL
┌──────────────────────────────────────────────────┐
│              ARTIFICIAL INTELLIGENCE              │
│    ┌──────────────────────────────────────┐       │
│    │         MACHINE LEARNING             │       │
│    │    ┌────────────────────────────┐    │       │
│    │    │       DEEP LEARNING        │    │       │
│    │    │   ┌────────────────────┐   │    │       │
│    │    │   │   GENERATIVE AI    │   │    │       │
│    │    │   │                    │   │    │       │
│    │    │   │  ChatGPT, DALL-E   │   │    │       │
│    │    │   │  Key: CREATES new  │   │    │       │
│    │    │   │  content           │   │    │       │
│    │    │   └────────────────────┘   │    │       │
│    │    └────────────────────────────┘    │       │
│    └──────────────────────────────────────┘       │
└──────────────────────────────────────────────────┘
```

### Teaching Tip:
Draw each circle one at a time. Pause after each to explain. Let students absorb the relationship before adding the next layer.

---

## Drawing 2: Traditional AI vs Generative AI

### When to Draw: Middle of Topic 1 (0:15)

```
TRADITIONAL AI                      GENERATIVE AI
                                    
Input                               Input
  │                                   │
  ▼                                   ▼
┌──────────────┐                   ┌──────────────┐
│   ANALYZE    │                   │  UNDERSTAND  │
│              │                   │              │
│  Classify    │                   │  Learn       │
│  Predict     │                   │  Patterns    │
│  Detect      │                   │              │
└──────┬───────┘                   └──────┬───────┘
       │                                  │
       ▼                                  ▼
┌──────────────┐                   ┌──────────────┐
│   OUTPUT     │                   │   CREATE     │
│              │                   │              │
│  "Spam"      │                   │  New Text    │
│  "Fraud"     │                   │  New Image   │
│  "Cat/Dog"   │                   │  New Code    │
└──────────────┘                   └──────────────┘

FINDS answers                      GENERATES answers
from existing data                 that never existed
```

---

## Drawing 3: How LLM Works — The Prediction Machine

### When to Draw: Topic 2 (0:25)

```
USER INPUT: "The capital of France is ___"

                    ┌─────────────────────────┐
                    │       TOKENIZER          │
                    │  "The" "capital" "of"    │
                    │  "France" "is"           │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │     EMBEDDINGS           │
                    │  Words → Numbers         │
                    │  [0.12, -0.34, 0.56...]  │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │   TRANSFORMER LAYERS     │
                    │   (Self-Attention)        │
                    │                          │
                    │  "France" pays attention │
                    │   to "capital" → knows   │
                    │   to predict a city name │
                    │                          │
                    │   96 layers of this!     │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │  PROBABILITY OUTPUT      │
                    │                          │
                    │  "Paris"    → 92%  ✓     │
                    │  "Lyon"     → 3%         │
                    │  "London"   → 1%         │
                    │  "Berlin"   → 1%         │
                    │  others     → 3%         │
                    └─────────────────────────┘

OUTPUT: "Paris"
```

### Teaching Tip:
Build this diagram from bottom to top. Start with the input, then show how each layer transforms the data.

---

## Drawing 4: Token Breakdown

### When to Draw: Topic 4 (0:40)

```
WHAT ARE TOKENS?

Words:    "I love machine learning"
Tokens:   [I] [love] [machine] [learning]
Count:    4 tokens

Words:    "Tokenization is important"  
Tokens:   [Token] [ization] [is] [important]
Count:    4 tokens (notice "Tokenization" = 2 tokens!)

Words:    "ChatGPT"
Tokens:   [Chat] [G] [PT]
Count:    3 tokens!

═══════════════════════════════════════

RULE OF THUMB:

┌──────────────────────────────────┐
│  1 token  ≈  4 characters        │
│  1 token  ≈  ¾ of a word         │
│  100 tokens ≈ 75 words           │
│  1 page   ≈  400-500 tokens      │
└──────────────────────────────────┘
```

---

## Drawing 5: Context Window — The Desk Analogy

### When to Draw: Topic 5 (0:45)

```
YOUR DESK (Context Window)
┌─────────────────────────────────────────┐
│                                          │
│  ┌────────────┐                          │
│  │ System     │  "You are a helpful..."  │
│  │ Prompt     │  (~500 tokens)           │
│  └────────────┘                          │
│                                          │
│  ┌────────────┐                          │
│  │ Message 1  │  "What is Python?"       │
│  └────────────┘                          │
│  ┌────────────┐                          │
│  │ Response 1 │  "Python is a..."        │
│  └────────────┘                          │
│  ┌────────────┐                          │
│  │ Message 2  │  "How do I install it?"  │
│  └────────────┘                          │
│  ┌────────────┐                          │
│  │ Response 2 │  "You can install..."    │
│  └────────────┘                          │
│                                          │
│  ┌────────────────────────────────────┐  │
│  │    SPACE FOR NEXT RESPONSE         │  │
│  │    (tokens remaining)              │  │
│  └────────────────────────────────────┘  │
│                                          │
└─────────────────────────────────────────┘

DESK SIZE:
GPT-3.5  → Small desk  (16K tokens)
GPT-4o   → Large desk  (128K tokens)
Gemini   → Warehouse   (2M tokens!)
```

---

## Drawing 6: Temperature Scale

### When to Draw: Topic 6 (0:55)

```
TEMPERATURE = CREATIVITY DIAL

Low ◄──────────────────────────────────────► High

0.0         0.3         0.7         1.0       2.0
 │           │           │           │         │
 ▼           ▼           ▼           ▼         ▼
┌────┐    ┌────┐     ┌────┐     ┌────┐    ┌────┐
│🎯  │    │📋  │     │✍️  │     │🎨  │    │🤪  │
│    │    │    │     │    │     │    │    │    │
│Same│    │Safe│     │Good│     │Wild│    │    │
│ans │    │    │     │mix │     │    │    │Chaos│
│ever│    │    │     │    │     │    │    │    │
│time│    │    │     │    │     │    │    │    │
└────┘    └────┘     └────┘     └────┘    └────┘
Code      Support    Content   Brainstorm  Never
Math      Q&A        Writing   Poetry      Use
Facts     Chatbot    Blogs     Stories     This
```

---

## Drawing 7: Hallucination — Why It Happens

### When to Draw: Topic 7 (1:00)

```
WHY LLMS HALLUCINATE

Input: "Who wrote 'The Azure Chronicles'?"
(This book doesn't exist!)

LLM's Process:
┌─────────────────────────────────────┐
│ Pattern: "Who wrote [book]"         │
│                                      │
│ Training data has thousands of:      │
│   "Who wrote Hamlet? → Shakespeare"  │
│   "Who wrote 1984? → George Orwell"  │
│   "Who wrote Harry Potter? → JK R." │
│                                      │
│ Pattern learned:                     │
│   "Who wrote [X]?" → [Famous Author] │
│                                      │
│ So for unknown book:                 │
│   "Who wrote Azure Chronicles?"      │
│   → "James Patterson"  ← WRONG!     │
│                                      │
│ The model PREDICTS, doesn't VERIFY   │
└─────────────────────────────────────┘

          ⚠️ KEY INSIGHT ⚠️
The LLM doesn't know what it doesn't know.
It always generates SOMETHING — never says
"this doesn't exist" by default.
```

---

## Drawing 8: API Architecture — How Your App Talks to LLMs

### When to Draw: Topic 8 (1:10)

```
YOUR AI APPLICATION ARCHITECTURE

┌──────────────┐         HTTPS          ┌──────────────────┐
│              │  ─────────────────►    │                  │
│   YOUR APP   │      API Request       │   LLM PROVIDER   │
│   (Python)   │                        │                  │
│              │  ◄─────────────────    │   ┌────────────┐ │
│  ┌────────┐  │      API Response      │   │  GPT-4o    │ │
│  │ API    │  │                        │   │  Gemini    │ │
│  │ Key    │  │                        │   │  Claude    │ │
│  └────────┘  │                        │   │  LLaMA     │ │
│              │                        │   └────────────┘ │
└──────────────┘                        └──────────────────┘

What you send (Request):
{
  "model": "gpt-4o-mini",
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."}
  ],
  "temperature": 0.7
}

What you get back (Response):
{
  "choices": [{
    "message": {
      "role": "assistant",
      "content": "Here's the answer..."
    }
  }],
  "usage": {
    "prompt_tokens": 50,
    "completion_tokens": 100,
    "total_tokens": 150
  }
}
```

---

## Drawing 9: Provider Comparison — Decision Matrix

### When to Draw: During API Providers section (1:15)

```
CHOOSING THE RIGHT PROVIDER

                    SPEED
                      ▲
                      │
           Groq ★     │
                      │
                      │        Gemini ★
                      │
                      │    OpenAI ★
                      │              Claude ★
                      │
    ──────────────────┼──────────────────► QUALITY
                      │
        HuggingFace ★ │
                      │
           Ollama ★   │
          (Local)     │
                      │
                      │
                      
    LEFT = Cheaper    RIGHT = Better Quality
    UP = Faster       DOWN = Slower

    ★ = Provider position (approximate)
```

---

## Drawing 10: Chatbot Architecture (Mini Project)

### When to Draw: Before Mini Project (1:30)

```
AI CHATBOT — CONVERSATION FLOW

┌──────┐     ┌────────────────────────────────────────┐
│ USER │     │          CONVERSATION HISTORY           │
│      │     │                                         │
│ "Hi" ├────►│ 1. System: "You are a helpful..."      │
│      │     │ 2. User: "Hi"                ← NEW     │
└──┬───┘     │                                         │
   │         └──────────────────┬──────────────────────┘
   │                            │
   │                   ┌────────▼────────┐
   │                   │   LLM API       │
   │                   │   (Groq/OpenAI) │
   │                   │                 │
   │                   │   Sends ALL     │
   │                   │   messages      │
   │                   └────────┬────────┘
   │                            │
   │         ┌──────────────────▼──────────────────────┐
   │         │          CONVERSATION HISTORY           │
   │         │                                         │
   │         │ 1. System: "You are a helpful..."      │
   │         │ 2. User: "Hi"                          │
   │◄────────│ 3. Assistant: "Hello! How can I..."    │
   │         │                           ← NEW        │
   │         └─────────────────────────────────────────┘
   │
   │ "What   ┌────────────────────────────────────────┐
   │  is     │ 1. System: "You are a helpful..."      │
   │  Python"│ 2. User: "Hi"                          │
   ├────────►│ 3. Assistant: "Hello! How can I..."    │
             │ 4. User: "What is Python?"  ← NEW      │
             └─────────────────────────────────────────┘

KEY INSIGHT: Every API call sends the ENTIRE history.
That's how the model "remembers" the conversation.
```

---

## 🎨 Drawing Tips for Instructor

### Colors to Use:
| Color  | Use For                              |
| ------ | ------------------------------------ |
| Blue   | Main concepts, titles                |
| Red    | Warnings, mistakes, important notes  |
| Green  | Good practices, correct answers      |
| Black  | Diagrams, text, arrows               |
| Yellow | Highlights, emphasis                 |

### General Tips:
1. **Draw slowly** — Students need time to copy
2. **Talk while drawing** — Don't draw in silence
3. **Use arrows** — Show flow and relationships
4. **Circle key terms** — Help visual learners
5. **Leave space** — You'll want to add annotations
6. **Take a photo** — Share with students after class
