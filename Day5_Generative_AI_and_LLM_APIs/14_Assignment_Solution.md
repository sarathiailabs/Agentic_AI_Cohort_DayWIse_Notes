# ✅ Day 5 – Assignment Solution: AI Career Mentor

> Solution architecture, folder structure, implementation plan, and development guide. Full code is NOT provided — students should build it themselves using this as a reference.

---

## 🏗️ Solution Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                    AI CAREER MENTOR                           │
│                                                               │
│  ┌─────────────┐                                             │
│  │ User Input   │                                             │
│  │ (Terminal)   │                                             │
│  └──────┬──────┘                                             │
│         │                                                     │
│  ┌──────▼──────────────────────────────────────────┐         │
│  │          COMMAND ROUTER                          │         │
│  │                                                   │         │
│  │  "quit" → Exit     "stats" → Analytics           │         │
│  │  "save" → Export   "clear" → Reset               │         │
│  │  "switch" → Change Provider                       │         │
│  │  "assess" → Quick Assessment                      │         │
│  │  else → Chat Message                              │         │
│  └──────┬──────────────────────────────────────────┘         │
│         │                                                     │
│  ┌──────▼──────────────────────────────────────────┐         │
│  │          CAREER MENTOR ENGINE                     │         │
│  │                                                   │         │
│  │  ┌──────────────┐   ┌────────────────────────┐   │         │
│  │  │ System Prompt │   │ Conversation History   │   │         │
│  │  │ (Career       │   │ (Full message list)    │   │         │
│  │  │  Expert)      │   │                        │   │         │
│  │  └──────────────┘   └────────────────────────┘   │         │
│  │                                                   │         │
│  │  ┌──────────────────────────────────────────────┐│         │
│  │  │ LLM Provider Manager                        ││         │
│  │  │                                              ││         │
│  │  │  Provider 1: Groq (Primary)                  ││         │
│  │  │  Provider 2: Gemini (Fallback)               ││         │
│  │  │                                              ││         │
│  │  │  Retry logic + Exponential backoff           ││         │
│  │  └──────────────────────────────────────────────┘│         │
│  │                                                   │         │
│  │  ┌──────────────────────────────────────────────┐│         │
│  │  │ Analytics Engine                             ││         │
│  │  │  - Token count (input/output)                ││         │
│  │  │  - Cost estimation                           ││         │
│  │  │  - Session duration                          ││         │
│  │  │  - Topics discussed                          ││         │
│  │  └──────────────────────────────────────────────┘│         │
│  └──────────────────────────────────────────────────┘         │
│                                                               │
│  ┌──────────────────────────────────────────────────┐         │
│  │          EXPORT ENGINE                            │         │
│  │  - JSON export (conversation data)               │         │
│  │  - Markdown export (formatted Q&A)               │         │
│  └──────────────────────────────────────────────────┘         │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

---

## 📁 Folder Structure

```
day5_assignment/
│
├── career_mentor.py          # Main application (all-in-one for simplicity)
│
├── requirements.txt          # Dependencies
│   groq
│   google-generativeai
│   python-dotenv
│
├── .env.example              # Template for API keys
│   GROQ_API_KEY=gsk_your_key_here
│   GEMINI_API_KEY=your_gemini_key_here
│
├── .gitignore                # Security
│   .env
│   __pycache__/
│   exports/
│
├── README.md                 # Documentation
│
└── exports/                  # Auto-created directory for saved conversations
    └── .gitkeep
```

---

## 📋 Implementation Plan

### Phase 1: Foundation (30 min)

1. **Create project structure**
   - Create directory
   - Create `requirements.txt`
   - Create `.env` file with API keys
   - Create `.gitignore`

2. **Design system prompt**
   - Define the career mentor persona
   - Include career paths, salary ranges, companies
   - Set rules for conversation flow
   - Test the prompt in ChatGPT first to validate quality

3. **Implement basic chatbot**
   - Connect to Groq API
   - Send/receive messages
   - Print responses

### Phase 2: Core Features (30 min)

4. **Add conversation memory**
   - Maintain `conversation_history` list
   - Append user + assistant messages after each turn

5. **Implement user commands**
   - `quit` — Show stats and exit
   - `stats` — Display session analytics
   - `save` — Export to JSON
   - `clear` — Reset conversation

6. **Add error handling**
   - Wrap API calls in try/except
   - Implement retry with backoff
   - Handle empty input, keyboard interrupt

### Phase 3: Multi-Provider (20 min)

7. **Add second provider (Gemini)**
   - Create Gemini client
   - Implement `switch` command
   - Ensure messages format works for both

8. **Implement fallback**
   - If primary fails, try secondary
   - Log which provider was used

### Phase 4: Analytics & Polish (20 min)

9. **Token tracking**
   - Count tokens for each request
   - Calculate estimated cost
   - Show in `stats` command

10. **Conversation export**
    - Save to JSON with metadata
    - Include session info, timestamps

11. **Polish UX**
    - Welcome banner
    - Clear prompts
    - Helpful error messages

---

## 🔑 Key Implementation Details

### System Prompt Design Tips

```python
# BAD — Too vague
system_prompt = "You are a career mentor."

# GOOD — Detailed, structured, actionable
system_prompt = """You are CareerAI, a senior tech career mentor...

YOUR EXPERTISE:
- AI/ML Engineering (₹8L-₹50L)
- Full-Stack Development (₹5L-₹40L)
...

YOUR APPROACH:
1. Ask 2 clarifying questions BEFORE giving advice
2. Provide specific, actionable steps
3. Include salary ranges and company names
4. Suggest a 90-day learning plan
...

RULES:
- Never guarantee job placement
- Always be encouraging but realistic
- End with a clear "Next Step"
"""
```

### Multi-Provider Pattern

```python
# The key insight: abstract the API call
class LLMProvider:
    def __init__(self, name, client, model):
        self.name = name
        self.client = client
        self.model = model
    
    def chat(self, messages):
        # Each provider has slightly different syntax
        # Abstract it behind a common interface
        pass

# Then switch providers easily:
providers = [groq_provider, gemini_provider]
active = 0

def switch_provider():
    active = (active + 1) % len(providers)
```

### Error Handling Pattern

```python
def safe_chat(messages, max_retries=3):
    for attempt in range(max_retries):
        try:
            return primary_provider.chat(messages)
        except RateLimitError:
            time.sleep(2 ** attempt)
        except Exception:
            # Try fallback provider
            try:
                return fallback_provider.chat(messages)
            except:
                if attempt == max_retries - 1:
                    return "I'm having connection issues. Please try again."
```

### Analytics Tracking

```python
class Analytics:
    def __init__(self):
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.start_time = datetime.now()
        self.message_count = 0
    
    def update(self, usage):
        self.total_input_tokens += usage.prompt_tokens
        self.total_output_tokens += usage.completion_tokens
        self.message_count += 1
    
    def get_cost(self, provider):
        pricing = {"groq": (0.59, 0.79), "gemini": (0.075, 0.30)}
        rates = pricing.get(provider, (0.15, 0.60))
        return (self.total_input_tokens / 1e6 * rates[0] + 
                self.total_output_tokens / 1e6 * rates[1])
```

---

## 🐛 Debugging Guide

### Common Issues and Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| `AuthenticationError` | Wrong API key | Check `.env` file, verify key on provider website |
| `RateLimitError` | Too many requests | Add retry logic with `time.sleep(60)` |
| `InvalidRequestError` | Messages format wrong | Check `role` is "system", "user", or "assistant" |
| `ConnectionError` | No internet | Add offline error handling |
| Response is `None` | API returned empty | Check `max_tokens`, add null check |
| Memory issues | Conversation too long | Implement sliding window (keep last 20 messages) |

### Testing Checklist

- [ ] Basic conversation works
- [ ] Bot remembers previous messages
- [ ] `quit` command exits cleanly
- [ ] `stats` shows correct token counts
- [ ] `save` creates JSON file
- [ ] `clear` resets conversation
- [ ] Error when internet is off → friendly message
- [ ] Empty input → handled gracefully
- [ ] Ctrl+C → doesn't crash, exits cleanly
- [ ] Multi-provider switch works

---

## 📚 Best Practices Applied

1. **Environment variables** for API keys (not hardcoded)
2. **Retry logic** with exponential backoff
3. **Clean code** with functions/classes, not one big script
4. **Error messages** that help the user, not scare them
5. **Token tracking** for cost awareness
6. **Conversation export** for data persistence
7. **Documentation** (README) for other developers
8. **.gitignore** to prevent accidental key leaks
