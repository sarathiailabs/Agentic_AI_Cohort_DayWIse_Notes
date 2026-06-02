# ⚠️ Day 5 – Common Mistakes: Generative AI & LLM APIs

> 15 mistakes beginners make with LLMs and how to avoid them.

---

## Mistake 1: Hardcoding API Keys in Source Code

### ❌ The Mistake
```python
# NEVER DO THIS!
client = OpenAI(api_key="sk-abc123xyz789...")
```

### 🤦 Why It Happens
- Students copy-paste from tutorials
- Quick prototyping leads to bad habits
- Don't understand Git history exposure

### 😱 What Goes Wrong
- API key gets pushed to GitHub → bots scan for keys → your account gets drained
- Real case: A developer leaked an AWS key on GitHub. $50,000 bill in 24 hours.

### ✅ How to Fix
```python
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

Create a `.env` file (add to `.gitignore`):
```
OPENAI_API_KEY=sk-abc123xyz789...
```

---

## Mistake 2: Not Setting `max_tokens`

### ❌ The Mistake
```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Tell me about Python"}]
    # No max_tokens specified!
)
```

### 🤦 Why It Happens
- Seems optional in tutorials
- "Let the model decide how much to write"

### 😱 What Goes Wrong
- Model generates 4,000+ tokens for a simple question
- API costs balloon unexpectedly
- Slow response times

### ✅ How to Fix
```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Tell me about Python"}],
    max_tokens=500  # Always set a reasonable limit!
)
```

---

## Mistake 3: Sending Entire Conversation History Every Time Without Limit

### ❌ The Mistake
```python
conversation = [{"role": "system", "content": system_prompt}]

# After 100 messages, you're sending ALL 100 messages with every request!
def chat(msg):
    conversation.append({"role": "user", "content": msg})
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=conversation  # This grows forever!
    )
```

### 🤦 Why It Happens
- Tutorials show simple examples without context management
- "It works, so why change it?"

### 😱 What Goes Wrong
- Token count grows linearly → costs explode
- Eventually exceeds context window → crashes
- Slower responses as history grows

### ✅ How to Fix
```python
def chat(msg):
    conversation.append({"role": "user", "content": msg})
    
    # Keep only the last 20 messages + system prompt
    messages_to_send = [conversation[0]] + conversation[-20:]
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages_to_send,
        max_tokens=500
    )
```

---

## Mistake 4: Trusting LLM Output Without Verification

### ❌ The Mistake
```python
# Using LLM output directly in production without checking
medical_advice = get_llm_response("What medication should I take for headache?")
display_to_user(medical_advice)  # Dangerous!
```

### 🤦 Why It Happens
- LLM responses are convincing
- "ChatGPT said it, so it must be right"
- Excitement about AI capabilities overrides caution

### 😱 What Goes Wrong
- Hallucinated medical advice → patient harm
- Fabricated legal citations → $5,000 fine (real case!)
- Wrong code suggestions → security vulnerabilities

### ✅ How to Fix
1. Always add disclaimers for critical domains
2. Use RAG to ground responses in verified data
3. Implement human-in-the-loop for high-stakes decisions
4. Use system prompts that instruct the model to say "I'm not sure"
5. Never use LLM output directly for medical, legal, or financial decisions

---

## Mistake 5: Using the Wrong Temperature for the Task

### ❌ The Mistake
```python
# Using high temperature for factual questions
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What is 2+2?"}],
    temperature=1.5  # Too creative for math!
)
```

### 🤦 Why It Happens
- Don't understand what temperature does
- Use default or random temperature values

### 😱 What Goes Wrong
- Math questions get wrong answers
- Customer support gives inconsistent responses
- Creative tasks get boring, repetitive output

### ✅ How to Fix
| Task | Temperature |
|------|------------|
| Code generation | 0.0 - 0.2 |
| Factual Q&A | 0.0 |
| Customer support | 0.3 |
| Content writing | 0.7 |
| Brainstorming | 0.9 - 1.0 |

---

## Mistake 6: Ignoring Error Handling

### ❌ The Mistake
```python
# No try-except, no retries
def chat(message):
    response = client.chat.completions.create(...)
    return response.choices[0].message.content  # Will crash on any error!
```

### 🤦 Why It Happens
- "It works in my testing"
- Error handling feels like boilerplate

### 😱 What Goes Wrong
- Rate limits → app crashes
- Network timeout → unhandled exception
- API downtime → entire application goes down

### ✅ How to Fix
```python
import time

def chat(message, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(...)
            return response.choices[0].message.content
        except RateLimitError:
            time.sleep(2 ** attempt)  # Exponential backoff
        except APIError as e:
            if attempt == max_retries - 1:
                return "Sorry, I'm having trouble. Please try again."
    return "Service temporarily unavailable."
```

---

## Mistake 7: Using Expensive Models for Simple Tasks

### ❌ The Mistake
```python
# Using GPT-4o for everything
response = client.chat.completions.create(
    model="gpt-4o",  # $2.50/$10.00 per 1M tokens
    messages=[{"role": "user", "content": "Say hello"}]
)
```

### 🤦 Why It Happens
- "More expensive = better"
- Don't know cheaper alternatives exist

### 😱 What Goes Wrong
- API bill: $5,000/month instead of $100/month
- No quality improvement for simple tasks
- Slower responses (larger models are slower)

### ✅ How to Fix
```python
# Use GPT-4o mini for simple tasks ($0.15/$0.60 per 1M)
simple_response = client.chat.completions.create(
    model="gpt-4o-mini",  # 16x cheaper input, 16x cheaper output!
    messages=[{"role": "user", "content": "Say hello"}]
)

# Use GPT-4o only for complex reasoning tasks
complex_response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Analyze this complex contract..."}]
)
```

**Strategy:** Route simple queries to cheap models, complex queries to powerful models.

---

## Mistake 8: Not Using System Prompts

### ❌ The Mistake
```python
# No system prompt — model behaves generically
messages = [
    {"role": "user", "content": "Help me with my resume"}
]
```

### 🤦 Why It Happens
- Seems unnecessary
- "The model is smart enough without instructions"

### 😱 What Goes Wrong
- Generic, unfocused responses
- Inconsistent behavior across conversations
- No guardrails on what the model says

### ✅ How to Fix
```python
messages = [
    {"role": "system", "content": "You are a professional resume writer. "
     "Focus on tech industry resumes. Use bullet points. "
     "Highlight quantifiable achievements. "
     "Keep suggestions concise and actionable."},
    {"role": "user", "content": "Help me with my resume"}
]
```

**System prompts improve quality by 10x** for the same model.

---

## Mistake 9: Not Tracking Token Usage

### ❌ The Mistake
```python
response = client.chat.completions.create(model="gpt-4o", messages=[...])
print(response.choices[0].message.content)
# Never checks response.usage!
```

### 🤦 Why It Happens
- Focused on getting the response
- "I'll worry about costs later"

### 😱 What Goes Wrong
- Surprise $10,000 bill at month end
- No way to debug cost spikes
- Can't optimize because you can't measure

### ✅ How to Fix
```python
response = client.chat.completions.create(model="gpt-4o-mini", messages=[...])

# Always log token usage
print(f"Input: {response.usage.prompt_tokens} tokens")
print(f"Output: {response.usage.completion_tokens} tokens")
print(f"Cost: ${(response.usage.prompt_tokens * 0.15 + response.usage.completion_tokens * 0.60) / 1_000_000:.6f}")
```

---

## Mistake 10: Confusing Model Knowledge Cutoff with Real-Time Knowledge

### ❌ The Mistake
```python
# Asking about recent events
response = chat("Who won the 2025 Champions League?")
# Model confidently answers with potentially wrong/fabricated information!
```

### 🤦 Why It Happens
- LLMs feel omniscient
- No visible "last updated" indicator

### 😱 What Goes Wrong
- Confident answers about events after the training cutoff
- Outdated information presented as current facts
- Users make decisions based on wrong information

### ✅ How to Fix
- Know each model's knowledge cutoff date
- For recent information, use RAG or web search integration
- Add system prompt: "Your knowledge has a cutoff. For recent events, say 'I may not have the latest information on this.'"

---

## Mistake 11: Writing Vague Prompts

### ❌ The Mistake
```python
response = chat("Tell me about coding")
# Vague prompt = vague answer
```

### ✅ How to Fix
```python
response = chat("Explain 3 key benefits of learning Python for a fresher "
                "looking for their first software engineering job. "
                "Include specific job roles and salary ranges in India.")
# Specific prompt = specific, useful answer
```

---

## Mistake 12: Not Handling the `stream=True` Response Correctly

### ❌ The Mistake
```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[...],
    stream=True
)
# Trying to access response.choices[0].message.content → ERROR!
```

### ✅ How to Fix
```python
stream = client.chat.completions.create(model="gpt-4o-mini", messages=[...], stream=True)
full_response = ""
for chunk in stream:
    if chunk.choices[0].delta.content:
        content = chunk.choices[0].delta.content
        full_response += content
        print(content, end="", flush=True)
```

---

## Mistake 13: Mixing Up API Syntax Between Providers

### ❌ The Mistake
```python
# Using OpenAI syntax with Anthropic → crashes
response = anthropic_client.chat.completions.create(...)  # Wrong!
```

### ✅ How to Fix
Each provider has its own syntax. Learn the differences:
```python
# OpenAI: response.choices[0].message.content
# Anthropic: message.content[0].text
# Gemini: response.text
# Groq: response.choices[0].message.content (same as OpenAI!)
```

---

## Mistake 14: Not Setting `.gitignore` Before First Commit

### ❌ The Mistake
Committing `.env` files or API keys before adding them to `.gitignore`. Git history remembers everything — even deleted files.

### ✅ How to Fix
Create `.gitignore` FIRST:
```
.env
*.key
config.yaml
__pycache__/
```

If you accidentally committed a key: **Rotate the key immediately!** Removing the file from Git doesn't remove it from history.

---

## Mistake 15: Building Without a System Prompt Template

### ❌ The Mistake
Writing ad-hoc system prompts for every project. Inconsistent quality and behavior.

### ✅ How to Fix — Use a Template
```python
SYSTEM_PROMPT_TEMPLATE = """
You are {role}.

YOUR EXPERTISE: {expertise}

RESPONSE STYLE:
- {style_1}
- {style_2}

RULES:
- {rule_1}
- {rule_2}
- If unsure, say "I'm not certain about this."
"""
```

Having a template ensures consistent quality across all your AI applications.
