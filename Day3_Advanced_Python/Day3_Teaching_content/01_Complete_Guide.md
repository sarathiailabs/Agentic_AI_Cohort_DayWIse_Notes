# 📖 Day 3 Complete Guide: Advanced Python (OOP, Exception Handling & File Handling)

## Master Reference Document

**Day:** 3 of 20
**Topic:** Advanced Python: OOP, Exception Handling, and File I/O
**Duration:** 2 Hours (120 Minutes)
**Difficulty Level:** Intermediate
**Prerequisites:** Day 2 (Functions, Lists, Tuples, Sets, Dictionaries)

---

## 🎯 Executive Summary

Welcome to Day 3 of the AI Engineer & Agentic AI Engineer Bootcamp. Today, we transition from functional programming to **Object-Oriented Programming (OOP)**, and learn how to handle operational hazards using **Exception Handling** and store persistent data using **File Handling**.

In the AI and Agentic AI landscape, these three pillars are fundamental:

1. **OOP:** AI Agents are represented as classes with states, memory, and tools as methods.
2. **Exception Handling:** LLM calls fail, rate limits are hit, and network requests time out. Graceful recovery keeps agents from crashing.
3. **File Handling:** Agents must read local system files, write execution logs, load prompt templates, and store state memory permanently in files.

Today's session is designed to make students build bulletproof, persistent, and structured Python systems.

---

## 📅 2-Hour Session Timing and Timeline

| Time Slot | Elapsed Time  | Duration | Section / Focus           | Description                                                                                             |
| --------- | ------------- | -------- | ------------------------- | ------------------------------------------------------------------------------------------------------- |
| 1         | 00:00 - 00:10 | 10 mins  | Intro & Recap             | Recap Day 2 (Data structures) and launch Day 3 Problem Statement                                        |
| 2         | 00:10 - 00:30 | 20 mins  | Conceptual & Story        | Warehouse Inventory Chaos Story, Blueprints/Safety nets/File Cabinets                                   |
| 3         | 00:30 - 00:50 | 20 mins  | Technical & Architecture  | Memory layout of instances, Class vs Instance variables, Dunder hooks, Exception stack, File IO buffers |
| 4         | 00:50 - 01:10 | 20 mins  | Whiteboard & Interaction  | Class Memory maps, Exception propagation trees, and interactive Q&A                                     |
| 5         | 01:10 - 01:40 | 30 mins  | Live Coding & Practice    | Step-by-step walkthrough of OOP models, try-except pipelines, and JSON files                            |
| 6         | 01:40 - 01:55 | 15 mins  | Industry Context & Review | Real-world ORMs, crawler exceptions, 10 traps, FAQs, and 30 interview questions                         |
| 7         | 01:55 - 02:00 | 5 mins   | Assignment & Wrap-up      | Intro to Library Management System CLI Assignment and rubric details                                    |

> [!TIP]
> **Pacing Reminder:** If students find inheritance and polymorphism confusing, use the simple "Shape -> Circle/Square" or "Employee -> Manager/Developer" analogy. Don't let them get bogged down in multiple inheritance syntax; keep it focused on single inheritance which covers 95% of real-world AI coding.

---

## 📚 Section 1: Problem Statement [00:00 - 00:10 | Duration: 10 mins]

### What problems exist in flat, functional, and volatile systems?

1. **State and Action Disconnect:** As code grows, you have variables storing data (e.g., `user_balance`) and separate functions performing calculations (e.g., `deduct_money(user_id, amount)`). If they are completely disconnected, another function can accidentally corrupt `user_balance` without going through your validation rules. We need a way to wrap data and actions together.
2. **Fragile Runs (Crashes):** If you ask a user for their age, and they type `"twenty"`, python attempts `int("twenty")` and instantly crashes with a `ValueError`. In production, a server crashing because of user input is unacceptable. We need safety nets to catch errors, report them, and continue running.
3. **Amnesia (Data Volatility):** When your Python script finishes running, all variables, lists, and dictionaries in RAM disappear. If Ramesh Kaka restarts his billing system, all registered customers and transaction credits are deleted. We need **permanent storage** on a hard drive using files.

### Why OOP, Exceptions, and Files Solve This:

- **OOP:** Combines data (attributes) and behavior (methods) into a single logical unit called a **Class**. It encapsulates state, inherits shared logic, and hides implementation details.
- **Exception Handling:** Uses `try-except-finally` blocks to intercept runtime errors, handle them gracefully, clean up resources, and keep the application alive.
- **File Handling:** Lets Python open, read, edit, write, and close physical files (text, CSV, JSON) on the local drive, turning volatile variables into permanent data.

---

## 📚 Section 2: Real World Story [00:10 - 00:20 | Duration: 10 mins]

### The Surat Saree Warehouse Automation Story

Meet Prakash, who runs "Surat Saree Emporium," a massive warehouse distributing sarees to 500+ retailers.

Prakash used to track inventory on a paper log register.

- **The OOP Problem:** Each saree has a design code, fabric type, price, and stock count. Prakash's staff kept mixing up variable columns. They needed a **Saree Blueprint (Class)** where every single saree is an **instance (Object)** containing its own unique attributes (`design_code`, `fabric`, `price`) and operations (`add_stock()`, `sell_item()`).
- **The Exception Problem:** Prakash built a basic Python script for staff to scan barcodes. Sometimes, the scanner read corrupt characters or a database lookup failed. The script would crash, halting the warehouse queue of delivery trucks. Prakash needed **Exception Handling** to intercept these errors: if a barcode read failed, log it as a warning, sound a buzzer, and ask the worker to scan again without crashing the entire terminal.
- **The File Handling Problem:** When the warehouse power tripped, the computer rebooted, and the script lost all registered transactions. They needed **File Handling** to save every single scan instantly to an `inventory.json` file. When the script rebooted, it read the file and restored the exact warehouse state.

Prakash's warehouse now processes 10,000 sarees daily. The system never crashes, memory is preserved across power cuts, and the warehouse logic is clean and structured.

---

## 📚 Section 3: Beginner Explanation [00:20 - 00:30 | Duration: 10 mins]

Let's explain these concepts using simple, everyday analogies:

### 1. Classes & Objects: The Cake Mould and Cakes

Think of a **Class** as a **Silicone Cake Mould**.

- The mould itself is not a cake. It is just the design, shape, and structure.
- An **Object** is the actual **Cake** baked using that mould. You can pour chocolate batter (chocolate cake object) or vanilla batter (vanilla cake object).
- Each cake has its own taste and color (attributes), but they all share the exact same round shape (class structure).

### 2. The Four Pillars of OOP

- **Encapsulation (The Capsule):** Like a paracetamol medicine capsule. The bitter chemical powder is hidden inside a sweet gelatin cover. You consume the capsule without tasting the bitter chemicals. In coding, we hide complex data variables inside a class and let the user access them only via public methods (e.g., `get_balance()`).
- **Inheritance (Family Traits):** A child inherits the eyes or nose shape of their parents, but has their own unique traits too. Similarly, a class `Car` inherits features from class `Vehicle` (steering, wheels) but adds its own (AC, air-bags).
- **Polymorphism (Many Forms):** Think of a laptop's **Power Button**. Press it when the laptop is off, it boots up. Press it when the laptop is on, it shows a sleep menu. The same button performs different actions based on context. In Python, different objects can have a method with the same name (`speak()`) but execute it differently (Dog: "Woof", Cat: "Meow").
- **Abstraction (The Car Dashboard):** When you drive a car, you press the accelerator pedal. You do not care how the engine injects fuel, how pistons move, or how the drive shaft rotates. The pedal is the abstraction layer. You interact with the simple interface, while the complex mechanics are hidden away.

### 3. Exception Handling: The Household Safety Fuse

In your house, if there is a sudden high voltage surge, the **safety fuse/MCB** trips, cutting off the electricity. It saves your expensive TV and refrigerator from blowing up.
`try-except` blocks are the safety fuses of Python. If a division-by-zero or missing file error occurs, instead of destroying your running program, the execution "trips" into the `except` block, logs the error, resets variables, and continues running safely.

### 4. File Handling: The Steel Filing Cabinet

Think of RAM (variables) as your **office study desk**. It holds files you are actively looking at. But when you leave for the night, the desk is wiped clean.
Think of File Handling as opening a **Steel Filing Cabinet** (hard drive). You open a drawer (`open("file.txt")`), read a document (`read()`), write notes on a paper (`write()`), and lock the cabinet (`close()`). The documents stay there safe forever.

---

## 📚 Section 4: Technical & Architecture [00:30 - 00:50 | Duration: 20 mins]

### Deep Dive: Python Object Instantiation & Memory Layout

```
                        RAM (Random Access Memory)
        Heap Memory                                 Stack Memory
        +-----------------------------------+       +--------------------+
        | Class: Saree                      |       | main thread        |
        | - methods: __init__, sell_item    |       |                    |
        +-----------------------------------+       |                    |
        |                                   |       |                    |
        | Object Instance: silk_saree       |<======| silk_saree pointer |
        | - design_code = "SILK-001"        |       +--------------------+
        | - price = 1200.0                  |       |                    |
        | - __class__ points to Class Saree |       |                    |
        +-----------------------------------+       +--------------------+
```

1. **Object Creation Cycle:**
   - When you call `silk_saree = Saree("SILK-001", 1200)`, Python executes `__new__()` to allocate raw memory for the object.
   - Then, it triggers `__init__()` (the initializer) to bind attributes (`design_code`, `price`) to the instance.
   - The variable `silk_saree` on the **Stack** holds a reference pointer to the actual object data residing on the **Heap**.
2. **Class vs. Instance Variables:**
   - **Instance variables:** Bound to `self`. Each object holds its own independent values. Modifying `silk_saree.price` does not affect `cotton_saree.price`.
   - **Class variables:** Declared directly inside the class body, shared by all instances. Useful for configuration constants (e.g., `GST_RATE = 0.05`). If modified, the change applies to all instances.
3. **Dunder Methods (Magic Hooks):**
   - Python classes use double-underscore methods (dunder) to interface with built-in functions.
   - `__str__(self)`: Hooks into `print(object)` to return a user-friendly string description.
   - `__repr__(self)`: Hooks into debug consoles to return a detailed developer-oriented description.
   - `__eq__(self, other)`: Hooks into `==` comparisons to define what makes two objects equal.

---

### Technical Architecture of Exceptions

When an error occurs, Python halts code execution and creates an **Exception Object** containing traceback details.

- **Propagation:** If an error occurs inside a function, and there is no `try-except` block there, Python pops the current execution frame off the stack and looks for a handler in the calling function. It propagates up the call stack. If it hits the top-level global frame without being caught, Python prints the traceback and exits.
- **The `finally` guarantee:** The block of code inside `finally` is guaranteed to execute *even if an exception was raised, caught, or if the function returned early*. This is critical for closing databases, network sockets, or files.

---

### File IO Buffers and Context Managers

- **File Buffering:** When you write data using `file.write()`, Python does not write directly to the hard drive immediately. It writes to a temporary **memory buffer** to save slow disk write cycles.
- **Flushing:** The data is pushed to the disk only when the buffer is full, when `file.flush()` is called, or when the file is closed using `file.close()`.
- **Context Managers (`with` block):** Under the hood, using `with open("data.txt", "w") as f:` triggers Python's context manager protocol:
  1. Calls `f.__enter__()`, which opens the file and assigns it to `f`.
  2. Executes the code block inside.
  3. Automatically calls `f.__exit__()` at the end of the block, which flushes buffers and closes the file descriptor, even if an unhandled crash occurs inside the block.

---

## 🎨 Section 5: Real World Examples [00:50 - 01:00 | Duration: 10 mins]

### Beginner Examples

#### 1. Bank Account Class (OOP Basics & Encapsulation)

* **Problem:** Storing account balance as a plain integer allows developers to set negative balances like `balance = -500` directly, corrupting database integrity.
* **Solution:** Encapsulate balance inside a class with `__balance` and force modifications through a `withdraw()` method containing checks.
* **Technology:** Class syntax, Private attributes (double underscore), methods.

#### 2. Safe User Registration Calculator (Exceptions)

* **Problem:** A script asks a user to enter their age. If they type `"abc"`, the script crashes.
* **Solution:** Wrap `int(input())` in a `try-except ValueError` loop. Keep asking until a valid number is supplied.
* **Technology:** Exception loops, `ValueError`.

#### 3. Daily Visitor Counter Log (File I/O)

* **Problem:** A retail shop wants to count total daily entries. If they reboot the system, the count drops back to zero.
* **Solution:** Write the count to a local `counter.txt` file. Increment the number in the file whenever a visitor logs in.
* **Technology:** File read (`r`) and write (`w`) modes.

---

### Industry Examples

#### 1. Zomato Delivery Partner Classes (Inheritance & Polymorphism)

* **Problem:** Zomato has different classes of delivery agents: Cycle riders, Auto drivers, and Bike riders. Each has a different speed and payout rate. Writing flat `if-else` loops for every dispatcher action is unmaintainable.
* **Solution:** Base class `DeliveryPartner` with subclass overrides `CyclePartner`, `BikePartner` implementing customized `calculate_trip_time()` and `calculate_payout()` methods.
* **Technology:** OOP Inheritance, Polymorphism.

#### 2. PhonePe API Gateway Retries (Exception Boundaries)

* **Problem:** Bank servers fail or timeout frequently. PhonePe cannot crash when a bank network is down.
* **Solution:** Wrap the bank transaction API request in a `try` block. Catch `TimeoutError` or `ConnectionError`, log it, and trigger an automatic routing fallback to a secondary server in the `except` block.
* **Technology:** Nested try-except, Network timeout exceptions.

#### 3. IRCTC Daily Bookings CSV Exporter (File I/O)

* **Problem:** IRCTC needs to compile a spreadsheet report of daily tickets booked in Nagpur.
* **Solution:** Write customer booking objects to a `.csv` file using Python's structured `csv` module, writing header lines and rows.
* **Technology:** Structured CSV writing, file context managers.

---

### Startup & Enterprise Examples

#### 1. Dunzo Order State Machine (OOP State Management)

```
Problem:
  Dunzo needs to manage an order's lifecycle: PLACED ➔ PARTNER_ASSIGNED ➔ PICKED_UP ➔ DELIVERED.
  Accidentally moving an order from PLACED directly to DELIVERED must be blocked.
Solution:
  A class `DunzoOrder` keeping state in a private attribute.
  Methods like `assign_partner()`, `pickup()`, and `deliver()` enforce validation rules, throwing exceptions if transition rules are violated.
Technology Used:
  Private attributes, custom state checks, enum tracking.
Business Outcome:
  Guarantees order lifecycle compliance across microservices.
```

#### 2. TCS Enterprise Log Rotation Tool (File Handling & Exception Traps)

```
Problem:
  A client server runs out of disk space because of massive daily log files. 
  TCS needs an automated script to open log files, read contents, compress older entries, and delete original files safely, even if a log file is currently locked by a running process.
Solution:
  A Python log rotation system that wraps system I/O operations in exceptions.
  If a `PermissionError` is thrown (file locked), it skips that file, writes a warning to a master log, and cleans up buffers.
Technology Used:
  File directory scanning (`os.walk`), context managers, PermissionError handling.
Business Outcome:
  System runs 24/7 without crashing due to file lock contention.
```

---

## 🎨 Section 6: Visual Diagrams [01:00 - 01:05 | Duration: 5 mins]

### OOP Pillars: Unified Visual Layout

```
+-------------------------------------------------------------+
|                     CLASS: BankAccount                      |
|                                                             |
|  [ Encapsulation ]                                          |
|  - Private variable: __balance (Hidden from direct access)  |
|  - Public methods: deposit(), withdraw()                    |
|                                                             |
|  [ Abstraction ]                                            |
|  - Method: calculate_interest()                             |
|    (Hides complex bank formulas; user just calls method)    |
+-------------------------------------------------------------+
                              |
                              v (Inheritance)
+-------------------------------------------------------------+
|                 SUBCLASS: SavingsAccount                    |
|                                                             |
|  - Inherits: deposit(), withdraw()                          |
|  - Adds: check_minimum_balance()                            |
|  - Overrides (Polymorphism): calculate_interest()           |
|    (Applies custom 4% interest rate instead of standard)    |
+-------------------------------------------------------------+
```

### Try-Except-Finally Lifecycle Stack

```
[ Start Block ]
       │
       ▼
┌──────────────┐
│  Try Block   │ ──(Error Occurs)──> ┌───────────────┐
└──────────────┘                     │ Except Block  │
       │                             └───────────────┘
       │                                     │
(No Error Occurs)                            │
       │                                     │
       ▼                                     ▼
┌──────────────┐                     ┌───────────────┐
│  Else Block  │                     │ Error Handled │
└──────────────┘                     └───────────────┘
       │                                     │
       └──────────────────┬──────────────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │  Finally Block  │  <-- ALWAYS runs (e.g., file.close())
                 └─────────────────┘
                          │
                          ▼
                  [ Next Line of Code ]
```

---

## 🎨 Section 7: Whiteboard Explanation [01:05 - 01:10 | Duration: 5 mins]

### Left Board: Class vs Object Reference Maps

1. Draw a Box labeled "Class Blueprint: `Book`". Inside, write `title`, `author`, `is_borrowed = False`.
2. Draw two memory boxes in "Heap Space" at address `0x32A4` and `0x89D2`.
3. Draw an arrow from pointer variable `book1` on Stack to `0x32A4` containing: `title="Python 101"`, `author="Guido"`.
4. Draw an arrow from pointer variable `book2` on Stack to `0x89D2` containing: `title="Git Guide"`, `author="Linus"`.
5. Explain: "Both books share the Class `Book` template, but modifying `book1.is_borrowed = True` ONLY changes the flag in box `0x32A4`. The box at `0x89D2` remains untouched. They are completely separate instances."

### Right Board: File Handling Lifecycle

1. Draw a physical disk platter labeled "Hard Drive (file.txt)".
2. Draw a pipe labeled "File Descriptor / Buffer".
3. Draw a box in the middle labeled Python script.
4. Show:
   - `open(..., "w")`: Python allocates a buffer pipe connecting the script to the disk.
   - `write("data")`: Pushes text into the buffer (still in RAM).
   - `close()` or exiting `with` block: Triggers a flush, squeezing the buffer data into the physical disk, and severs the pipe link.
5. Explain: "If you don't call `close()` or use `with`, the pipe stays open, the data might stay trapped in the buffer, and other programs cannot access the file because it is locked."

---

## 💬 Section 8: Teaching Script [01:10 - 01:20 | Duration: 10 mins]

**Instructor:** "Good morning! Imagine you are building a system for a bank. You store the user's name as a string and their balance as an integer. Let's say `user_balance = 500`. Now, what happens if another developer joins your team, writes a function, and accidentally does: `user_balance = -999999`? Does Python stop them?"

**Student:** "No, it's just a variable. Python will allow it."

**Instructor:** "Exactly. Python doesn't care! But the bank is now bankrupt because of a typo. This is where **Object-Oriented Programming** saves us. We create a Class `BankAccount`. We hide the balance variable inside it so no one can access it directly. We declare it as a private variable by adding two underscores: `__balance`. If anyone tries to do `account.__balance = -500`, Python will throw an error. They are *forced* to use our public function `withdraw()`, which checks if they have enough money first. This is called **Encapsulation**."

**Student:** "But what happens if a user inputs something bad when calling our function, like a string instead of a number?"

**Instructor:** "Ah! If they type `"five hundred"`, python throws a `ValueError` and the script crashes. The ATM screen would go black. That is where we build safety nets using `try-except` blocks. Think of it as a fuse in your house. If the fuse trips, the lights go out, but your house doesn't catch fire. In Python, we catch the `ValueError`, print a clean message to the screen: `'Please enter numbers only!'`, and loop back to ask again. The ATM stays alive.

Now, what if the ATM loses power? The customer's balance stored in our program is in RAM, so it vanishes. How do we keep it permanent?"

**Student:** "We save it to the hard drive in a file!"

**Instructor:** "Spot on! We write it to a file, like `balance.txt` or `ledger.json`. When the computer boots back up, we read the file and reload the balance. Today, we will combine these three tools to build a robust, crash-proof, permanent command-line program. Let's jump into the code!"

---

## 💻 Section 9: Live Demo [01:20 - 01:40 | Duration: 20 mins]

### Demo Goal

Initialize a project using `uv`. Write a python script defining an OOP hierarchy, implementing custom exceptions, wrapping inputs in try-except statements, and reading/writing transaction logs to a persistent JSON file.

### Step-by-Step Flow

1. **Initialize workspace:**
   ```bash
   uv init day3_demo
   cd day3_demo
   ```
2. **Write the Script (`main.py`):**
   ```python
   import json
   import os

   # 1. Custom Exceptions
   class InsufficientFundsError(Exception):
       """Raised when account balance is less than withdrawal amount."""
       pass

   class NegativeAmountError(Exception):
       """Raised when a user inputs a negative value for transaction."""
       pass

   # 2. Base Class: Account
   class Account:
       def __init__(self, owner: str, balance: float = 0.0):
           self.owner = owner
           # Encapsulation: Private balance attribute
           self.__balance = balance

       def get_balance(self) -> float:
           return self.__balance

       def deposit(self, amount: float):
           if amount <= 0:
               raise NegativeAmountError("Deposit amount must be positive!")
           self.__balance += amount

       def withdraw(self, amount: float):
           if amount <= 0:
               raise NegativeAmountError("Withdrawal amount must be positive!")
           if amount > self.__balance:
               raise InsufficientFundsError(
                   f"Attempted to withdraw ₹{amount} but balance is ₹{self.__balance}"
               )
           self.__balance -= amount

       # Dunder method for easy printing
       def __str__(self) -> str:
           return f"Account of {self.owner} | Balance: ₹{self.__balance:.2f}"

   # 3. Subclass: SavingsAccount (Inheritance & Polymorphism)
   class SavingsAccount(Account):
       def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.04):
           super().__init__(owner, balance)
           self.interest_rate = interest_rate

       # Polymorphic behavior: adds interest calculation details to string
       def __str__(self) -> str:
           return f"Savings {super().__str__()} (Interest: {self.interest_rate * 100}%)"

   # 4. Persistence Controller (File I/O)
   DB_FILE = "accounts_db.json"

   def load_accounts() -> dict:
       if not os.path.exists(DB_FILE):
           return {}
       try:
           with open(DB_FILE, "r") as file:
               return json.load(file)
       except (json.JSONDecodeError, IOError) as e:
           print(f"⚠️ Error reading database file: {e}. Starting fresh.")
           return {}

   def save_accounts(data: dict):
       try:
           with open(DB_FILE, "w") as file:
               json.dump(data, file, indent=4)
       except IOError as e:
           print(f"❌ Critical: Failed to write to disk: {e}")

   # 5. Live Demo Execution Block
   def run_bank_demo():
       print("=== WELCOME TO THE COIMBATORE BANK SYSTEM ===")
       accounts_data = load_accounts()

       # Input gathering with exception safety
       owner_name = input("Enter your name: ").strip()
       if not owner_name:
           owner_name = "Guest User"

       # Check if account already exists in JSON database
       initial_balance = 0.0
       if owner_name in accounts_data:
           initial_balance = accounts_data[owner_name]
           print(f"Welcome back, {owner_name}! Loaded existing balance: ₹{initial_balance:.2f}")
       else:
           print(f"New user detected. Creating account for {owner_name}.")

       user_acc = SavingsAccount(owner=owner_name, balance=initial_balance)

       while True:
           print("\n--- MENU ---")
           print("1. View Account Summary")
           print("2. Deposit Money")
           print("3. Withdraw Money")
           print("4. Save & Exit")
           choice = input("Enter choice (1-4): ").strip()

           if choice == "1":
               print(user_acc)

           elif choice == "2":
               try:
                   amount = float(input("Enter deposit amount: ₹"))
                   user_acc.deposit(amount)
                   print(f"🎉 Successfully deposited! New Balance: ₹{user_acc.get_balance():.2f}")
               except ValueError:
                   print("❌ Error: Invalid input! Please enter a valid decimal number.")
               except NegativeAmountError as nae:
                   print(f"❌ Transaction Rejected: {nae}")

           elif choice == "3":
               try:
                   amount = float(input("Enter withdrawal amount: ₹"))
                   user_acc.withdraw(amount)
                   print(f"💸 Successfully withdrew! Remaining Balance: ₹{user_acc.get_balance():.2f}")
               except ValueError:
                   print("❌ Error: Invalid input! Please enter a valid decimal number.")
               except (NegativeAmountError, InsufficientFundsError) as transaction_error:
                   print(f"❌ Transaction Rejected: {transaction_error}")

           elif choice == "4":
               # Save data to persistent JSON file
               accounts_data[user_acc.owner] = user_acc.get_balance()
               save_accounts(accounts_data)
               print("💾 Data saved successfully. Thank you for banking with us!")
               break
           else:
               print("⚠️ Invalid choice. Select 1 to 4.")

   if __name__ == "__main__":
       run_bank_demo()
   ```
3. **Run using UV:**
   ```bash
   uv run main.py
   ```

---

## 💼 Section 10: Industry Use Cases [01:40 - 01:45 | Duration: 5 mins]

### 1. Django & SQLAlchemy ORMs (OOP Mapping)

In modern web frameworks, SQL database tables are mapped directly to Python classes. An instance of a class `User` represents a single row in the database. Calling `user.save()` triggers the ORM to convert the object attributes into SQL queries behind the scenes.

### 2. Web Crawlers and AI Scraping Logs (Exceptions)

Enterprise scrapers parse thousands of URLs. If a website blocks requests, or a tag is missing, the scraper would crash. Tech companies wrap crawling blocks in `try-except ConnectionError` structures, logging failures to a log file while letting the scraping engine skip to the next URL.

### 3. API Prompt Config Loaders (File I/O)

AI models (such as GPT-4 or Gemini) require system prompts. In production, these system prompts are not hard-coded. Instead, they are stored in text or JSON files (`system_prompt.json`). The Python backend opens and reads these files at startup, injecting the prompt templates into the API request payload.

---

## ⚠️ Section 11: Common Mistakes & Fixes [01:45 - 01:50 | Duration: 5 mins]

### 1. Modifying Shared Class variables instead of Instance variables

- *Error:*
  ```python
  class Agent:
      skills = [] # Class variable shared by ALL agents
  agent1 = Agent(); agent1.skills.append("web_search")
  agent2 = Agent()
  print(agent2.skills) # Prints ['web_search'] - Leak!
  ```
- *Fix:* Define instance attributes inside `__init__()`:
  ```python
  class Agent:
      def __init__(self):
          self.skills = [] # Unique to each instance
  ```

### 2. Catching ALL Exceptions with a Blank `except:` (Naked Except)

- *Error:*
  ```python
  try:
      x = float(input())
  except: # Swallows keyboard interrupt (Ctrl+C), syntax, and name errors
      print("Error occurred")
  ```
- *Fix:* Specify the target exception class:
  ```python
  try:
      x = float(input())
  except ValueError:
      print("Invalid number format")
  ```

### 3. Forgetting to Close Files (Leaking File Descriptors)

- *Error:* Opening files manually without using the context manager hook can lock files on Windows systems and block edits.
  ```python
  file = open("data.txt", "w")
  file.write("Hello")
  # If code crashes here, file is never closed!
  ```
- *Fix:* Always use context managers (`with` statements):
  ```python
  with open("data.txt", "w") as file:
      file.write("Hello")
  ```

### 4. Forgetting `self` in Class Methods

- *Error:*
  ```python
  class Cat:
      def meow(): # Missing self parameter
          print("Meow")
  cat = Cat(); cat.meow() # Throws TypeError
  ```
- *Fix:* Always pass `self` as the first argument to instance methods:
  ```python
  class Cat:
      def meow(self):
          print("Meow")
  ```

### 5. Attempting to Read a File in Write Mode ("w")

- *Error:* Opening a file with `open("data.txt", "w")` and trying to run `file.read()`. Write mode clears the file instantly, deleting old data, and crashes when read is called.
- *Fix:* Use `r` for reading, `w` for overwriting, `a` for appending, and `r+` for reading and writing.

### 6. Calling `super()` without parentheses

- *Error:* Calling `super.__init__()` inside subclass constructors.
- *Fix:* Always add execution parentheses: `super().__init__()`.

### 7. Over-nesting Try Blocks

- *Error:* Having nested, multi-level try-except blocks that make debugging trackback errors impossible.
- *Fix:* Break logical actions into independent functions, each handling its own isolated errors.

### 8. Appending JSON directly instead of deserializing first

- *Error:* Opening a JSON file in `"a"` (append) mode and executing `file.write(json_string)`. This breaks JSON syntax formats, resulting in multiple root entries.
- *Fix:* Read the file contents, deserialize to list/dict using `json.load()`, append/edit data, and rewrite using `json.dump()`.

### 9. Swallowing Exceptions without Logging

- *Error:* Catching exceptions with `except Exception: pass`. If a bug occurs, there is no traceback output, leaving developers blind in production.
- *Fix:* Print the error string or use Python's built-in logging module to write details to trace logs: `except Exception as e: print(f"Warning: {e}")`.

### 10. Accessing private variables directly

- *Error:* Accessing `account.__balance` outside of a class wrapper. This throws an `AttributeError` due to name mangling (`_ClassName__balance`).
- *Fix:* Implement public getter methods (`get_balance()`) to view properties.

---

## 📋 Section 12: Interview Questions & Answers [01:50 - 01:55 | Duration: 5 mins]

### Beginner Level (10 Questions)

1. **What is the difference between a class and an object?**
   - *Answer:* A class is a blueprint or template defining variables and methods. An object is a concrete instance of that class allocated in memory.
2. **What is the purpose of the `__init__` method in Python?**
   - *Answer:* It acts as the initializer method. It is called automatically when an object is instantiated, binding initial parameters to the object's instance variables.
3. **What does the `self` keyword represent?**
   - *Answer:* `self` refers to the specific instance of the class currently executing the method. It allows access to instance variables and other methods of the object.
4. **Explain the difference between instance variables and class variables.**
   - *Answer:* Instance variables are bound to `self` and are unique to each object. Class variables are shared by all instances of a class.
5. **How do you create a subclass that inherits from a parent class?**
   - *Answer:* Pass the parent class name inside parentheses after the subclass name: `class SubClass(ParentClass):`.
6. **What are the three statements in a basic exception block?**
   - *Answer:* `try` (contains risky code), `except` (contains handler logic), and `finally` (contains cleanup code that always executes).
7. **What is the difference between writing mode `"w"` and append mode `"a"`?**
   - *Answer:* `"w"` clears the target file's content completely before writing. `"a"` appends new data at the end of the existing content without deleting anything.
8. **Why should we use the `with` statement when opening files?**
   - *Answer:* It implements the context manager protocol. It guarantees that the file is closed and buffers are flushed, even if a runtime exception halts code inside the block.
9. **What does `super()` do?**
   - *Answer:* It returns a proxy object that delegates method calls to a parent or sibling class, typically used to trigger the parent class's constructor.
10. **What error is raised when trying to divide a number by zero?**
    - *Answer:* `ZeroDivisionError`.

### Intermediate Level (10 Questions)

11. **Explain Encapsulation. How do you declare a private variable in Python?**
    - *Answer:* Encapsulation wraps data and methods in a single unit and hides the internal state. In Python, adding two leading underscores (e.g., `__balance`) makes an attribute private through name mangling.
12. **What is Polymorphism? Provide an example.**
    - *Answer:* Polymorphism allows different classes to implement methods with the same name but different behaviors. For instance, `Dog.speak()` prints "Woof", while `Cat.speak()` prints "Meow".
13. **Explain the difference between `__str__` and `__repr__`.**
    - *Answer:* `__str__` returns a user-friendly string representation (called by `print(obj)`). `__repr__` returns an unambiguous representation useful for developers and debugging.
14. **What is exception propagation?**
    - *Answer:* If an exception is not caught inside a nested function call, Python passes the exception object up to the calling frame, repeating this up the stack until a handler is found or the program terminates.
15. **What happens in a try block if the code executes successfully? Does the `else` block run?**
    - *Answer:* Yes. If the code inside the `try` block runs without errors, the `else` block executes before moving to the `finally` block.
16. **How do you define a custom exception class in Python?**
    - *Answer:* Create a class that inherits from the built-in `Exception` (or a subclass of it): `class MyCustomError(Exception): pass`.
17. **What is the difference between `os.path.exists()` and exception handling for checking file availability?**
    - *Answer:* `os.path.exists()` is a check-then-act pattern that is susceptible to race conditions. It is best practice to use Exception Handling (`try` opening, catch `FileNotFoundError`), which is safer and atomic.
18. **Explain the difference between `__enter__` and `__exit__` methods.**
    - *Answer:* They form the context manager protocol. `__enter__` sets up resources and returns the target object. `__exit__` handles cleanup, including closing files and handling exceptions raised in the block.
19. **How do you write a list of dictionaries directly into a CSV file with headers?**
    - *Answer:* Use the `csv.DictWriter` class. Pass the file object and the field names list, call `writeheader()`, and then call `writerows(data_list)`.
20. **What is Method Resolution Order (MRO)?**
    - *Answer:* MRO is the order in which Python searches for inherited methods in multiple inheritance structures, calculated using the C3 Linearization algorithm.

### Advanced Level (10 Questions)

21. **How does Python's name mangling work under the hood for private variables?**
    - *Answer:* When python compiles class source code, any attribute starting with double underscores (e.g. `__secret`) is rewritten to `_ClassName__secret` in the class dictionary, protecting it from accidental override.
22. **Can you access a private variable from outside its class? If yes, how?**
    - *Answer:* Yes, because name mangling does not create absolute privacy. You can access it by using its mangled name: `object._ClassName__variableName`. However, this is strongly discouraged in production.
23. **What is the difference between concrete classes, abstract classes, and interfaces in Python?**
    - *Answer:* Concrete classes can be instantiated. Abstract classes (inheriting from `abc.ABC`) contain abstract methods (decorated with `@abstractmethod`) and cannot be instantiated directly. Python has no formal interface keyword; it uses abstract base classes with no concrete methods as interfaces.
24. **Explain how Python manages exceptions during a `finally` block execution that has a `return` statement.**
    - *Answer:* If a `finally` block executes a `return` statement, any active exception raised inside the preceding `try` or `except` blocks is discarded/swallowed, and the function returns the value specified in `finally`.
25. **How does Python's JSON parser serialize custom class objects? What exception is raised, and how do you fix it?**
    - *Answer:* Python's `json.dump` throws a `TypeError: Object of type X is not JSON serializable` for custom class instances. To fix it, provide a custom encoder class inheriting from `json.JSONEncoder` or a serialization method (e.g., `to_dict()`) returning standard Python data structures.
26. **What is the difference between deep inheritance hierarchies and composition? Why does modern software design favor composition?**
    - *Answer:* Inheritance represents an "is-a" relationship (coupling classes tightly). Composition represents a "has-a" relationship (combining smaller independent components). Composition is favored because it reduces coupling and allows dynamic swapping of behaviors at runtime.
27. **How does Python's garbage collection handle class instances that contain reference cycles and define `__del__` methods?**
    - *Answer:* Prior to Python 3.4, reference cycles with `__del__` could not be safely collected and ended up in `gc.garbage`. In modern Python, the cyclic garbage collector can collect objects in cycles even if they have `__del__` methods, but utilizing `__del__` is still discouraged due to unpredictable execution timing.
28. **Explain the behavior of exceptions inside generator expressions or generators.**
    - *Answer:* When an exception occurs inside a generator, the exception is raised at the location of the `next()` call that triggered the generation. The generator is marked as closed, and subsequent `next()` calls will raise `StopIteration`.
29. **What are dunder methods for operator overloading? Name three of them and their operator targets.**
    - *Answer:* Dunder methods intercept Python operators:
      - `__add__(self, other)` for `+`
      - `__mul__(self, other)` for `*`
      - `__len__(self)` for `len()`
30. **Explain how the `traceback` module can be used programmatically to inspect errors.**
    - *Answer:* The `traceback` module allows you to extract, format, and print stack traces programmatically inside an `except` block using `traceback.format_exc()`, which is useful for sending logs to remote telemetry tools.

---

## ❓ Section 13: FAQs [01:55 - 01:58 | Duration: 3 mins]

**Q: Can I create a class without any variables, just functions?**
**A:** Yes. However, if your class only has functions and no state (variables), you might not need a class at all. You can write simple top-level Python functions instead, which is cleaner and uses less memory.

**Q: What is the difference between `except Exception as e:` and `except e:`?**
**A:** `except Exception as e:` is the correct syntax. It catches the exception class `Exception` and assigns the caught exception instance to the variable `e`. Writing `except e:` is invalid syntax because python expects a class name, not a variable.

**Q: Do file operations slow down my Python app?**
**A:** Yes. Reading/writing to a physical hard drive is thousands of times slower than reading/writing to RAM. To optimize, minimize file open/close operations. Batch your writes, or perform operations in RAM and save to the disk once at the end.

**Q: Can a class inherit from multiple classes in Python?**
**A:** Yes. Python supports **Multiple Inheritance**. However, it can make class architectures complex (known as the Diamond Problem). It is recommended to use interfaces or composition instead.

**Q: What does the `"r+"` file access mode do?**
**A:** It opens a file for both reading and writing. Unlike `"w+"`, it does not truncate or clear the file contents when opened.

**Q: Can I catch custom exceptions from external packages (like requests)?**
**A:** Yes. Import the exception class from the library (e.g. `from requests.exceptions import ConnectionError`) and catch it in your `except` block.

**Q: What is the difference between a TypeError and a ValueError?**
**A:** `TypeError` is raised when an operation is applied to an object of inappropriate type (e.g. adding string and integer: `"a" + 5`). `ValueError` is raised when the type is correct but the value is inappropriate (e.g. `int("abc")`).

**Q: Does Python have private access modifiers like `private` or `protected` in C++?**
**A:** No. Python operates on trust. Double underscores mangle the variable name to prevent direct modifications, but they do not enforce security. A single underscore (e.g., `_price`) is a developer convention indicating that the attribute is protected and should not be accessed outside the class.

**Q: Can I throw or raise an exception manually?**
**A:** Yes. Use the `raise` keyword: `raise ValueError("Invalid entry!")`.

**Q: What is a JSONDecodeError?**
**A:** It is a subclass of `ValueError` raised by the `json` module when it tries to parse a file containing invalid JSON formatting (e.g. missing commas or braces).

---

## 📋 Section 14: Assignment Brief [01:58 - 02:00 | Duration: 2 mins]

### Scenario

You are a Software Engineer at a civic tech agency in Coimbatore. The local public library has requested a lightweight console application to catalog books, track member registration, and manage loans. They do not have internet connection or SQL database systems. They need a robust Python command-line system that persists state to a local JSON file, validates inputs, and handles error loops gracefully.

### Objectives & Deliverables

Build a consolidated CLI suite containing:

1. **Book Class & Inventory**: Tracks ISBN, Title, Author, Stock, and Borrowers.
2. **Member Class**: Tracks Name, Member ID, and Loan limits.
3. **Library System Manager**: Connects Book and Member transactions, handles checkout/checkin logic.
4. **JSON File Persistence**: Automatically saves and loads library state from `library_db.json`.
5. **Robust Exception Handling**: Prevents invalid transactions or input crashes.

Refer to [04_Assignment.md](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day3_Advanced_Python/Day3_Teaching_content/04_Assignment.md) for full specs.

---

## 📋 Section 15: Assignment Solution Architecture

### Folder Structure

```
day3_assignment/
├── pyproject.toml
└── src/
    └── main.py
```

### Best Practices for Solutions

- Store Books and Members in classes to enforce OOP logic.
- Save library state to JSON by serialization of class properties.
- Define clear custom exceptions like `BookUnavailableError` and `MemberLimitError`.
- Wrap all terminal options in clean input validation loops to avoid crashes.
