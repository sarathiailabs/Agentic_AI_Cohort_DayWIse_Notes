"""
Day 6 Assignment: LinkedIn Post Generator
Author: Cohort Teaching Team
Date: 2026

This tool takes a raw technical topic and generates a highly engaging,
pre-formatted LinkedIn post using Role Prompting and Few-Shot examples.
"""

import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load environment configurations
load_dotenv()

# Verify API configuration
groq_key = os.getenv("GROQ_API_KEY")

if groq_key and not groq_key.endswith("_here"):
    print("[Active LLM Provider: Groq (llama-3.3-70b-versatile)]")
    client = OpenAI(
        api_key=groq_key,
        base_url="https://api.groq.com/openai/v1"
    )
    MODEL_NAME = "llama-3.3-70b-versatile"
else:
    ollama_base = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
    ollama_model = os.getenv("OLLAMA_MODEL", "llama3")
    print(f"[Active LLM Provider: Ollama ({ollama_model} via {ollama_base})]")
    client = OpenAI(
        api_key="ollama",
        base_url=ollama_base
    )
    MODEL_NAME = ollama_model

SYSTEM_ROLE = """
You are a world-class Developer Advocate and tech content copywriter who writes viral, highly engaging technical LinkedIn updates.
Your tone is technical, direct, and conversational. Avoid corporate clichés like 'thrilled to announce' or 'groundbreaking paradigm'.

For every topic requested, you must follow this exact layout:
1. Hook: A punchy first-line statement (starts with a relevant emoji).
2. Context: 2 sentences explaining why the topic matters.
3. Bullet points: 3 concise, bulleted key facts or takeaways (using '-' as bullet point).
4. Pro-tip: A single tactical '💡 Pro-tip:' line.
5. CTA: An open-ended discussion question.
"""

FEW_SHOT_TEMPLATES = """
Example 1:
Topic: Stop using global pip installations
Post:
📦 Stop installing Python packages globally!

Every time you run 'pip install' without an active virtual environment, you risk corrupting your system path variables.

Here is why virtual environments are a non-negotiable best practice:
- Prevents version conflicts between different project libraries
- Avoids modifying shared system files required by the operating system
- Makes deployments predictable by keeping local and production trees identical

💡 Pro-tip: Use 'uv venv' to create environments in less than 0.1 seconds.

Are you still using global installations, or have you fully switched? Let me know below! 👇
---
Example 2:
Topic: Git Rebase vs Git Merge
Post:
🔀 Git Merge or Git Rebase? Stop guessing and choose the right strategy.

Using the wrong branch strategy can clutter your history or delete critical debugging context.

Here is what you need to know:
- Use 'git merge' to preserve the complete history of feature branches
- Use 'git rebase' to keep your main branch commit history linear and readable
- Never rebase commits that have been pushed to a public remote branch

💡 Pro-tip: Run 'git log --graph --oneline' to visualize your branch commit tree.

What's your team's policy on branch strategies? Let's discuss in the comments! 👇
---
"""

def generate_post(topic_text: str) -> str:
    """
    Sends the prompt to OpenAI and gets the completed LinkedIn post.
    """
    # Wrap user input in XML-like tags to prevent prompt injection
    user_prompt = f"""
    {FEW_SHOT_TEMPLATES}
    
    Topic: <topic>{topic_text}</topic>
    Post:
    """
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_ROLE},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7  # Temperature set to 0.7 for creative wording
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Runtime Error calling API: {str(e)}"

def main():
    print("=" * 60)
    print("🚀 PROMPT-ENGINEERED LINKEDIN POST GENERATOR")
    print("=" * 60)
    
    topic = input("Enter a technical topic or idea: ").strip()
    if not topic:
        print("\nNo topic entered. Using default: 'Learning Docker containerization'")
        topic = "Learning Docker containerization"
        
    print("\nDrafting post...")
    post_output = generate_post(topic)
    
    print("\n" + "-" * 50)
    print(post_output)
    print("-" * 50 + "\n")

if __name__ == "__main__":
    main()
