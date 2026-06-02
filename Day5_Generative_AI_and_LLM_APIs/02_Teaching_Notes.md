# 📋 Day 5 – Teaching Notes: Generative AI & LLM APIs

## 🎯 Instructor Guide

> These notes tell you exactly what to say, when to say it, what to write on the whiteboard, and how to handle student questions.

---

## ⏱️ Session Timeline (2 Hours)

| Time          | Duration | Topic                              | Activity             |
| ------------- | -------- | ---------------------------------- | -------------------- |
| 0:00 – 0:05  | 5 min    | Welcome & Context Setting          | Talk + Poll          |
| 0:05 – 0:25  | 20 min   | AI vs ML vs DL vs GenAI            | Lecture + Whiteboard |
| 0:25 – 0:40  | 15 min   | What is an LLM? + How LLMs Work   | Lecture + Demo       |
| 0:40 – 0:55  | 15 min   | Tokens + Context Window            | Lecture + Live Demo  |
| 0:55 – 1:05  | 10 min   | Temperature + Hallucinations       | Lecture + Demo       |
| 1:05 – 1:10  | 5 min    | ☕ Quick Break                     | Break                |
| 1:10 – 1:30  | 20 min   | API Providers (All 6)              | Live Coding          |
| 1:30 – 1:50  | 20 min   | Mini Project: AI Chatbot           | Hands-on Coding      |
| 1:50 – 2:00  | 10 min   | Wrap-up + Assignment Brief         | Discussion           |

---

## 📍 Segment 1: Welcome & Context Setting (0:00 – 0:05)

### What to Say:

> "Welcome to Day 5! Today is a game-changer. We've spent 4 days learning Python and Git — the foundation. Today, we start building with AI."
>
> "Quick show of hands: How many of you have used ChatGPT?"
> *(Wait — most hands should go up)*
>
> "Now, how many of you have built something WITH ChatGPT's technology? Like built your own chatbot?"
> *(Fewer or no hands)*
>
> "By the end of today, every single one of you will have built a working AI chatbot. Not using ChatGPT — building your OWN ChatGPT-like application."
>
> "Let's start by understanding what's really happening behind the scenes."

### Energy Level: 🔥🔥🔥 HIGH
Start with energy. This is the "cool" day — students are excited about AI.

---

## 📍 Segment 2: AI vs ML vs DL vs GenAI (0:05 – 0:25)

### Opening Question:

> "Before we talk about AI, let me ask: What's the smartest thing your phone does?"

**Expected answers:** Autocomplete, face unlock, Siri/Google Assistant, photo suggestions

> "Great! All of those use some form of AI. But here's the thing — they use DIFFERENT types of AI. Let's understand the difference."

### 🖊️ Whiteboard Instructions:

**Draw the nested circles diagram:**

```
1. Draw a large circle — label it "AI"
2. Inside it, draw a smaller circle — label it "ML"
3. Inside ML, draw a smaller circle — label it "DL"
4. Inside DL, draw the smallest circle — label it "GenAI"
```

### What to Say While Drawing:

> "Think of this like Russian dolls. AI is the biggest concept — any machine that acts smart."
>
> *(Draw AI circle)*
>
> "Inside AI, we have Machine Learning. Not all AI learns — a calculator is AI but not ML. ML specifically means the machine learns from data."
>
> *(Draw ML circle inside)*
>
> "Inside ML, we have Deep Learning. It uses neural networks — inspired by the human brain. This is what powers image recognition, voice assistants."
>
> *(Draw DL circle inside)*
>
> "And the newest, most exciting layer: Generative AI. This doesn't just analyze data — it CREATES new content. Text, images, code, music, video."
>
> *(Draw GenAI circle inside)*

### Teaching the Difference with Examples:

> "Let me make this concrete with examples you use daily."

**Write on whiteboard:**

```
AI:     Thermostat (adjusts temp — follows rules)
ML:     Netflix recommendations (learns your taste)
DL:     Face ID on your phone (recognizes your face)
GenAI:  ChatGPT (writes new text that never existed before)
```

### Student Interaction Point:

> "Quick quiz: Is Google Maps AI, ML, DL, or GenAI?"

**Expected answer:** ML (it learns from traffic patterns)

> "What about Alexa?"

**Expected:** AI (mostly rule-based for commands, some ML for understanding speech)

> "What about DALL-E generating images?"

**Expected:** GenAI

### 🚨 Common Student Question:

**Q: "Is GenAI just a fancy chatbot?"**

> "No! GenAI includes text generation (ChatGPT), image generation (DALL-E, Midjourney), code generation (Copilot), music generation (Suno), and even video generation (Sora). It's an entire new paradigm of computing."

### Key Analogy to Use:

> "Traditional AI is like a librarian — finds answers from existing books. GenAI is like an author — writes entirely new books."

---

## 📍 Segment 3: What is an LLM + How LLMs Work (0:25 – 0:40)

### Transition:

> "Now that we know GenAI creates new content — let's understand the technology behind it. When you use ChatGPT, the engine under the hood is called an LLM — Large Language Model."

### What to Say:

> "LLM stands for three things: Large — billions of parameters. Language — understands and generates text. Model — a trained neural network."
>
> "Here's the mind-blowing part: LLMs don't understand language the way you and I do. They're the world's most sophisticated autocomplete."

### 🖊️ Whiteboard Instructions:

**Draw the prediction flow:**

```
"The cat sat on the ___"

Next word prediction:
  mat   → 65%
  chair → 15%
  floor → 10%
  table → 5%
  dog   → 5%

Model picks: "mat" ✓
```

### What to Say:

> "Your phone's keyboard suggests the next word, right? An LLM does the same thing, but it's been trained on the ENTIRE internet. So its predictions are incredibly accurate."
>
> "GPT-4 has about 1.8 trillion parameters. That's 1.8 trillion knowledge connections. Your phone's autocomplete has maybe a few million."

### Live Demo (2 minutes):

> "Let me show you. I'll open ChatGPT and ask it to complete a sentence. Watch how it generates one token at a time."

Open ChatGPT → Type: "Write a story about a programmer who" → Show the streaming response appearing word by word.

> "See how it appears word by word? Each word is a prediction based on everything before it."

### Student Interaction:

> "If I ask the LLM: 'The president of the United States in 2020 was ___' — what will it say?"

**Expected:** "Donald Trump" or "Joe Biden" depending on interpretation

> "Now, what if I ask: 'The president of Mars in 2020 was ___' — what will it say?"

**Expected:** It will make something up! → This leads naturally to hallucinations

> "It will confidently generate a name — a completely made-up name. Because it's predicting what word is MOST LIKELY to come next, not what's TRUE. Remember this — it's the key to understanding hallucinations."

---

## 📍 Segment 4: Tokens + Context Window (0:40 – 0:55)

### Transition:

> "Now, you might wonder — when you type a message to ChatGPT, does it see individual letters? Words? Sentences? The answer is: TOKENS."

### What to Say About Tokens:

> "Tokens are pieces of words. Not characters, not full words — pieces."
>
> "The word 'ChatGPT' is actually 3 tokens: 'Chat', 'G', 'PT'."
>
> "Why does this matter? Because you PAY per token. Your app's COST depends on tokens. Your model's MEMORY is measured in tokens."

### 🖊️ Whiteboard:

```
"Hello World"          → 2 tokens
"I am learning Python" → 4 tokens  
"Tokenization"         → 2 tokens ("Token" + "ization")

Rule: 1 token ≈ 4 characters ≈ ¾ word
     100 tokens ≈ 75 words
     1 page ≈ 400-500 tokens
```

### 💰 Cost Example (Write on Board):

```
GPT-4o mini pricing:
  Input:  $0.15 per 1 million tokens
  Output: $0.60 per 1 million tokens

Your chatbot:
  Average conversation: 2,000 tokens
  1,000 users/day: 2,000,000 tokens/day
  Monthly cost: ~$30/month

That's CHEAP for AI!
```

### Live Demo — Token Counter:

> "Let me show you a live token counter."

Go to: https://platform.openai.com/tokenizer

Type different texts and show how tokens are counted.

> "Notice how 'hello' is 1 token but 'antidisestablishmentarianism' is 6 tokens. Longer, rarer words use more tokens."

### Context Window:

> "Now, here's something crucial. The context window is the LLM's TOTAL MEMORY for one conversation."

### 🖊️ Whiteboard:

```
Context Window = Everything the model can "see" at once

GPT-3.5:   16K tokens  ≈  25 pages
GPT-4o:    128K tokens ≈  300 pages  
Claude 3.5: 200K tokens ≈  500 pages
Gemini 1.5: 2M tokens  ≈  5,000 pages!

What fits inside:
┌──────────────────────────────┐
│ System Prompt (~500 tokens)  │
│ Message 1                    │
│ Response 1                   │
│ Message 2                    │
│ Response 2                   │
│ ...                          │
│ Latest Message               │
│ Space for Response           │
└──────────────────────────────┘
```

> "If your conversation exceeds the context window, the model literally can't see the earlier messages. That's why ChatGPT sometimes 'forgets' what you said earlier in a long conversation."

### Student Interaction:

> "Pop quiz: If GPT-4o has a 128K context window and your system prompt uses 1,000 tokens, how many tokens are left for conversation?"

**Expected:** 127,000 tokens

> "And if each message+response averages 500 tokens, how many exchanges can you have?"

**Expected:** ~254 exchanges — plenty for most conversations!

---

## 📍 Segment 5: Temperature + Hallucinations (0:55 – 1:05)

### Temperature:

> "Now let's talk about something fun — the Temperature parameter. It's like a creativity dial."

### 🖊️ Whiteboard:

```
Temperature Scale:

0.0 ──── 0.3 ──── 0.7 ──── 1.0 ──── 2.0
│         │         │         │        │
Exact     Safe     Balanced  Random   Chaos
(code)   (support) (content) (brainstorm)
```

> "Temperature 0 = always gives the same answer. Perfect for math, code, facts."
>
> "Temperature 0.7 = default for most use cases. Good balance."
>
> "Temperature 1.0+ = wild, creative, unpredictable. Good for brainstorming."

### Live Demo (1 minute):

Call the API twice with temperature=0 for "What is 2+2?" → Same answer both times.

Call twice with temperature=1.0 for "Write a haiku about coding" → Different answers!

### Hallucinations:

> "Now, the most DANGEROUS aspect of LLMs: Hallucinations."
>
> "In 2023, a lawyer used ChatGPT to write a legal brief. ChatGPT cited court cases that DON'T EXIST. The lawyer got fined $5,000."

### 🖊️ Whiteboard:

```
Hallucination = LLM generates confident but WRONG information

Why?
1. It predicts probable words, not TRUE words
2. No built-in fact-checking
3. Fills knowledge gaps with plausible-sounding content

How to mitigate:
1. Always verify LLM output
2. Use temperature=0 for facts
3. Use RAG (Day 8) to ground in real data
4. Tell the model: "Say I don't know if unsure"
```

### Student Interaction:

> "Why do you think companies like banks and hospitals can't just deploy ChatGPT for critical decisions?"

**Expected:** Because it might hallucinate → wrong medical/financial advice → lawsuits, harm

> "Exactly. This is why AI ENGINEERS are needed — to build systems that MINIMIZE hallucinations. You'll learn RAG on Day 8, which is the industry standard solution."

---

## 📍 BREAK (1:05 – 1:10)

> "Take 5 minutes. Grab water. When we come back, we're writing code."

---

## 📍 Segment 6: API Providers — Live Coding (1:10 – 1:30)

### Setup:

> "Now the fun part. We're going to call REAL LLM APIs."

**Pre-session requirements (shared before class):**
- Students should have API keys ready:
  - Groq (free, instant): https://console.groq.com
  - Google Gemini (free tier): https://aistudio.google.com
  - (Optional) OpenAI: https://platform.openai.com

### Live Coding Flow:

**Demo 1: Groq API (Start here — free and fast)**

> "We'll start with Groq because it's free, fast, and uses the same format as OpenAI."

```python
# Type this LIVE, explaining each line
from groq import Groq

client = Groq(api_key="your-key-here")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Python in 2 sentences?"}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
```

> "See how fast that was? Groq uses custom hardware called LPUs — Language Processing Units. 10x faster than GPT-4."

**Demo 2: Google Gemini**

```python
import google.generativeai as genai

genai.configure(api_key="your-key")
model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Explain machine learning in simple terms")
print(response.text)
```

> "Notice the API syntax is different from OpenAI/Groq. Each provider has their own SDK."

**Demo 3: OpenAI (if students have keys)**

```python
from openai import OpenAI

client = OpenAI(api_key="your-key")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "What is machine learning?"}
    ]
)

print(response.choices[0].message.content)
```

### Key Teaching Moments:

1. **After each API call, ask:** "What's the same across all providers? What's different?"
   - Same: Send messages, get text response
   - Different: SDK syntax, model names, pricing, speed

2. **Point out:** "Notice the `messages` format — `role` and `content`. This is the standard pattern. `system` tells the model HOW to behave. `user` is the human's message. `assistant` is the model's response."

3. **Cost comparison:**
   > "The same query cost us $0.001 on GPT-4o mini, $0.0001 on Groq, and $0 on Gemini's free tier. Choosing the right provider can save you thousands."

---

## 📍 Segment 7: Mini Project — AI Chatbot (1:30 – 1:50)

### What to Say:

> "Now let's build something real. We're going to build an AI chatbot with conversation memory — just like ChatGPT."

### Live Coding (guide students step by step):

```python
# Build this together, line by line
from groq import Groq

client = Groq(api_key="your-key")

# System prompt defines the chatbot's personality
system_prompt = """You are a friendly AI assistant. 
You help with coding questions, explain concepts simply, 
and always encourage the learner."""

# Conversation memory
conversation_history = [
    {"role": "system", "content": system_prompt}
]

def chat(user_message):
    """Send a message and get a response."""
    # Add user's message to history
    conversation_history.append(
        {"role": "user", "content": user_message}
    )
    
    # Call the API
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history,
        temperature=0.7,
        max_tokens=1024
    )
    
    # Extract the response
    assistant_message = response.choices[0].message.content
    
    # Save to history (memory!)
    conversation_history.append(
        {"role": "assistant", "content": assistant_message}
    )
    
    return assistant_message

# Chat loop
print("🤖 AI Chatbot (type 'quit' to exit)")
print("-" * 40)

while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() in ['quit', 'exit', 'bye']:
        print("🤖 Goodbye! Happy coding!")
        break
    
    response = chat(user_input)
    print(f"\n🤖 Assistant: {response}")
```

### While Building, Explain:

1. **System prompt:** "This is like giving the chatbot its personality and rules"
2. **Conversation history:** "This is how it remembers previous messages — just a list of dictionaries"
3. **The chat function:** "Every time you send a message, ALL previous messages go to the API. That's how it maintains context"
4. **The loop:** "This is the simplest UI — just terminal input/output"

### Student Exercise (5 minutes):

> "Now modify the chatbot! Change the system prompt to make it:
> - A pirate who explains coding
> - A fitness trainer who motivates you
> - A chef who recommends recipes
>
> Be creative! Change the personality and test it."

---

## 📍 Segment 8: Wrap-up + Assignment (1:50 – 2:00)

### Summary:

> "Let's recap what you learned today:"
>
> 1. "AI → ML → DL → GenAI — each more specific and powerful"
> 2. "LLMs are massive next-token prediction machines"
> 3. "Tokens are the currency — you pay per token"
> 4. "Context window is the model's memory limit"
> 5. "Temperature controls creativity"
> 6. "Hallucinations are the #1 risk — always verify"
> 7. "Six API providers — OpenAI, Gemini, Claude, Groq, HuggingFace, Ollama"
> 8. "You built a working AI chatbot!"
>
> "Tomorrow, we learn Prompt Engineering — how to make LLMs do EXACTLY what you want."

### Assignment Preview:

> "Your assignment: Build an AI Career Mentor. It should:
> - Ask the user about their background and interests
> - Provide career guidance for AI/tech roles
> - Suggest a learning roadmap
> - Work as a conversational chatbot
>
> Details are in the assignment file. Due before next session."

---

## 🚨 Troubleshooting Guide for Instructor

### Common Issues During Class:

| Issue                              | Solution                                         |
| ---------------------------------- | ------------------------------------------------ |
| Student doesn't have API key       | Use Groq (free, instant signup)                  |
| `pip install` fails                | Use `uv pip install` or `uv add`                 |
| Rate limit error                   | Wait 60 seconds or use a different provider       |
| Import error                       | Run: `pip install openai groq google-generativeai`|
| "API key invalid" error            | Check for extra spaces, verify on provider website|
| Slow response                      | Switch to Groq for speed                         |
| Student gets hallucination         | GREAT teaching moment — explain why it happened  |

### Backup Plans:

- If internet is down: Use Ollama (local) or show pre-recorded demos
- If API provider is down: Switch to another provider
- If students finish early: Challenge them to add features (chat history saving, multi-model support)

---

## 📝 Post-Session Checklist

- [ ] Students can explain AI vs ML vs DL vs GenAI
- [ ] Students understand LLMs and next-token prediction
- [ ] Students understand tokens and pricing
- [ ] Students successfully called at least 1 API
- [ ] Students built a working chatbot
- [ ] Assignment is clearly understood
- [ ] Groq/Gemini API keys are working for all students
