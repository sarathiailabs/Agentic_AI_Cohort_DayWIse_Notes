# 📚 Day 5 – Resources: Generative AI & LLM APIs

> Curated resources for further learning. Organized by topic and difficulty level.

---

## 🔗 API Documentation (Official)

| Provider | Documentation | API Key Signup |
|----------|--------------|----------------|
| **OpenAI** | [platform.openai.com/docs](https://platform.openai.com/docs) | [platform.openai.com](https://platform.openai.com) |
| **Google Gemini** | [ai.google.dev/docs](https://ai.google.dev/docs) | [aistudio.google.com](https://aistudio.google.com) |
| **Anthropic Claude** | [docs.anthropic.com](https://docs.anthropic.com) | [console.anthropic.com](https://console.anthropic.com) |
| **Groq** | [console.groq.com/docs](https://console.groq.com/docs) | [console.groq.com](https://console.groq.com) |
| **HuggingFace** | [huggingface.co/docs](https://huggingface.co/docs) | [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) |
| **Ollama** | [ollama.ai](https://ollama.ai) | No signup needed |

---

## 📖 Essential Reading

### Beginner Level

| Resource | Type | Link | Why Read |
|----------|------|------|----------|
| "Attention Is All You Need" (Simplified) | Blog | [jalammar.github.io/illustrated-transformer](https://jalammar.github.io/illustrated-transformer/) | Best visual explanation of Transformers |
| "What are LLMs?" | Article | OpenAI Blog | Official explanation from the makers |
| OpenAI Tokenizer | Tool | [platform.openai.com/tokenizer](https://platform.openai.com/tokenizer) | Visual token counting tool |
| tiktoken Library | GitHub | [github.com/openai/tiktoken](https://github.com/openai/tiktoken) | Programmatic token counting |

### Intermediate Level

| Resource | Type | Link | Why Read |
|----------|------|------|----------|
| OpenAI Cookbook | GitHub | [github.com/openai/openai-cookbook](https://github.com/openai/openai-cookbook) | Production-ready code examples |
| Prompt Engineering Guide | Guide | [promptingguide.ai](https://www.promptingguide.ai/) | Comprehensive prompt engineering |
| LLM University by Cohere | Course | [cohere.com/llmu](https://docs.cohere.com/docs/llmu) | Free LLM fundamentals course |
| AI Canon | Reading List | [a16z.com/ai-canon](https://a16z.com/ai-canon/) | Curated AI reading list by a16z |

### Advanced Level

| Resource | Type | Link | Why Read |
|----------|------|------|----------|
| "Attention Is All You Need" | Paper | [arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762) | The original Transformer paper |
| "Language Models are Few-Shot Learners" (GPT-3) | Paper | [arxiv.org/abs/2005.14165](https://arxiv.org/abs/2005.14165) | Understanding scale |
| "Training language models to follow instructions" (InstructGPT) | Paper | [arxiv.org/abs/2203.02155](https://arxiv.org/abs/2203.02155) | How RLHF works |
| Andrej Karpathy's "Let's build GPT" | Video | [YouTube](https://www.youtube.com/watch?v=kCc8FmEb1nY) | Build a GPT from scratch |

---

## 🎓 Free Courses

| Course | Provider | Duration | Level |
|--------|----------|----------|-------|
| ChatGPT Prompt Engineering for Developers | DeepLearning.AI + OpenAI | 1 hour | Beginner |
| Building Systems with ChatGPT API | DeepLearning.AI + OpenAI | 1 hour | Intermediate |
| LangChain for LLM Application Development | DeepLearning.AI + LangChain | 1 hour | Intermediate |
| Generative AI for Everyone | DeepLearning.AI (Andrew Ng) | 3 hours | Beginner |
| Google AI Essentials | Google | 10 hours | Beginner |
| HuggingFace NLP Course | HuggingFace | 20 hours | Intermediate |

---

## 🛠️ Tools & Libraries

### Python Libraries for LLM Development

```bash
# Core LLM APIs
pip install openai          # OpenAI SDK
pip install groq            # Groq SDK (fast inference)
pip install google-generativeai  # Google Gemini SDK
pip install anthropic       # Anthropic Claude SDK
pip install huggingface_hub # HuggingFace SDK

# Token Counting
pip install tiktoken        # OpenAI's tokenizer

# Environment Management
pip install python-dotenv   # Load .env files

# Coming in later days:
pip install langchain       # LLM framework (Day 12)
pip install chromadb        # Vector database (Day 9)
pip install langgraph       # Agent framework (Day 14)
```

### Development Tools

| Tool | Purpose | Link |
|------|---------|------|
| **VS Code** | Code editor | [code.visualstudio.com](https://code.visualstudio.com) |
| **Jupyter Notebook** | Interactive coding | Pre-installed with Python |
| **Postman** | API testing | [postman.com](https://www.postman.com) |
| **OpenAI Playground** | Test prompts in browser | [platform.openai.com/playground](https://platform.openai.com/playground) |
| **Google AI Studio** | Test Gemini in browser | [aistudio.google.com](https://aistudio.google.com) |

---

## 🎙️ Recommended YouTube Channels

| Channel | Focus | Why Watch |
|---------|-------|-----------|
| **Andrej Karpathy** | Deep technical AI | Former Tesla AI Director, builds things from scratch |
| **3Blue1Brown** | Math/AI visualization | Best visual explanations of neural networks |
| **Fireship** | Quick tech explainers | "100 seconds" format, great for quick concepts |
| **NetworkChuck** | Hands-on tutorials | Beginner-friendly, practical projects |
| **Two Minute Papers** | AI research summaries | Stay current with latest papers |
| **Yannic Kilcher** | AI paper reviews | Deep dives into important papers |

---

## 📊 AI Model Leaderboards & Benchmarks

| Leaderboard | What It Tracks | Link |
|-------------|---------------|------|
| **LMSYS Chatbot Arena** | Human-rated LLM rankings | [lmsys.org/leaderboard](https://chat.lmsys.org/?leaderboard) |
| **Open LLM Leaderboard** | Open-source model benchmarks | [huggingface.co/spaces](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) |
| **Artificial Analysis** | Speed, price, quality comparison | [artificialanalysis.ai](https://artificialanalysis.ai/) |

---

## 🌐 Communities

| Community | Platform | Why Join |
|-----------|----------|----------|
| r/MachineLearning | Reddit | Research discussions |
| r/LocalLLaMA | Reddit | Open-source LLM community |
| HuggingFace Discord | Discord | Model discussions, help |
| LangChain Discord | Discord | LLM app development help |
| AI Twitter/X | Social | Follow AI researchers and engineers |
| LinkedIn AI Groups | LinkedIn | Professional networking + job opportunities |

---

## 📅 What's Next in This Cohort

| Day | Topic | Connection to Day 5 |
|-----|-------|---------------------|
| **Day 6** | Prompt Engineering | How to write better prompts for the APIs you learned today |
| **Day 7** | Advanced Prompt Engineering | System prompts, structured outputs, function calling |
| **Day 8** | RAG Fundamentals | How to fix hallucinations using real documents |
| **Day 9** | Vector Databases | How to store and search knowledge for your AI apps |
| **Day 10** | Advanced RAG | Production-ready AI with grounded responses |
| **Day 12** | LangChain | Framework that makes everything from today 10x easier |
| **Day 13** | AI Agents | Make your LLMs take actions, not just chat |

---

## 💡 Quick Reference Card

### API Call Template (Works with OpenAI/Groq)

```python
from groq import Groq  # or: from openai import OpenAI

client = Groq(api_key="your-key")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "Your instructions here"},
        {"role": "user", "content": "User's message here"}
    ],
    temperature=0.7,
    max_tokens=500
)

print(response.choices[0].message.content)
print(f"Tokens: {response.usage.total_tokens}")
```

### Environment Setup

```bash
# 1. Install dependencies
pip install groq google-generativeai python-dotenv

# 2. Create .env file
echo "GROQ_API_KEY=gsk_your_key" > .env
echo "GEMINI_API_KEY=your_key" >> .env

# 3. Load in Python
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
```

### Temperature Quick Guide

```
0.0 → Code, Math, Facts
0.3 → Customer Support
0.7 → General Content (DEFAULT)
1.0 → Creative Writing
```

### Token Estimation

```
1 page of English text ≈ 400-500 tokens
1 token ≈ 4 characters
100 tokens ≈ 75 words
```
