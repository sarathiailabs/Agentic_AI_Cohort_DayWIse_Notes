# 🎨 Day 6 – Whiteboard Drawings: Visualizing Prompt Engineering

Use these ASCII drawings on the board to visually explain the mechanics of prompting.

---

## 1. Zero-Shot vs. Few-Shot In-Context Learning

This drawing illustrates how Few-Shot prompting biases the attention mechanism towards a specific output structure.

```
ZERO-SHOT PROMPTING:
====================
Prompt: "Summarize this bug: 'Login page button is misaligned on Mobile Safari.'"
               │
               ▼
┌──────────────────────────────────────────────┐
│             LLM General Weights              │
│ (Sees bug ➔ guesses format ➔ outputs prose)   │
└──────────────────────────────────────────────┘
               │
               ▼
Output: "This bug reports that when a user attempts to log in on Mobile Safari, the login button appears off-center."


FEW-SHOT PROMPTING:
===================
Prompt:
"Bug: 'Home page footer overlaps text on iPad' ➔ [BUG-UI]: Footer overlap on iPad
 Bug: 'API payment checkout times out' ➔ [BUG-API]: Payment timeout
 Bug: 'Login button misaligned on Mobile Safari' ➔ "
               │
               ▼
┌──────────────────────────────────────────────┐
│       LLM Attention Mechanism Activated       │
│ (Detects formatting pattern: [BUG-TYPE]: Msg)│
└──────────────────────────────────────────────┘
               │
               ▼
Output: "[BUG-UI]: Login button misaligned on Mobile Safari"
```

---

## 2. Role Prompting Context Constraining

This drawing shows how role prompts narrow down the target distribution of generated tokens from "all internet text" to "specific expert voice."

```
LLM Knowledge Space (All web text, reddit, journals, tutorials)
┌─────────────────────────────────────────────────────────────┐
│  • Reddit Comments   • Academic Papers   • Spam Articles     │
│                                                             │
│         Role Prompt: "You are a Senior Security Auditor"    │
│         ┌─────────────────────────────────────────┐         │
│         │ • Threat Reports   • CVE Databases     │         │
│         │ • Secure Coding Guides                  │         │
│         │                                         │         │
│         │        User Query: "Check this code"    │         │
│         │        ┌────────────────────────┐       │         │
│         │        │  Outputs specific,     │       │         │
│         │        │  actionable audit log  │       │         │
│         │        └────────────────────────┘       │         │
│         └─────────────────────────────────────────┘         │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Chain of Thought (CoT) Calculation Space

This diagram visualizes why Chain of Thought works. In Standard Prompting, the LLM must generate the final token immediately, causing mathematical calculation errors. In CoT, it writes intermediate tokens as "scratchpad state" memory.

```
STANDARD PROMPTING (Error-prone):
=================================
Question: "If a pool fills at 10L/min and leaks at 2L/min, how long to fill 400L?"
LLM Output: "It will take..." (LLM calculates next token '50' without writing math steps)
Result: ❌ "It will take 40 minutes." (Wrong calculation)


CHAIN OF THOUGHT PROMPTING (Reliable):
======================================
Question: "If a pool fills at 10L/min and leaks at 2L/min, how long to fill 400L? Think step-by-step."

LLM Output (Scratchpad tokens generated):
1. "Net fill rate = Fill rate - Leak rate"
2. "Net fill rate = 10L/min - 2L/min = 8L/min"
3. "Total volume to fill = 400L"
4. "Time needed = Total volume / Net fill rate"
5. "Time needed = 400L / 8L/min = 50 minutes"
Result:  "Therefore, it will take 50 minutes." (Correct calculation)
```

---

## 4. The ReAct Prompt Structure

This diagram shows how a ReAct prompt guides the LLM to format output that an external python runner can parse to execute actions.

```
User Query: "What is the stock price of AAPL?"
     │
     ▼
┌──────────────┐
│  LLM Brain   │ ◄─────────────────────────┐
└──────┬───────┘                           │
       │                                   │
       ▼ Output text in ReAct format       │
Thought: I need to check the AAPL stock    │
         price. I should use StockTool.    │
Action: StockTool[AAPL]                    │
     │                                     │
     ▼ Parser extracts action              │
┌──────────────┐                           │
│ Python Tool  │                           │
│  Execution   │                           │
└──────┬───────┘                           │
       │                                   │
       ▼ Tool returns result               │
Observation: Stock AAPL is $180.25         │
(Result fed back into LLM context) ────────┘
```
