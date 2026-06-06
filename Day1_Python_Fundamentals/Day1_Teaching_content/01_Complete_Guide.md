# 📖 Day 1 Complete Guide: Python Fundamentals & UV Package Manager

## Master Reference Document

**Day:** 1 of 20
**Topic:** Python Fundamentals & UV Package Manager
**Duration:** 2 Hours (120 Minutes)
**Difficulty Level:** Beginner
**Prerequisites:** None (Builds from absolute zero)

---

## 🎯 Executive Summary

Welcome to Day 1 of the AI Engineer & Agentic AI Engineer Bootcamp. Today, we establish the core foundations of programming. We introduce **Python** from scratch and set up our development environment using **UV**, a modern, blazing-fast Python package manager. Students will learn the mechanics of variables, data types, operators, conditional logic, loops, and terminal Input/Output (I/O). The session is designed to transform tier 2/3 city college students from passive tech users into active builders.

---

## 📅 2-Hour Session Timing and Timeline

| Time Slot | Elapsed Time  | Duration | Section / Focus           | Description                                                           |
| --------- | ------------- | -------- | ------------------------- | --------------------------------------------------------------------- |
| 1         | 00:00 - 00:10 | 10 mins  | Intro & Setup             | Today's Problem Statement, UV installation overview                   |
| 2         | 00:10 - 00:30 | 20 mins  | Conceptual & Story        | Variables & Data Types, Kirana Store Credit Ledger Analogy            |
| 3         | 00:30 - 00:50 | 20 mins  | Technical & Architecture  | Conditions & Loops, Auto-rickshaw fare structure, IRCTC queue analogy |
| 4         | 00:50 - 01:10 | 20 mins  | Whiteboard & Interaction  | Memory layout, flow control diagrams, and student interactive Q&A     |
| 5         | 01:10 - 01:40 | 30 mins  | Live Coding & Practice    | Interactive setup of `uv`, environment run, simple I/O scripting    |
| 6         | 01:40 - 01:55 | 15 mins  | Industry Context & Review | Industry use cases, 10 common beginner mistakes, FAQs                 |
| 7         | 01:55 - 02:00 | 5 mins   | Assignment & Wrap-up      | Student assignment explanation, rubric, and wrap-up                   |

> [!TIP]
> **Pacing Reminder:** If environment setup with `uv` takes longer than 15 minutes due to slow college lab internet, have students pair up or focus on the logical syntax first, and run code in the browser/repl temporarily.

---

## 📚 Section 1: Problem Statement [00:00 - 00:10 | Duration: 10 mins]

### What problem existed before programming?

Imagine running a local kirana (grocery) store in a tier 3 town. Every day, 100+ customers buy items. Some pay cash, some buy on credit (*udhaari*).

- **Manual tracking:** You write transactions in a paper diary (*khata register*).
- **The chaos:** Pages tear, handwriting is messy, and manually summing up credits at the end of the month takes hours. You make calculation mistakes, losing money.
- **Why automation matters:** We need a system that remembers numbers (variables), categorizes them (data types), calculates totals (operators), takes decisions (conditions), and automates repetitive reminders (loops).

### Why Python?

Python is written in plain English like syntax. Instead of worrying about complex memory management or semicolons (like in C++ or Java), an AI Engineer can write thoughts directly into code. Almost all modern AI and Machine Learning systems (OpenAI, Gemini, LangChain, PyTorch) are built using Python.

### Why UV Package Manager?

Traditionally, Python users used `pip` and `venv`. However:

1. They are slow and consume significant disk space.
2. In college labs with slow BSNL/Jio internet, installing packages takes ages.
3. Managing virtual environments manually is confusing for freshers.
   **UV** (written in Rust by Astral) is 10-100x faster than `pip`. It acts as a single tool to install Python, create virtual environments, and run scripts instantly.

---

## 📚 Section 2: Real World Story [00:10 - 00:20 | Duration: 10 mins]

### The Canteen Bill Automation Story

Meet Rahul, a 2nd-year engineering student in Visakhapatnam. His college canteen owner, Ramesh Kaka, serves samosas, tea, and maggi to hundreds of students daily.
Ramesh Kaka tracks bills manually. During exam days, the queue is long. Ramesh Kaka gets stressed, miscalculates bills, and students get late for exams.

Rahul decides to help Ramesh Kaka. He writes a simple Python script.

1. The script asks: "What did the student eat?" and "How many?" (Input/Output).
2. It stores the price of a Samosa (₹15) and Tea (₹10) in variables.
3. If a student orders more than 5 samosas, it applies a 10% discount (Conditions).
4. If there are 10 students in a queue, it processes their bills one by one (Loops).

Ramesh Kaka now just inputs the numbers on a cheap terminal screen, and the bill is generated in 1 second. No more manual mistakes!

---

## 📚 Section 3: Beginner Explanation [00:20 - 00:30 | Duration: 10 mins]

Let's break down the concepts using everyday analogies:

### 1. Variables: The Storage Boxes

Think of a variable as a labeled steel dabba (container) in your mother's kitchen. One dabba is labeled "Sugar", another "Salt". You can change the contents inside, but the label stays the same.
In Python:

```python
sugar_amount = 5  # sugar_amount is the label, 5 is the content
```

### 2. Data Types: The Kinds of Goods

In the kitchen, sugar is solid, milk is liquid, and eggs are counted in units. You cannot pour sugar into a milk packet. Similarly, computer memory needs to know what *type* of data it is saving:

- **Integer (`int`)**: Whole numbers, e.g., number of samosas ordered (`5`).
- **Float (`float`)**: Decimal numbers, e.g., price of tea (`10.50`).
- **String (`str`)**: Text, e.g., customer name (`"Rahul"`). Always wrapped in quotes.
- **Boolean (`bool`)**: True or False, e.g., is student bill paid? (`True`).

### 3. Operators: The Calculations

How do we calculate?

- **Arithmetic:** `+` (add), `-` (subtract), `*` (multiply), `/` (divide), `%` (remainder - useful for finding even/odd numbers).
- **Comparison:** `==` (is equal?), `!=` (not equal), `>` (greater than), `<` (less than).
- **Logical:** `and` (both conditions must be true), `or` (at least one must be true), `not` (reverse the boolean).

---

## 📚 Section 4: Technical Explanation & Architecture [00:30 - 00:50 | Duration: 20 mins]

### Technical Definition

Python is an **interpreted, dynamically typed** language.

- **Interpreted:** Python code is executed line by line by the Python Interpreter. It does not need to be fully compiled into machine code before running (unlike C++).
- **Dynamically-typed:** You don't need to declare whether a variable is an `int` or `str` beforehand. Python determines it automatically at runtime.

### How Python Executes Under the Hood

```
Source Code (.py) ➔ Python Interpreter ➔ Bytecode (.pyc) ➔ Python Virtual Machine (PVM) ➔ Machine Code (0s & 1s)
```

### Virtual Environments & UV Architecture

When you install packages for different projects, they can conflict (e.g., Project A needs NumPy version 1.2, Project B needs NumPy 2.0).
A **Virtual Environment** is an isolated folder containing its own copy of the Python interpreter and packages.

- **`pip` method:** Manually create virtual environment (`python -m venv .venv`), activate it, and run `pip install`.
- **`uv` method:** UV manages everything. Run `uv run script.py` and it automatically sets up an isolated environment behind the scenes in milliseconds.

---

## 🎨 Section 5: Real World Examples [00:50 - 01:00 | Duration: 10 mins]

### Beginner Examples (Tier 2/3 City Context)

#### 1. Auto-Rickshaw Fare Calculator

* **Problem:** An auto driver in Surat charges ₹20 base fare for the first 2 km, and ₹10 per km afterwards. Calculating this manually for passengers causes arguments.
* **Solution:** A simple CLI script where the driver inputs the distance, and it computes the exact fare.
* **Technology Used:** Variable assignment, Input/Output, Arithmetic operators, Conditions.
* **Business Outcome:** Zero arguments, transparent pricing for passengers.

#### 2. College Exam Eligibility Check

* **Problem:** A college admin in Bhopal manually checks if students have > 75% attendance and have paid their fees to issue hall tickets.
* **Solution:** A Python script taking student inputs and printing eligibility status.
* **Technology Used:** Boolean variables, comparison operators, logical operators (`and`).
* **Business Outcome:** Automates verification of 1,000 students in seconds instead of 3 days.

#### 3. BSNL Broadband Data Alert

* **Problem:** A user in Kanpur has a 100GB monthly plan. They want an alert when usage exceeds 90GB.
* **Solution:** Python script tracking usage and printing a warning message.
* **Technology Used:** Float variable, input/output, conditional check.
* **Business Outcome:** Avoids heavy bill shocks at month-end.

---

### Industry Examples (Indian App Context)

#### 1. PhonePe Transaction Status Categorizer

* **Problem:** PhonePe processes millions of transactions. They need to categorize them as SUCCESS, PENDING, or FAILED, and print custom messages based on error codes.
* **Solution:** Conditional block matching incoming status codes from bank APIs.
* **Technology Used:** String manipulation, conditional branching (`if-elif-else`).
* **Business Outcome:** Fast UI updates for users, reducing customer support tickets.

#### 2. Swiggy Delivery Agent Allocation Loop

* **Problem:** A Swiggy order is placed in Nagpur. The system must notify 5 nearby delivery agents one by one until someone accepts.
* **Solution:** A loop that iterates through list of available agents and stops when acceptance status becomes `True`.
* **Technology Used:** Loops (`while`), list iteration, conditions.
* **Business Outcome:** Swift delivery partner assignment.

#### 3. IRCTC Seat Availability Lookup

* **Problem:** A passenger searches for tickets on the sleeper coach of the Nagpur-Pune Express. The system needs to accept train number and class, check seat count, and return if tickets are available.
* **Solution:** CLI simulator querying seat integers.
* **Technology Used:** Integers, variables, comparison operators.
* **Business Outcome:** Immediate response to seat search.

---

### Startup & Enterprise Examples

#### 1. Dunzo Package Delivery Status (Startup Example)

```
Problem:
  Dunzo needs to calculate delivery fee dynamically.
  Base fee is ₹40. If time is peak hour (6 PM - 9 PM), charge ₹20 extra. If rain is True, charge ₹30 extra.
Solution:
  A Python conditional script computing prices dynamically.
Technology Used:
  Python conditions, comparison operators, variables.
Business Outcome:
  Dynamic pricing handles rider availability during tough conditions automatically.
```

#### 2. TCS Automation Script (Enterprise Example)

```
Problem:
  A TCS system administrator has to generate daily server check reports for a banking client. 
  Checking 50 server logs manually takes 2 hours every morning.
Solution:
  A Python script that loops through server directory, reads status flags, and prints a summary report.
Technology Used:
  File loops, system variables, print formatting.
Business Outcome:
  Reduces human labor to 2 seconds, eliminating human errors in checking server status.
```

---

## 🎨 Section 6: Visual Diagrams [01:00 - 01:05 | Duration: 5 mins]

### Python Execution Cycle (ASCII Diagram)

```
+------------------------------------+
|        python_script.py            | (Human-readable code)
+-----------------+------------------+
                  |
                  v (Interpreter compiles to bytecode)
+-----------------+------------------+
|        python_script.pyc           | (Bytecode - platform independent)
+-----------------+------------------+
                  |
                  v (PVM executes bytecode on local CPU)
+-----------------+------------------+
|      Python Virtual Machine (PVM)  |
+-----------------+------------------+
                  |
                  v
+-----------------+------------------+
|           CPU Output               | (Calculates 2 + 2 = 4)
+------------------------------------+
```

### Dynamic Typing Memory Allocation

```
      [ Variable Label ]               [ Memory Address ]
    
      x = 10              ---------->   [ 0x1023 (Integer: 10) ]
    
      x = "Nagpur"        ---------->   [ 0x892A (String: 'Nagpur') ]
                                        *Old integer memory is cleaned up
                                         by garbage collector.
```

---

## 🎨 Section 7: Whiteboard Explanation [01:05 - 01:10 | Duration: 5 mins]

### Left Board: Variables & Memory Layout

1. Draw a grid of boxes to represent RAM (Random Access Memory).
2. Write addresses like `0x01`, `0x02`.
3. Draw an arrow from a variable named `samosa_price` to a box containing the number `15`.
4. Explain: "When we write `samosa_price = 15`, Python reserves a box in memory, stores 15 inside it, and tags it as `samosa_price`."

### Right Board: Loops vs. Conditions (Control Flow)

1. Draw a flowchart for **Conditions**:
   - Diamond Box: `Is age >= 18?`
   - Arrow Yes ➔ "Eligible for Voter ID"
   - Arrow No ➔ "Not Eligible"
2. Draw a flowchart for **Loops**:
   - Diamond Box: `Are there remaining items in the cart?`
   - Arrow Yes ➔ Process Item ➔ Loop back to Diamond
   - Arrow No ➔ Exit Loop ➔ Print Bill

---

## 💬 Section 8: Teaching Script [01:10 - 01:20 | Duration: 10 mins]

**Instructor:** "Good morning everyone! Let's start with a simple question. How many of you buy groceries or snacks on credit (*udhaari*) at your college canteen?"
*(Students raise hands, laugh)*

**Instructor:** "Awesome. How does the canteen uncle keep track of it?"

**Student:** "He writes it in a yellow notebook!"

**Instructor:** "Exactly. Now, what happens if he spills tea on that notebook? Or forgets which page you are on? He loses money, and you get a free snack! But for business, that's a disaster. Today, we are going to write a Python script that replaces that yellow notebook forever. First, let's look at variables. Think of variables as plastic containers in your kitchen. If you put rice in it, it holds rice. If you empty it and put sugar, it holds sugar. Let's write code: `canteen_balance = 150`. What data type is `150`?"

**Student:** "Integer!"

**Instructor:** "Perfect. What if your balance is `150.50`? That's a `float`. What if your name is `'Amit'`? That's a `string`. Now, let's learn how to run this code using a tool called `uv`. It is written in Rust, and it's extremely fast. Even if your lab computer has slow internet, `uv` will install Python and run your code in less than 2 seconds!"

---

## 💻 Section 9: Live Demo [01:20 - 01:40 | Duration: 20 mins]

### Demo Goal

Initialize a Python environment using `uv`, write a dynamic billing script that reads student input, applies conditions, and prints the result.

### Step-by-Step Flow

1. **Install UV:**
   Run in terminal:
   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
2. **Initialize Workspace:**
   ```bash
   uv init day1_canteen
   cd day1_canteen
   ```
3. **Write the Script (`main.py`):**
   Open `main.py` and write:
   ```python
   # Ramesh Kaka Canteen Billing System

   print("=== RAMESH KAKA CANTEEN BILLING ===")

   # Input: Get customer name and item counts
   customer_name = input("Enter student name: ")
   samosa_count = int(input("Enter number of Samosas ordered (₹15 each): "))
   tea_count = int(input("Enter number of Tea cups ordered (₹10 each): "))

   # Process: Calculations
   samosa_total = samosa_count * 15
   tea_total = tea_count * 10
   subtotal = samosa_total + tea_total

   # Condition: Special discount for bulk purchase (total > ₹100)
   discount = 0.0
   if subtotal > 100:
       discount = subtotal * 0.10  # 10% discount
       print("🎉 Special Bulk Discount of 10% applied!")

   final_bill = subtotal - discount

   # Output: Print structured invoice
   print("\n--- INVOICE ---")
   print(f"Customer Name: {customer_name}")
   print(f"Samosas x {samosa_count} : ₹{samosa_total}")
   print(f"Tea Cups x {tea_count} : ₹{tea_total}")
   print(f"Subtotal     : ₹{subtotal}")
   print(f"Discount     : ₹{discount}")
   print(f"Total Bill   : ₹{final_bill}")
   print("----------------")
   ```
4. **Run using UV:**
   ```bash
   uv run main.py
   ```

### Expected Output

```
=== RAMESH KAKA CANTEEN BILLING ===
Enter student name: Amit
Enter number of Samosas ordered (₹15 each): 6
Enter number of Tea cups ordered (₹10 each): 2

🎉 Special Bulk Discount of 10% applied!

--- INVOICE ---
Customer Name: Amit
Samosas x 6 : ₹90
Tea Cups x 2 : ₹20
Subtotal     : ₹110
Discount     : ₹11.0
Total Bill   : ₹99.0
----------------
```

---

## 💼 Section 10: Industry Use Cases [01:40 - 01:45 | Duration: 5 mins]

1. **UPI Transaction Retries:** If a payment via Google Pay fails, a `while` loop retries the transaction up to 3 times before declaring it failed.
2. **E-commerce Cart Validation:** Amazon uses conditions (`if-else`) to check if the user is a Prime Member. If True, shipping fee is set to ₹0. Else, shipping fee is ₹40.
3. **Log Monitoring Automation:** At Infosys, developers write Python loops to scan daily server log files line by line to detect errors containing the keyword "CRITICAL".

---

## ⚠️ Section 11: Common Mistakes & Fixes [01:45 - 01:50 | Duration: 5 mins]

Here are 10 common mistakes beginner Python students make:

1. **Mixing Data Types in Input:**
   - *Error:* `samosas = input("Enter count: ")` then `total = samosas * 15`. If user inputs `3`, output is `'333333333333333'` (string repetition) instead of `45`.
   - *Fix:* Explicitly cast input to integer: `int(input("Count: "))`.
2. **Missing Colons (`:`) in Conditions/Loops:**
   - *Error:* `if x > 10` (SyntaxError).
   - *Fix:* Always end conditional/loop statement headers with a colon: `if x > 10:`.
3. **Indentation Mismatch:**
   - *Error:* Mixing spaces and tabs or having inconsistent space counts inside conditional blocks.
   - *Fix:* Always use 4 spaces for indentation. Set IDE to convert tabs to spaces automatically.
4. **Single Equals vs. Double Equals:**
   - *Error:* `if x = 10:` (attempts variable assignment inside condition).
   - *Fix:* Use double equals `==` for comparison: `if x == 10:`.
5. **Infinite Loops:**
   - *Error:* `while count < 5:` without updating `count` variable. The loop runs forever, freezing the CPU.
   - *Fix:* Ensure the loop variable changes within the block (e.g. `count += 1`).
6. **String Concatenation Error:**
   - *Error:* `print("Total is: " + bill_amount)` where `bill_amount` is a float. Throws `TypeError: can only concatenate str (not "float") to str`.
   - *Fix:* Use f-strings: `print(f"Total is: {bill_amount}")`.
7. **`uv` script executing wrong python version:**
   - *Error:* System default Python is old (e.g. 3.8) and doesn't support modern f-string syntax features.
   - *Fix:* Set python version in `pyproject.toml` or let uv download it: `uv run --with python@3.12 main.py`.
8. **Modifying loop variable during list iteration:**
   - *Error:* Trying to delete elements from a list while iterating over it. Causes skipped items.
   - *Fix:* Iterate over a copy of the list or use list comprehensions.
9. **Index Error in loops:**
   - *Error:* Accessing index `length` of a list (remember list indices start at 0, so last index is `length - 1`).
   - *Fix:* Use `for item in list` instead of manual index loops wherever possible.
10. **Using reserved keywords as variable names:**
    - *Error:* `int = 5` or `class = "Math"`. Overwrites built-in functions.
    - *Fix:* Never use keywords (`class`, `def`, `int`, `str`, `import`) as variables.

---

## 📋 Section 12: Interview Questions & Answers [01:50 - 01:55 | Duration: 5 mins]

### Beginner Level (10 Questions)

1. **What is the difference between `/` and `//` operators in Python?**
   - *Answer:* `/` performing normal division returns a float (e.g. `5 / 2 = 2.5`). `//` is floor division, which rounds down to the nearest integer (e.g. `5 // 2 = 2`).
2. **What does the `%` operator do?**
   - *Answer:* It is the modulo operator, which returns the remainder of a division (e.g. `7 % 3 = 1`).
3. **Is Python statically typed or dynamically typed?**
   - *Answer:* Dynamically typed. You don't need to specify variable types; they are checked at runtime.
4. **How do you convert a string `"100"` to an integer?**
   - *Answer:* Using `int("100")`.
5. **What is an f-string in Python?**
   - *Answer:* It is a way to format strings by embedding variables directly inside braces (e.g. `f"Hello {name}"`).
6. **What is the difference between `input()` in Python 2 vs Python 3?**
   - *Answer:* In Python 3, `input()` always returns a string. In Python 2, it executed the input as code (deprecated).
7. **What is a syntax error? Give an example.**
   - *Answer:* An error where the code violates Python's writing rules, such as `if x > 5` (missing colon).
8. **How do you write comments in Python?**
   - *Answer:* Use `#` for single-line comments, or triple quotes `"""` for docstrings.
9. **What are the rules for writing Python variable names?**
   - *Answer:* Must start with a letter or underscore, cannot start with a number, and cannot contain spaces or special characters except `_`.
10. **What is the default return type of the `input()` function?**
    - *Answer:* Always a string (`str`).

### Intermediate Level (10 Questions)

11. **Explain the short-circuit evaluation of logical operators `and` / `or`.**
    - *Answer:* For `and`, if the first condition is False, the second is not evaluated. For `or`, if the first condition is True, the second is not evaluated.
12. **Why is `uv` faster than `pip`?**
    - *Answer:* `uv` is written in Rust, resolves dependencies concurrently, and uses global caches (linking instead of copying packages).
13. **What is bytecode in Python?**
    - *Answer:* A low-level representation of source code compiled by the interpreter to run on the Python Virtual Machine (PVM).
14. **How do you generate a sequence of numbers from 1 to 10 using loops?**
    - *Answer:* `for i in range(1, 11):`.
15. **What is the difference between `=` and `==`?**
    - *Answer:* `=` assigns a value to a variable, while `==` compares two values for equality.
16. **How does Python handle memory management?**
    - *Answer:* Through private heaps, reference counting, and an automatic garbage collector that deletes unused objects.
17. **What happens if you check `True or False and False`?**
    - *Answer:* Returns `True`. `and` has higher precedence than `or`, so it evaluates `False and False` first (returns `False`), then `True or False` (returns `True`).
18. **What is the purpose of virtual environments?**
    - *Answer:* To isolate project dependencies so that package updates in one project do not break another.
19. **How does `uv run` work without manual activation of a virtual environment?**
    - *Answer:* It inspects the script's inline metadata or project config, prepares a temp environment, installs dependencies, and runs the script in that sandbox.
20. **Can you change the value of a variable once it is created?**
    - *Answer:* Yes, Python variables are just labels pointing to memory. You can point the label to a new value.

### Advanced Level (10 Questions)

21. **Explain Python's GIL (Global Interpreter Lock).**
    - *Answer:* A mutex that prevents multiple native threads from executing Python bytecodes at once, ensuring thread safety but limiting multi-core CPU utilization in CPU-bound tasks.
22. **What is the difference between dynamic typing and duck typing?**
    - *Answer:* Dynamic typing means type checks occur at runtime. Duck typing is a style where an object's suitability is determined by the presence of certain methods/properties rather than inheritance.
23. **How does `range()` save memory compared to a list of numbers?**
    - *Answer:* `range()` returns a lazy iterable sequence object that generates numbers on-demand rather than allocating a full list in RAM.
24. **How does `uv` manage global cache synchronization on Windows?**
    - *Answer:* By using content-addressed caches and hard links/reflinks where supported by the file system, avoiding redundant writes.
25. **What is the difference between `is` and `==` in Python?**
    - *Answer:* `==` checks for equality of value, while `is` checks for identity (if two variables point to the exact same object in memory).
26. **Explain how Python executes an `else` block after a `for` loop.**
    - *Answer:* The `else` block runs only if the loop completes all iterations without encountering a `break` statement.
27. **What is PEP 8? Name 3 core styling conventions.**
    - *Answer:* Python's official style guide. Conventions: Use 4 spaces for indentation, limit lines to 79 characters, separate functions with two blank lines.
28. **Explain the behavior of `sys.argv` for command-line arguments.**
    - *Answer:* A list containing command-line arguments passed to the script, where `sys.argv[0]` is always the script name itself.
29. **What is dynamic scoping vs lexical scoping? Which does Python use?**
    - *Answer:* Python uses lexical (static) scoping, meaning variable resolution is determined by the location of variables within the nested source code block structure.
30. **How does Python's Garbage Collection handle reference cycles?**
    - *Answer:* In addition to reference counting, Python uses a cyclic garbage collector that periodically detects groups of unreachable objects referencing each other using a double-linked list traversal.

---

## ❓ Section 13: FAQs [01:55 - 01:58 | Duration: 3 mins]

**Q: Do I need a high-end laptop to run Python and UV?**
**A:** No. Python and UV can easily run on a dual-core laptop with 4GB RAM. Since `uv` is written in Rust, it uses minimal memory and CPU resources.

**Q: Why should I use UV if I can just write scripts online in Google Colab?**
**A:** Colab is great for playing with data, but you cannot build production software, deploy local bots, or handle direct computer hardware/APIs from it. Real software engineers build locally.

**Q: What is the difference between `float` and `double` in Python?**
**A:** In Python, there is no `double` type. Python's `float` is internally represented as a double-precision 64-bit float (similar to `double` in C++ or Java).

---

## 📋 Section 14: Assignment Brief [01:58 - 02:00 | Duration: 2 mins]

### Scenario

You are hired as a Junior Software Engineer at a fast-growing local tech agency in Coimbatore. The agency wants to build simple, interactive console utilities that can be deployed to kiosks in schools and shops.

### Objectives & Deliverables

Build a consolidated CLI suite containing:

1. **Interactive Calculator:** Basic operations with division error handling.
2. **Number Guessing Game:** Compares guess with target number and tracks guess count.
3. **Student Grade Analyzer:** Computes average score for 3 subjects and assigns a division/grade.

Refer to [04_Assignment.md](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day1_Python_Fundamentals/Day1_Teaching_content/04_Assignment.md) for full specs.

---

## 📋 Section 15: Assignment Solution Architecture

### Folder Structure

```
day1_assignment/
├── pyproject.toml
└── src/
    └── main.py
```

### Best Practices for Solutions

- Use f-strings for formatted printing.
- Always cast string inputs to numeric types before math operations.
- Catch division-by-zero errors (`ZeroDivisionError` or using conditions `if operand == 0`).
