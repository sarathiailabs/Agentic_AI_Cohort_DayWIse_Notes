# 📝 Day 5 – Assignment: Generative AI & LLM APIs

---

## 🏢 Scenario

You work as a **Junior AI Engineer** at **EduNext**, an EdTech startup that provides career guidance to college students and working professionals across India.

The CEO has tasked you with building a **proof-of-concept AI Career Mentor** that can:
- Understand a student's background and interests
- Provide personalized career guidance for tech roles
- Suggest learning roadmaps with specific resources
- Work as a conversational chatbot with memory

If the POC is successful, it will be integrated into EduNext's mobile app (50,000+ users).

---

## 🎯 Objective

Build a **command-line AI Career Mentor** using LLM APIs that demonstrates:
1. Effective use of system prompts for specialized behavior
2. Multi-turn conversation with memory
3. At least 2 different API providers
4. Error handling and graceful fallbacks
5. Session analytics (token tracking, cost estimation)

---

## 📋 Requirements

### Core Requirements (Must Have)

1. **System Prompt Design**
   - Design a detailed system prompt that makes the AI act as a career mentor
   - The mentor should specialize in tech careers (AI/ML, Web Dev, Data Science, DevOps, Cloud)
   - Include salary ranges (India + Global), real company names, and specific roadmaps
   - The AI should ask clarifying questions before giving advice

2. **Conversation Memory**
   - Maintain full conversation history across the session
   - The chatbot should remember previous messages and refer to them

3. **Multi-Provider Support**
   - Implement at least 2 API providers (e.g., Groq + Gemini)
   - Allow switching between providers via a command (e.g., typing "switch")

4. **User Commands**
   - `quit` — Exit the application
   - `stats` — Show session statistics (messages, tokens, estimated cost)
   - `save` — Save conversation to a JSON file
   - `clear` — Clear conversation history and start over

5. **Error Handling**
   - Handle API errors gracefully (rate limits, network issues, invalid keys)
   - Implement retry logic with exponential backoff
   - Never crash — always show a friendly error message

### Bonus Requirements (Nice to Have)

1. **Quick Assessment Mode** (+10 points)
   - Ask 5 structured questions about background, skills, interests, timeline, goals
   - Generate a comprehensive career recommendation based on answers

2. **Conversation Export to Markdown** (+5 points)
   - Export the conversation as a formatted Markdown file (not just JSON)
   - Include timestamps, session stats, and formatted Q&A

3. **Token Cost Comparison** (+5 points)
   - After each response, show estimated cost for the same query across 3 different providers
   - Help users understand the cost implications

4. **Multi-Language Support** (+5 points)
   - Allow users to chat in Hindi or another Indian language
   - AI responds in the user's preferred language

5. **Personality Modes** (+5 points)
   - Let users choose between mentoring styles:
     - `Professional` — Formal, data-driven advice
     - `Friendly` — Casual, encouraging mentor
     - `Strict` — No-nonsense, direct advice

---

## 📦 Deliverables

1. **`career_mentor.py`** — Main application file
2. **`requirements.txt`** — Dependencies list
3. **`.env.example`** — Example environment variables file (with placeholder keys)
4. **`README.md`** — Setup instructions, features list, usage examples
5. **`sample_conversation.json`** — One exported sample conversation

### File Structure:

```
day5_assignment/
├── career_mentor.py          # Main application
├── requirements.txt          # pip install -r requirements.txt
├── .env.example              # API key placeholders
├── .gitignore                # Exclude .env from Git
├── README.md                 # Documentation
├── exports/                  # Saved conversations
│   └── sample_conversation.json
└── screenshots/              # Terminal screenshots (optional)
```

---

## 🏆 Evaluation Rubric

| Criteria | Points | Description |
|----------|--------|-------------|
| **System Prompt Quality** | 15 | Detailed, effective, produces good career advice |
| **Conversation Memory** | 15 | Multi-turn conversations work correctly |
| **Multi-Provider Support** | 15 | At least 2 providers, can switch between them |
| **Error Handling** | 15 | Graceful error handling, retry logic, never crashes |
| **User Commands** | 10 | All required commands work (quit, stats, save, clear) |
| **Code Quality** | 10 | Clean, well-commented, modular code |
| **Session Analytics** | 10 | Token tracking, cost estimation displayed |
| **README & Documentation** | 10 | Clear setup instructions, feature list |
| **Bonus Features** | Up to 30 | See bonus requirements above |
| **Total** | 100 + 30 bonus | |

### Grading Scale:

| Score | Grade | Level |
|-------|-------|-------|
| 90-130 | ⭐ Exceptional | Production-ready quality |
| 75-89 | 🟢 Great | Strong implementation |
| 60-74 | 🟡 Good | Meets core requirements |
| 40-59 | 🟠 Needs Work | Missing key features |
| <40 | 🔴 Incomplete | Major gaps |

---

## 📤 Submission Format

1. Push your code to a GitHub repository
2. Name the repo: `ai-career-mentor` or `day5-assignment`
3. Include a proper README with:
   - Project description
   - Setup instructions
   - Features list
   - Screenshots of the chatbot in action
   - What you learned
4. Share the GitHub repo link

---

## 💡 Tips for Success

1. **Start with the system prompt** — Spend 15 minutes crafting a great prompt. It's the most important part.
2. **Get one provider working first** — Then add the second provider.
3. **Test edge cases** — What happens with empty input? Very long messages? API key errors?
4. **Use Groq for development** — It's free and fast. Perfect for testing.
5. **Add features incrementally** — Get core features working before adding bonus features.
6. **Comment your code** — Explain WHY, not just WHAT.
7. **Read the error messages** — API errors usually tell you exactly what went wrong.

---

## ⏰ Estimated Time

| Task | Time |
|------|------|
| System prompt design | 15 minutes |
| Core chatbot (1 provider) | 30 minutes |
| Multi-provider support | 20 minutes |
| User commands | 15 minutes |
| Error handling | 15 minutes |
| Session analytics | 10 minutes |
| Documentation | 15 minutes |
| **Total** | **~2 hours** |
| Bonus features | +1-2 hours |

---

## 🎯 Real World Relevance

This assignment simulates a real task you'd get in your first week as an AI Engineer at a startup:

- **Day 1:** "Build a POC of an AI chatbot for our product"
- **Day 2:** "Make it work with multiple providers so we're not locked into one"
- **Day 3:** "Add analytics so we know how much it costs"
- **Day 4:** "Handle errors properly so it doesn't crash in production"

Companies doing this right now: **Intercom (Fin AI)**, **Drift**, **Zendesk**, **Freshworks**
