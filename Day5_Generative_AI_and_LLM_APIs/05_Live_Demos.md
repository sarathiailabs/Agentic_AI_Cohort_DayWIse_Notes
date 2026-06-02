# 🎬 Day 5 – Live Demos: Generative AI & LLM APIs

> For each demo: Goal → Steps → Code → Expected Output → Discussion Questions

---

## Demo 1: Google Search vs ChatGPT

### 🎯 Goal
Show students the fundamental difference between search (finding information) and generation (creating information).

### ⏱️ Duration: 3 minutes

### 📝 Steps

1. Open Google in one browser tab
2. Open ChatGPT in another tab
3. Ask both the same question: **"Explain recursion in Python with an example"**
4. Compare the results side by side

### 🔍 What to Show:

**Google Results:**
```
- Link 1: GeeksforGeeks article (need to click, read, scroll)
- Link 2: Stack Overflow answer (need to filter through multiple answers)
- Link 3: Python docs (dense, hard for beginners)
- Link 4: W3Schools (basic, maybe outdated)

→ User must: Click, Read, Compare, Filter, Understand
→ Time: 5-10 minutes to get a good answer
```

**ChatGPT Result:**
```
- Direct explanation in simple language
- Code example tailored to the question
- Step-by-step breakdown
- No ads, no navigation, no filtering

→ User gets: Complete answer in 10 seconds
→ But: Need to VERIFY accuracy!
```

### 💬 Discussion Questions:

1. **"Which one gave you a better answer faster?"**
   Expected: ChatGPT

2. **"Which one can you trust more?"**
   Expected: Google (because it links to sources) — Great teaching moment about hallucinations!

3. **"If you were building a product, which would you use as a backend?"**
   Expected: Depends on use case — search for factual data, LLM for generation/conversation

4. **"What happens when the LLM's training data is outdated?"**
   Expected: It won't know recent events — leads to discussion about knowledge cutoff

---

## Demo 2: Token Counting — See Tokens in Action

### 🎯 Goal
Make tokens tangible. Students should visually see how text is broken into tokens and understand pricing.

### ⏱️ Duration: 3 minutes

### 📝 Steps

1. Open https://platform.openai.com/tokenizer
2. Type different texts and observe token counts

### 💻 Code Demo:

```python
"""
Demo: Understanding Tokens
Run this in your terminal to see tokens in action.
"""

# Method 1: Using tiktoken (OpenAI's tokenizer)
# pip install tiktoken
import tiktoken

# Get the tokenizer for GPT-4
encoder = tiktoken.encoding_for_model("gpt-4o")

# Example texts to tokenize
texts = [
    "Hello",
    "Hello World",
    "I am learning about LLMs",
    "Artificial Intelligence",
    "supercalifragilisticexpialidocious",
    "ChatGPT is amazing!",
    "Python programming language",
    "मैं हिंदी में लिख रहा हूं",  # Hindi text
    "def hello_world():\n    print('Hello!')",
]

print("=" * 60)
print(f"{'Text':<45} | {'Tokens':>6} | Token IDs")
print("=" * 60)

for text in texts:
    tokens = encoder.encode(text)
    print(f"{text:<45} | {len(tokens):>6} | {tokens[:5]}...")

print("=" * 60)

# Show individual tokens
print("\n📝 Detailed Token Breakdown:")
text = "Tokenization is important for LLMs"
tokens = encoder.encode(text)
decoded_tokens = [encoder.decode([t]) for t in tokens]
print(f"Text: '{text}'")
print(f"Tokens ({len(tokens)}): {decoded_tokens}")

# Cost calculation
print("\n💰 Cost Calculation Example:")
prompt_tokens = 500
completion_tokens = 1000
cost_per_1m_input = 0.15   # GPT-4o mini
cost_per_1m_output = 0.60  # GPT-4o mini

input_cost = (prompt_tokens / 1_000_000) * cost_per_1m_input
output_cost = (completion_tokens / 1_000_000) * cost_per_1m_output
total_cost = input_cost + output_cost

print(f"Input tokens: {prompt_tokens} → Cost: ${input_cost:.6f}")
print(f"Output tokens: {completion_tokens} → Cost: ${output_cost:.6f}")
print(f"Total cost per request: ${total_cost:.6f}")
print(f"Cost for 10,000 requests/day: ${total_cost * 10000:.2f}")
print(f"Monthly cost (30 days): ${total_cost * 10000 * 30:.2f}")
```

### 📊 Expected Output:

```
============================================================
Text                                          | Tokens | Token IDs
============================================================
Hello                                         |      1 | [9906]...
Hello World                                   |      2 | [9906, 4435]...
I am learning about LLMs                      |      5 | [40, 1097, 6975, 922, 445]...
Artificial Intelligence                       |      2 | [9470, 22107]...
supercalifragilisticexpialidocious             |     10 | [13066, 3035, ...]...
ChatGPT is amazing!                           |      4 | [16047, 38, 374, 8056]...
Python programming language                   |      3 | [31380, 15840, 4221]...
मैं हिंदी में लिख रहा हूं                         |     18 | [...]...
def hello_world():\n    print('Hello!')       |      9 | [...]...
============================================================

📝 Detailed Token Breakdown:
Text: 'Tokenization is important for LLMs'
Tokens (5): ['Token', 'ization', ' is', ' important', ' for', ' LL', 'Ms']

💰 Cost Calculation Example:
Input tokens: 500 → Cost: $0.000075
Output tokens: 1000 → Cost: $0.000600
Total cost per request: $0.000675
Cost for 10,000 requests/day: $6.75
Monthly cost (30 days): $202.50
```

### 💬 Discussion Questions:

1. **"Why does Hindi text use more tokens than English?"**
   Expected: Tokenizers are primarily trained on English — non-English text is less efficiently tokenized

2. **"If you're building a chatbot for India, how does this affect your costs?"**
   Expected: Hindi/regional language responses cost more tokens = higher API bills

3. **"How would you reduce token costs in a production app?"**
   Expected: Shorter prompts, summarize history, use cheaper models

---

## Demo 3: Temperature Comparison — Same Prompt, Different Creativity

### 🎯 Goal
Visually demonstrate how temperature affects output. Students should understand when to use what temperature.

### ⏱️ Duration: 4 minutes

### 💻 Code:

```python
"""
Demo: Temperature Comparison
Shows how the same prompt produces different results at different temperatures.
"""

from groq import Groq

client = Groq(api_key="your-groq-api-key")

prompt = "Write a one-sentence description of Python programming language."

temperatures = [0.0, 0.3, 0.7, 1.0, 1.5]

print("🌡️ TEMPERATURE COMPARISON")
print("=" * 70)
print(f"Prompt: '{prompt}'")
print("=" * 70)

for temp in temperatures:
    print(f"\n🌡️ Temperature: {temp}")
    print("-" * 50)
    
    # Call 3 times to show consistency vs variety
    for i in range(3):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=temp,
            max_tokens=100
        )
        result = response.choices[0].message.content.strip()
        print(f"  Run {i+1}: {result}")

print("\n" + "=" * 70)
print("🔑 KEY OBSERVATIONS:")
print("  temp=0.0 → Same answer every time (deterministic)")
print("  temp=0.7 → Similar but varied (balanced)")
print("  temp=1.5 → Very different, sometimes weird (creative/chaotic)")
```

### 📊 Expected Output:

```
🌡️ TEMPERATURE COMPARISON
======================================================================
Prompt: 'Write a one-sentence description of Python programming language.'
======================================================================

🌡️ Temperature: 0.0
--------------------------------------------------
  Run 1: Python is a high-level, interpreted programming language known for its simplicity and readability.
  Run 2: Python is a high-level, interpreted programming language known for its simplicity and readability.
  Run 3: Python is a high-level, interpreted programming language known for its simplicity and readability.

🌡️ Temperature: 0.7
--------------------------------------------------
  Run 1: Python is a versatile, high-level programming language celebrated for its clean syntax.
  Run 2: Python is a widely-used, interpreted language known for simplicity and powerful libraries.
  Run 3: Python is an intuitive programming language that makes coding accessible to beginners.

🌡️ Temperature: 1.5
--------------------------------------------------
  Run 1: Python dances between elegance and power, a serpentine language of digital creation.
  Run 2: A beginner's gateway and expert's toolkit, Python reshapes how we talk to machines.
  Run 3: Python—the Swiss army knife of code—slices through complexity with indented grace.

======================================================================
🔑 KEY OBSERVATIONS:
  temp=0.0 → Same answer every time (deterministic)
  temp=0.7 → Similar but varied (balanced)
  temp=1.5 → Very different, sometimes weird (creative/chaotic)
```

### 💬 Discussion Questions:

1. **"Which temperature would you use for a medical diagnosis chatbot?"**
   Expected: 0.0 — you want consistent, reliable answers

2. **"Which for a creative writing assistant?"**
   Expected: 0.7-1.0 — you want variety and creativity

3. **"Why not always use temperature 0?"**
   Expected: You'd get boring, repetitive content for creative tasks

---

## Demo 4: Hallucination Example — Catching the LLM Lying

### 🎯 Goal
Show students a LIVE hallucination so they understand the danger and learn to verify outputs.

### ⏱️ Duration: 3 minutes

### 💻 Code:

```python
"""
Demo: Hallucination Detection
Ask the LLM questions that might trigger hallucinations.
"""

from groq import Groq

client = Groq(api_key="your-groq-api-key")

# Questions designed to potentially trigger hallucinations
hallucination_tests = [
    {
        "question": "Who wrote the book 'The Azure Chronicles of Digital Wisdom'?",
        "truth": "This book does NOT exist. Any author name is a hallucination."
    },
    {
        "question": "What happened at the 2025 Mars Landing Ceremony?",
        "truth": "No Mars landing ceremony happened. Any details are fabricated."
    },
    {
        "question": "Tell me about the research paper 'Quantum Neural Bridges' by Dr. Sarah Chen published in Nature in 2023.",
        "truth": "This paper likely doesn't exist. The LLM may fabricate details."
    },
    {
        "question": "What is 7 * 13 * 19?",
        "truth": "The correct answer is 1,729. LLMs often get multi-step math wrong."
    }
]

print("🔍 HALLUCINATION DETECTION TEST")
print("=" * 70)

for i, test in enumerate(hallucination_tests, 1):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": test["question"]}
        ],
        temperature=0.7,
        max_tokens=200
    )
    
    answer = response.choices[0].message.content.strip()
    
    print(f"\n{'─' * 70}")
    print(f"❓ Question {i}: {test['question']}")
    print(f"\n🤖 LLM Answer: {answer[:200]}...")
    print(f"\n✅ TRUTH: {test['truth']}")
    print(f"\n⚠️  Hallucinated? {'YES - The LLM made this up!' if 'don' not in answer.lower() else 'Maybe not - it admitted uncertainty'}")

print(f"\n{'=' * 70}")
print("🔑 LESSON: Always verify LLM outputs, especially for:")
print("   1. Specific facts, dates, and names")
print("   2. Research papers and citations")
print("   3. Mathematical calculations")
print("   4. Events that haven't happened yet")
```

### 💬 Discussion Questions:

1. **"Were you surprised that the model confidently answered about a fake book?"**
   Expected: Yes! It's scary how convincing the fake answer is.

2. **"How would you fix this in a production application?"**
   Expected: RAG (Retrieval Augmented Generation), fact-checking, source citations

3. **"Why is this particularly dangerous in healthcare or finance?"**
   Expected: Wrong medical advice could harm patients. Wrong financial advice could cost money.

---

## Demo 5: Calling Groq API — Your First AI API Call

### 🎯 Goal
Students make their first LLM API call. This is the "Hello World" of AI engineering.

### ⏱️ Duration: 5 minutes

### 📋 Pre-requisites:
1. Groq API key from https://console.groq.com
2. `pip install groq`

### 💻 Code (Type This Live):

```python
"""
Demo: Your First AI API Call
This is the "Hello World" of AI Engineering!
"""

# Step 1: Import the library
from groq import Groq

# Step 2: Create a client with your API key
client = Groq(api_key="gsk_your_key_here")  # Get from console.groq.com

# Step 3: Send a message to the AI
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",   # Which AI model to use
    messages=[                          # The conversation
        {
            "role": "system",           # System = Instructions for AI
            "content": "You are a helpful Python tutor."
        },
        {
            "role": "user",             # User = What the human says
            "content": "What is a list in Python? Explain in 3 sentences."
        }
    ],
    temperature=0.7,                    # Creativity level
    max_tokens=200                      # Max response length
)

# Step 4: Print the response
print("🤖 AI Response:")
print(response.choices[0].message.content)

# Step 5: Check token usage
print(f"\n📊 Token Usage:")
print(f"  Input tokens:  {response.usage.prompt_tokens}")
print(f"  Output tokens: {response.usage.completion_tokens}")
print(f"  Total tokens:  {response.usage.total_tokens}")
```

### 📊 Expected Output:

```
🤖 AI Response:
A list in Python is a versatile, ordered collection that can hold multiple 
items of different data types, including numbers, strings, and even other 
lists. You can create a list using square brackets, like `my_list = [1, 2, 
"hello", True]`, and access elements using their index position starting 
from 0. Lists are mutable, meaning you can add, remove, or modify elements 
after creation using methods like `append()`, `remove()`, and `pop()`.

📊 Token Usage:
  Input tokens:  35
  Output tokens: 89
  Total tokens:  124
```

### What to Explain Line by Line:

1. **`from groq import Groq`** — "We import the Groq SDK. Just like importing `math` or `json`, but for AI."
2. **`client = Groq(api_key=...)`** — "The API key is like your password. It tells Groq who you are and bills your account."
3. **`model="llama-3.3-70b-versatile"`** — "This is Meta's LLaMA model with 70 billion parameters, running on Groq's fast hardware."
4. **`messages=[...]`** — "This is the conversation format. `system` = rules for AI. `user` = your question."
5. **`temperature=0.7`** — "Our creativity dial. 0.7 is a good default."
6. **`max_tokens=200`** — "Maximum response length. Prevents runaway costs."
7. **`response.choices[0].message.content`** — "The actual text response. `choices[0]` because the API can return multiple completions."
8. **`response.usage`** — "Token usage tracking. Critical for monitoring costs."

### 💬 Discussion Questions:

1. **"What happens if you change the system prompt to 'You are a pirate'?"**
   Let students try it live!

2. **"What if you set max_tokens to 10? What happens?"**
   Expected: The response gets cut off mid-sentence

3. **"How is this different from using ChatGPT in the browser?"**
   Expected: Same technology, but now YOU control it programmatically

---

## Demo 6: Simple AI Chatbot — Build It Live

### 🎯 Goal
Build a working chatbot with conversation memory in under 5 minutes.

### ⏱️ Duration: 5 minutes

### 💻 Code (Build step by step with students):

```python
"""
Demo: AI Chatbot with Memory
Build a ChatGPT-like experience in ~30 lines of Python!
"""

from groq import Groq

# Initialize client
client = Groq(api_key="gsk_your_key_here")

# The chatbot's personality
SYSTEM_PROMPT = """You are CodeBuddy, a friendly AI coding assistant.

Your personality:
- You explain things simply, like talking to a friend
- You use emojis occasionally to be friendly 😊
- You always encourage the learner
- You give short, practical answers (not essays)
- If asked about non-coding topics, you politely redirect

Example style:
User: "What is a variable?"
You: "Think of a variable as a labeled box 📦 where you store data!

```python
name = 'Alice'  # A box labeled 'name' containing 'Alice'
age = 25        # A box labeled 'age' containing 25
```

You can change what's inside anytime. That's why it's called a 'variable' — it can vary! 🎯"
"""

# Conversation memory — this is how the chatbot "remembers"
conversation = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

def get_response(user_message: str) -> str:
    """Send a message and get a response from the AI."""
    # Add user message to conversation history
    conversation.append({"role": "user", "content": user_message})
    
    # Call the AI
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation,
        temperature=0.7,
        max_tokens=1024
    )
    
    # Extract response text
    ai_message = response.choices[0].message.content
    
    # Save AI response to conversation history
    conversation.append({"role": "assistant", "content": ai_message})
    
    return ai_message

# Main chat loop
def main():
    print("🤖 CodeBuddy - Your AI Coding Assistant")
    print("=" * 45)
    print("Type your coding questions! (type 'quit' to exit)")
    print("=" * 45)
    
    while True:
        # Get user input
        user_input = input("\n👤 You: ").strip()
        
        # Check for exit
        if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
            print("\n🤖 CodeBuddy: Happy coding! See you next time! 👋")
            break
        
        # Skip empty input
        if not user_input:
            print("🤖 CodeBuddy: Please type something! 😊")
            continue
        
        # Get AI response
        response = get_response(user_input)
        print(f"\n🤖 CodeBuddy: {response}")

if __name__ == "__main__":
    main()
```

### 📊 Expected Interaction:

```
🤖 CodeBuddy - Your AI Coding Assistant
=============================================
Type your coding questions! (type 'quit' to exit)
=============================================

👤 You: What is a for loop?

🤖 CodeBuddy: A for loop lets you repeat code for each item in a collection! 🔄

```python
# Loop through a list of fruits
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I love {fruit}!")
```

Output:
```
I love apple!
I love banana!
I love cherry!
```

Think of it like going through a shopping list — you handle each item one by one! 🛒

👤 You: Can you show me a while loop?

🤖 CodeBuddy: Sure! A while loop repeats code AS LONG AS a condition is true ♾️

```python
# Count from 1 to 5
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1
```

Notice it remembers our previous chat about for loops! The key difference:
- `for` loop: "Do this for each item" 
- `while` loop: "Keep doing this until I say stop"

👤 You: quit

🤖 CodeBuddy: Happy coding! See you next time! 👋
```

### 💬 Discussion Questions:

1. **"Why does the chatbot remember the previous message about for loops?"**
   Expected: Because we store ALL messages in `conversation` list and send them every time

2. **"What happens when the conversation gets very long?"**
   Expected: Eventually exceeds context window → need to truncate/summarize old messages

3. **"How is this different from ChatGPT?"**
   Expected: Same core concept! ChatGPT just has a fancy web UI, but the backend is similar

4. **"What would you change to make this a customer support bot instead?"**
   Expected: Change the system prompt! The code stays the same.

---

## 🎯 Demo Summary

| Demo | What Students Learn                          | Key Takeaway                              |
| ---- | -------------------------------------------- | ----------------------------------------- |
| 1    | Google vs ChatGPT                            | Search finds info, LLMs generate info     |
| 2    | Token Counting                               | Tokens ≠ words, they affect cost          |
| 3    | Temperature Comparison                       | Lower = consistent, Higher = creative     |
| 4    | Hallucination Example                        | LLMs can confidently lie — always verify  |
| 5    | First API Call                               | 10 lines of code = AI-powered application |
| 6    | AI Chatbot                                   | Conversation memory = sending all history |
