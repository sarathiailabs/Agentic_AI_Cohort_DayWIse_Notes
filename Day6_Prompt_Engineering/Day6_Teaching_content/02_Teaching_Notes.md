# 📝 Day 6 – Teaching Notes: Prompt Engineering

## Comprehensive Instructor Guide

### Session Timeline & Flow (120 Minutes)

*   **00:00 - 00:15 (15m): Introduction & The Problem**
    *   Hook the students with a story of a failed generic LLM output.
    *   Explain the "illusion of mind reading."
    *   Define Prompt Engineering.
*   **00:15 - 00:45 (30m): Zero, One, and Few-Shot Prompting**
    *   Explain with concrete examples.
    *   Show how few-shot prompting teaches style and structure.
    *   Interact with students: ask them to classify items.
*   **00:45 - 01:10 (25m): Role Prompting & Chain of Thought**
    *   The power of personas. Contrast generic prompts vs. role prompts.
    *   Solve complex math/logic puzzles on the board using CoT. Show why models fail without it.
*   **01:10 - 01:30 (20m): ReAct Prompting Intro**
    *   How ReAct prompts connect LLMs to actions.
    *   Detail the Thought ➔ Action ➔ Observation loop.
*   **01:30 - 01:50 (20m): Live Coding & Demos**
    *   Demo 1: The LinkedIn Post Generator in action.
    *   Demo 2: The Email Generator showing reasoning paths.
*   **01:50 - 02:00 (10m): Wrap-up & Q&A**
    *   Explain the assignment requirements and rubric.

---

## Part 1: The Narrative Hook

### Story: The Copywriting Nightmare (5 minutes)
*   **Narrative:** *"Imagine you're the social media manager for a hot AI startup. You need to write 5 LinkedIn posts a day about Python, Git, and LLMs to drive traffic."*
*   **Conflict:** *"You're busy, so you go to ChatGPT and type: 'Write a LinkedIn post about why Python is awesome.' ChatGPT outputs a post starting with 'Hey LinkedIn Fam! 🚀 Spark your day with Python... ✨' filled with corporate fluff, 15 emojis, and zero actual insight. It looks generic and spammy."*
*   **Resolution:** *"You write a strict prompt defining a persona: 'You are an opinionated, elite backend engineer who writes short, technical, text-only insights.' Suddenly, the LLM outputs a clean, readable post with 500+ likes. That is prompt engineering."*

---

## Part 2: Analogies for Teaching

### 1. The Chef Analogy (Zero vs. Few-Shot)
*   **Zero-Shot:** You walk up to a world-class chef and say, "Make me a dessert." The chef doesn't know if you like chocolate, fruit, or ice cream. They guess, and you might hate it.
*   **One-Shot:** You say, "Make me a dessert. Here is a picture of a chocolate lava cake I like. Make something similar." Now the chef has a style guide.
*   **Few-Shot:** You say, "Here are 3 desserts I love: a fruit tart, a chocolate soufflé, and a lemon meringue. Notice they are all light, not too sweet, and beautifully plated. Now make a new dessert." The chef has a complete pattern of your taste, constraints, and presentation requirements.

### 2. The Math Exam (Chain of Thought)
*   If you give a student a 5-step algebra question and tell them, "You have 1 second to write only the final answer or you fail," they will guess and fail.
*   But if you say, "Show your calculations line-by-line, and then write the final answer," they get it right.
*   LLMs are the same: they generate text token-by-token. Giving them the space to output their reasoning steps gives them the "computational draft paper" they need to succeed.

---

## Part 3: Instructor Scripts & Prompts

### Zero-Shot vs Few-Shot Class Discussion
*   **Instructor Says:** *"Why does the LLM hallucinate or write bad content when you give it zero examples?"*
*   **Expected Student Answer:** *"Because it doesn't have reference data on how we want the output structured, so it pulls from the average statistical probability of all text on the internet."*
*   **Instructor Discussion Point:** *"Exactly! Few-shot prompting acts as an in-context learning mechanism. We aren't changing the model's weights, we are temporarily biasing its attention mechanism toward our specific style."*

---

## Part 4: Key Checkpoints & Troubleshooting

*   **Checkpoint 1:** Can students distinguish between few-shot prompting and model fine-tuning? (Fine-tuning changes weights; few-shot is in-context learning).
*   **Checkpoint 2:** Do students understand why temperature should be lower for logic tasks (CoT) and slightly higher for creative writing (LinkedIn Generator)?
*   **Troubleshooting:** If the model ignores the role persona, ensure the role prompt is at the very beginning of the prompt string or passed as a `system` message if using chat endpoints.
