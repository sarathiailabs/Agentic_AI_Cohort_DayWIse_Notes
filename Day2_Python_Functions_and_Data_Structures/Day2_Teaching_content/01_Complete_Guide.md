# 📖 Day 2 Complete Guide: Python Functions & Data Structures

## Master Reference Document

**Day:** 2 of 20  
**Topic:** Python Functions & Data Structures  
**Duration:** 2 Hours (120 Minutes)  
**Difficulty Level:** Beginner to Intermediate  
**Prerequisites:** Day 1 (Python Variables, Conditions, and Loops)

---

## 🎯 Executive Summary
Welcome to Day 2 of the AI Engineer & Agentic AI Engineer Bootcamp. Today, we move beyond basic control flow to study the core organizing structures of Python: **Functions** and **Data Structures** (Lists, Tuples, Sets, Dictionaries). We will learn how to write modular, reusable code using functions, handle groups of ordered items in lists, protect static data using tuples, enforce uniqueness with sets, map relationships with key-value dictionaries, and generate data concisely using list comprehensions. 

The goal of this session is to teach students how to manage, manipulate, and query complex data patterns. This forms the foundation for data handling in retrieval-augmented generation (RAG) and state-tracking in AI Agents.

---

## 📅 2-Hour Session Timing and Timeline

| Time Slot | Elapsed Time | Duration | Section / Focus | Description |
|-----------|--------------|----------|-----------------|-------------|
| 1 | 00:00 - 00:10 | 10 mins | Intro & Recap | Previous concept recap & today's Problem Statement |
| 2 | 00:10 - 00:30 | 20 mins | Conceptual & Story | Problem, Real World Story, Beginner Explanation, & Why it exists |
| 3 | 00:30 - 00:50 | 20 mins | Technical & Architecture | Technical explanation, deep dive, components, internal working, and ASCII diagrams |
| 4 | 00:50 - 01:10 | 20 mins | Whiteboard & Interaction | Live whiteboard session, student Q&A, and interactive discussion points |
| 5 | 01:10 - 01:40 | 30 mins | Live Coding & Practice | Live demo of `03_Coding_Notebook.ipynb`, step-by-step walkthrough, mini-project, and industry project |
| 6 | 01:40 - 01:55 | 15 mins | Industry Context & Review | Industry use cases, common mistakes, FAQs, and top interview questions |
| 7 | 01:55 - 02:00 | 5 mins | Assignment & Wrap-up | Student assignment explanation, rubric, and session conclusion |

> [!TIP]
> **Pacing Reminder:** If students struggle with the syntax of list comprehensions, pause and write out the equivalent traditional `for` loop first. Show them that list comprehensions are just a visual shortcut, not a magic trick.

---

## 📚 Section 1: Problem Statement [00:00 - 00:10 | Duration: 10 mins]

### What problem existed before functions and data structures?
In Day 1, we wrote a canteen billing script that read input, did some arithmetic, and printed a result. That worked for one order. But consider these challenges as a business grows:
1. **Code Duplication:** What if Ramesh Kaka has 3 billing counters? If we need to change how the bulk discount is calculated, we must copy-paste the same code 3 times and modify it in multiple places. If we make a mistake in one copy, the system becomes inconsistent.
2. **Data Scaling:** What if we have 50 items on the menu instead of just Samosa and Tea? Storing them in variables like `item1_price`, `item2_price`... up to `item50_price` is an absolute nightmare. We cannot easily loop through individual variables, sort them, or search for an item.
3. **Relational Lookup:** How do we link an item name (e.g., "Samosa") to its price (₹15)? Without a mapping structure, we have to write long chains of `if-elif-else` statements, which are slow and hard to maintain.
4. **Duplicate Entries:** If a customer adds "Samosa" to their cart multiple times, how do we keep a clean list of unique items they ordered?

### Why Functions & Data Structures Exist
- **Functions:** Allow us to package a block of code, give it a name, and run it anywhere in our program by passing different inputs (arguments). It enforces the **DRY (Don't Repeat Yourself)** principle.
- **Lists:** Ordered, modifiable sequences that allow us to store collections of data (e.g., items in a cart).
- **Tuples:** Immutable (unmodifiable) ordered sequences, perfect for read-only configurations (e.g., GPS coordinates of a delivery address).
- **Sets:** Unordered collections of unique elements, ideal for removing duplicates and running math operations like union/intersection.
- **Dictionaries:** Key-value stores that allow instant lookup (e.g., looking up the price of an item using its name).
- **List Comprehensions:** A clean, readable Pythonic shorthand to create new lists from existing ones in a single line.

---

## 📚 Section 2: Real World Story [00:10 - 00:20 | Duration: 10 mins]

### The Swiggy Restaurant Partner Automation Story
Let's visit Amit, a restaurant owner in Nagpur who runs "Nagpur Biryani House". He decides to list his restaurant on Swiggy. 

Initially, Swiggy was small. For every order, a Swiggy support agent would call Amit and say, "One Chicken Biryani, please prepare it." Amit would write it down, cook it, and hand it to a driver.

Soon, Amit was receiving 200 orders a day. The phone lines were jammed. 
- **The Data Structure Problem:** How does Swiggy store the menu of Nagpur Biryani House? If they use single variables, it's impossible. They need a **Dictionary** where the key is the dish name and the value is the price: `{"Chicken Biryani": 250, "Veg Pulao": 180, "Raita": 40}`.
- **The List Problem:** When a customer orders, their cart is a **List** of dishes: `["Chicken Biryani", "Raita"]`.
- **The Function Problem:** When the order is placed, Swiggy's server needs to calculate the final bill. They don't write billing code from scratch for each order. Instead, they call a pre-defined function: `calculate_final_bill(cart_items, tax_rate, discount_code)`. This function takes the customer's cart, applies tax, subtracts coupon discounts, and outputs the final payable amount.
- **The Set Problem:** If the restaurant wants to know how many *unique* customers ordered today (excluding repeat customers), they feed the list of customer phone numbers into a **Set**.

Thanks to this automation, Amit receives orders on a tablet screen, cooks them immediately, and Swiggy processes millions of transactions daily without a single phone call.

---

## 📚 Section 3: Beginner Explanation [00:20 - 00:30 | Duration: 10 mins]

Let's break down these five structures using daily Indian life analogies:

### 1. Functions: The Tea Recipe Maker
Think of a function as an **automatic tea maker machine** at a railway platform. 
- You write the recipe once (define the function `def make_tea()`).
- The machine accepts inputs (parameters: milk type, sugar spoons, ginger status).
- You press a button (call the function), and it outputs a cup of tea (returns the result).
- You can make 100 cups of tea with different ingredients without rewriting the recipe.

### 2. Lists: The Tiffin Box Compartments
Think of a List as a **tiered steel tiffin box** (*dabba*).
- You have compartment 0 (Roti), compartment 1 (Sabzi), compartment 2 (Achar).
- The order matters. You can replace the Sabzi with Paneer (mutable/modifiable).
- You can add another compartment at the bottom (append) or remove one (pop).

### 3. Tuples: The Sealed ID Card
Think of a Tuple as a student's **College ID Card**.
- Once printed, your Name, Roll Number, and Date of Birth cannot be changed (immutable).
- If you try to write on it with a pen, the security guard won't allow it. It protects core integrity.

### 4. Sets: The Mandir Footwear Stand
Think of a Set as the **shoe rack outside a temple**.
- No two pairs of shoes can be kept in the exact same spot. Every pair must be unique (no duplicates).
- The shoes are not in any specific order; they are scattered (unordered).
- If you bring a pair of shoes that is already in the rack, you can't add a duplicate.

### 5. Dictionaries: The Kirana Khata Ledger
Think of a Dictionary as the **shopkeeper's credit register book** (*khata diary*).
- Each page is labeled with a customer's name (the unique **Key**), e.g., `"Rahul"`.
- Opposite to the name, the credit balance is written (the **Value**), e.g., `₹450`.
- If you want to check Rahul's balance, you don't read the whole book from page 1. You flip straight to the page labeled `"Rahul"` (fast lookup).

---

## 📚 Section 4: Technical Explanation & Architecture [00:30 - 00:50 | Duration: 20 mins]

### Deep Dive: Python Memory Allocation for Lists vs. Tuples

To understand why Python has both Lists and Tuples, we must look at how they are stored in computer RAM.

#### 1. Python Lists (Dynamic Arrays)
A list is a **dynamic array**. Because lists are mutable (you can append items at runtime), Python overallocates memory. If you create a list of 3 items, Python might allocate space for 6 items in memory to avoid resizing the array constantly.
- **Under the hood:** The list object itself contains a reference to a contiguous block of memory containing pointers to the actual objects (integers, strings, etc.) stored elsewhere in the heap.
- **Time Complexity:** 
  - Accessing item by index (`list[0]`): $O(1)$ (constant time).
  - Appending item (`list.append(x)`): $O(1)$ amortized.
  - Inserting/Deleting at start (`list.insert(0, x)`): $O(N)$ (requires shifting all subsequent items in memory).

#### 2. Python Tuples (Static Arrays)
A tuple is a **static array**. Because its size and contents are fixed at creation time, Python allocates the exact amount of memory needed.
- **Under the hood:** Tuples are lightweight and read-only. Python optimizes tuple creation via a mechanism called *tuple recycling* for small tuples to save memory.
- **Performance:** Tuples are faster to iterate over than lists and consume less memory.

#### 3. Python Dictionaries (Hash Tables)
Python dictionaries are implemented as **hash tables**.
- **Hashing:** When you store a key-value pair, Python passes the key through a hash function: `hash(key)`. This generates an integer index.
- **Lookup:** Python goes directly to the index in memory. This is why dictionary lookups are $O(1)$ on average, regardless of whether the dictionary has 10 items or 10,000,000 items.
- **Keys must be hashable:** Only immutable objects (strings, numbers, tuples) can be used as keys. You cannot use a list as a dictionary key.

---

### Visual Diagrams (ASCII)

#### Memory Layout: List vs. Tuple

```
Python List: `my_list = [10, 20]` (Mutable)
+-------------------------------------------+
| List Header: Size=2, Allocated=4          |
| [ Pointer 0 ] ---> [ 10 ] (in Heap)       |
| [ Pointer 1 ] ---> [ 20 ] (in Heap)       |
| [ Empty Slot ]                            |  <-- Overallocated memory for future appends
| [ Empty Slot ]                            |
+-------------------------------------------+

Python Tuple: `my_tuple = (10, 20)` (Immutable)
+-------------------------------------------+
| Tuple Header: Size=2                      |
| [ Pointer 0 ] ---> [ 10 ] (in Heap)       |
| [ Pointer 1 ] ---> [ 20 ] (in Heap)       |  <-- Exact memory allocation, no overhead
+-------------------------------------------+
```

#### Hash Table Lookup in Dictionaries

```
Key: "Samosa" ➔ [ Hash Function ] ➔ Index: 4 ➔ [ Bucket 4 ] ➔ Value: ₹15
Key: "Tea"    ➔ [ Hash Function ] ➔ Index: 1 ➔ [ Bucket 1 ] ➔ Value: ₹10
```

---

## 🎨 Section 5: Real World Examples [00:50 - 01:00 | Duration: 10 mins]

### Beginner Examples

#### 1. College Attendance Log (Lists & Sets)
*   **Problem:** A teacher in Visakhapatnam records student roll numbers in a WhatsApp chat. Some students copy-paste the message and accidentally duplicate roll numbers. The teacher needs a clean count of unique students present.
*   **Solution:** Put all roll numbers in a list, convert it to a set to remove duplicates, and calculate the length.
*   **Technology Used:** Lists, Sets, `len()` function.
*   **Business Outcome:** Eliminates proxy attendance and manual sorting errors.

#### 2. Auto Driver Ride Log (List of Tuples)
*   **Problem:** A Rapido auto driver in Surat needs to log their trips. Each log entry needs a pick-up area, a drop-off area, and the fare. This data must not be accidentally modified once logged.
*   **Solution:** Store each trip as an immutable tuple: `(pickup, dropoff, fare)`. Combine these trips into a list.
*   **Technology Used:** Tuples, Lists.
*   **Business Outcome:** Secure log history that cannot be modified by fat-finger editing mistakes.

#### 3. Phone Contact Details (Dictionaries)
*   **Problem:** A senior citizen in Bhopal needs to look up phone numbers easily. Searching a paper directory page by page is hard due to weak eyesight.
*   **Solution:** A CLI tool where entering the name instantly retrieves the number from a key-value dictionary.
*   **Technology Used:** Dictionary lookup, String normalization.
*   **Business Outcome:** Instant contact search, improved accessibility.

---

### Industry Examples

#### 1. Swiggy Cart Item Counter (Dictionaries & Lists)
*   **Problem:** A Swiggy user in Pune adds multiple items to their cart. The system needs to keep track of the quantity of each unique item without storing duplicates.
*   **Solution:** A dictionary mapping the item ID to its quantity: `{"biryani_01": 2, "coke_05": 3}`.
*   **Technology Used:** Dictionary updating, element checking.
*   **Business Outcome:** Accurate cart display and item counting for payment processing.

#### 2. Paytm Wallet Cashback Filters (List Comprehensions)
*   **Problem:** Paytm wants to query a user's transaction history list and filter out transactions greater than ₹500 to send a cashback coupon.
*   **Solution:** Use list comprehension to filter the transactions in a single line of code.
*   **Technology Used:** List Comprehension with Conditional filter.
*   **Business Outcome:** Blazing-fast marketing automation running on high-velocity data.

#### 3. IRCTC Seat Allocation Lock (Sets & Functions)
*   **Problem:** During Tatkal booking, thousands of users request seat numbers simultaneously. The system must prevent assigning the same seat number to two different passengers.
*   **Solution:** Maintain a set of `booked_seats`. Use a function to check if a seat is in the set; if not, add it to the set and confirm the ticket.
*   **Technology Used:** Sets, Functions, Set Member Checking (`in`).
*   **Business Outcome:** Zero double-bookings, preventing operational disputes.

---

### Startup & Enterprise Examples

#### 1. Dunzo Delivery Partner Routing (Startup Example)
```
Problem:
  Dunzo needs to calculate delivery coordinates for a driver.
  The pick-up and drop-off coordinates (Latitude, Longitude) must remain strictly constant so the map logic doesn't crash due to accidental code edits.
Solution:
  Store coordinates in immutable tuples: `pickup = (21.1458, 79.0882)`.
  Pass these tuples to a function that computes the distance.
Technology Used:
  Tuples, Math formulas, Functions.
  Time Complexity: O(1) memory lookup.
Business Outcome:
  Guarantees route calculations are bug-free and crash-free due to coordinate mutability.
```

#### 2. TCS Employee Skill Mapping (Enterprise Example)
```
Problem:
  TCS resource managers in Chennai need to search a list of 10,000 employees to find developers who know BOTH "Python" and "AWS" to assign them to a premium client project.
Solution:
  Represent each employee's skills as a set.
  Perform a set intersection operation (`python_set & aws_set`) to instantly find qualifying employees.
Technology Used:
  Python Sets, Set Intersection (`&`).
  Time Complexity: O(min(len(s1), len(s2))) - significantly faster than nested loops.
Business Outcome:
  Reduces project staffing search time from hours to milliseconds.
```

---

## 🎨 Section 6: Visual Diagrams [01:00 - 01:05 | Duration: 5 mins]

### Visual Representation of Data Structures (ASCII)

```
LIST: Ordered, Indexable, Mutable (Tiffin Box)
+-----------+-----------+-----------+
|  Index 0  |  Index 1  |  Index 2  |
|  "Roti"   |  "Sabzi"  |  "Achar"  |  <--- Can change "Sabzi" to "Paneer"
+-----------+-----------+-----------+

TUPLE: Ordered, Indexable, Immutable (Sealed Envelope)
+-----------+-----------+-----------+
|  Index 0  |  Index 1  |  Index 2  |
| "Roll_10" | "Amit K." | "B.Tech"  |  <--- Lock symbol: Read-only
+-----------+-----------+-----------+

SET: Unordered, Unique, No Indices (Shoe Rack)
     +------------+      +------------+
     |  "Adidas"  |      |   "Bata"   |   <--- If you try to add another "Bata",
     +------------+      +------------+        it is silently ignored.
            +------------+
            |  "Sparx"   |
            +------------+

DICTIONARY: Key-Value Pairs, Fast Lookup (Khata Register Pages)
+-----------------------+-----------------------+
|  Key (Unique)         |  Value (Any data)     |
+-----------------------+-----------------------+
|  "samosa"             |  15                   |
|  "tea"                |  10                   |
|  "poha"               |  20                   |
+-----------------------+-----------------------+
```

---

## 🎨 Section 7: Whiteboard Explanation [01:05 - 01:10 | Duration: 5 mins]

### Left Board: Function Execution Stack & Scope
1. Draw two boxes: **Global Scope** and **Local Scope (inside function)**.
2. Define a simple function:
   ```python
   def add_gst(price):
       tax = price * 0.18
       return price + tax
   ```
3. Show that calling `add_gst(100)` creates a temporary workspace in memory. The variable `tax` exists *only* inside this block. If you try to print `tax` in the main program (Global Scope), Python throws a `NameError`.
4. Explain: "Think of the local scope as your bedroom. What happens inside stays inside, unless you throw it out of the window (which is the `return` statement)."

### Right Board: List vs. Set Venn Diagrams
1. Draw a circle representing `Student_A_Skills = {"Python", "SQL", "Excel"}`.
2. Draw an overlapping circle representing `Student_B_Skills = {"SQL", "AWS", "Docker"}`.
3. Show the intersection area: `{"SQL"}` (Common skills).
4. Show the union area: `{"Python", "SQL", "Excel", "AWS", "Docker"}` (Total skills pool).
5. Explain: "Sets let us solve complex business questions (like matching requirements with skills) in a single line of code using Venn Diagram mathematics."

---

## 💬 Section 8: Teaching Script [01:10 - 01:20 | Duration: 10 mins]

**Instructor:** "Yesterday, we built a billing script for Ramesh Kaka's canteen. Now, imagine Ramesh Kaka wants to add a new rule: 'If a student orders Samosa, Tea, and Biscuit, give them a Combo Discount.' How would you write this if your menu items are all individual variables?"

**Student:** "We would have to write lots of `if-else` blocks for each item, which would get very messy."

**Instructor:** "Exactly. It's a complete mess! Today, we solve this. Let's introduce the **Dictionary**. Think of it as Kaka's credit khata ledger. Every page has a customer name (key) and their debt amount (value). Let's write this on our screen: `menu = {"Samosa": 15, "Tea": 10, "Biscuit": 5}`. What happens if we want to find the price of a 'Tea'? We write `menu["Tea"]`, and Python gives us `10` instantly. No loops, no searching. It is direct.

Now, let's talk about **Functions**. Think of a juice stall on the road. The vendor has a mixer-grinder. The mixer-grinder has a fixed process: chop, blend, filter. You feed in mango and milk (inputs), it runs, and outputs Mango Shake. You feed in apple and water, it outputs Apple Juice. You don't buy a new mixer for every customer! You reuse the same machine. In Python, that mixer is a function. We write `def make_juice(fruit, liquid):` and use it multiple times. Let's see how this works in code."

---

## 💻 Section 9: Live Demo [01:20 - 01:40 | Duration: 20 mins]

### Demo Goal
To write a script that stores a restaurant menu, accepts customer orders, calculates the subtotal using a function with tax, and extracts high-value items using a list comprehension.

### Step-by-Step Flow

1. **Initialize project directory:**
   ```bash
   uv init day2_demo
   cd day2_demo
   ```
2. **Write the Script (`main.py`):**
   ```python
   # Day 2 Live Demo: Restaurant Bill Processor

   # 1. Define the Menu (Dictionary)
   MENU = {
       "samosa": 15,
       "tea": 10,
       "biryani": 150,
       "paneer_tikka": 120,
       "cold_coffee": 50
   }

   # 2. Define the Bill Calculator Function
   def calculate_bill(cart, gst_rate=0.05):
       """
       Calculates subtotal, GST, and final bill from a list of cart items.
       """
       subtotal = 0
       missing_items = []
       
       for item in cart:
           item_lower = item.lower().strip()
           if item_lower in MENU:
               subtotal += MENU[item_lower]
           else:
               missing_items.append(item)
               
       gst_amount = subtotal * gst_rate
       total_bill = subtotal + gst_amount
       
       return subtotal, gst_amount, total_bill, missing_items

   # 3. Simulate a Customer Order (List)
   customer_cart = ["Samosa", "tea", "biryani", "ice_cream"]

   # 4. Call the Function
   sub, tax, final, unresolved = calculate_bill(customer_cart)

   # 5. Output Invoice
   print("=== INVOICE ===")
   print(f"Items Ordered: {', '.join(customer_cart)}")
   print(f"Subtotal: ₹{sub:.2f}")
   print(f"GST (5%):  ₹{tax:.2f}")
   print(f"Total Bill: ₹{final:.2f}")
   if unresolved:
       print(f"⚠️ Warning: We don't sell: {', '.join(unresolved)}")
   print("===============\n")

   # 6. List Comprehension: Filter Premium Items (Price > ₹40)
   premium_items = [item for item, price in MENU.items() if price > 40]
   print(f"⭐ Premium Menu Items: {premium_items}")
   ```

3. **Run using UV:**
   ```bash
   uv run main.py
   ```

### Expected Output
```
=== INVOICE ===
Items Ordered: Samosa, tea, biryani, ice_cream
Subtotal: ₹175.00
GST (5%):  ₹8.75
Total Bill: ₹183.75
⚠️ Warning: We don't sell: ice_cream
===============

⭐ Premium Menu Items: ['biryani', 'paneer_tikka', 'cold_coffee']
```

---

## 💼 Section 10: Industry Use Cases [01:40 - 01:45 | Duration: 5 mins]

### 1. Zomato Restaurant Search (Dictionaries)
Zomato searches for restaurants in seconds because it caches restaurant details indexed by restaurant ID. Instead of checking every database record, it performs a dictionary-like key lookup.

### 2. PhonePe Fraud Detection (Sets)
PhonePe tracks malicious device IDs. If a user logs in, their device ID is checked against a set of `fraudulent_devices = {"dev_92", "dev_34", "dev_12"}`. Since set lookups take $O(1)$ time, transactions are approved or flagged in milliseconds.

### 3. LinkedIn Feed Generator (List Comprehensions & Functions)
When you open LinkedIn, a ranking function scores posts. A list comprehension is then used to filter out posts with scores below a certain threshold: `feed = [post for post in posts if score(post) > 0.5]`.

---

## ⚠️ Section 11: Common Mistakes & Fixes [01:45 - 01:50 | Duration: 5 mins]

### 1. Modifying a List While Iterating Over It
- *Error:* 
  ```python
  numbers = [1, 2, 3, 4, 5]
  for n in numbers:
      if n % 2 == 0:
          numbers.remove(n)  # Skips elements because indices shift
  ```
- *Fix:* Iterate over a copy of the list or use list comprehensions:
  ```python
  numbers = [n for n in numbers if n % 2 != 0]
  ```

### 2. Mutating Default Arguments in Functions
- *Error:*
  ```python
  def add_to_cart(item, cart=[]):
      cart.append(item)
      return cart
  # Multiple calls will share the same list in memory!
  ```
- *Fix:* Use `None` as the default value:
  ```python
  def add_to_cart(item, cart=None):
      if cart is None:
          cart = []
      cart.append(item)
      return cart
  ```

### 3. Accessing a Dictionary Key That Doesn't Exist
- *Error:* `menu["maggi"]` throws a `KeyError` if "maggi" is not in the dictionary.
- *Fix:* Use the `.get()` method to provide a fallback: `menu.get("maggi", 0)`.

### 4. Confusing `append()` and `extend()` in Lists
- *Error:* `list.append([1, 2])` nests the list, making it `[old, [1, 2]]` instead of merging it.
- *Fix:* Use `list.extend([1, 2])` or `list += [1, 2]` to merge elements.

### 5. Attempting to Modify a Tuple
- *Error:* `coords = (12.97, 77.59); coords[0] = 13.0` throws a `TypeError: 'tuple' object does not support item assignment`.
- *Fix:* Convert to list first if modification is needed, or re-bind the variable to a new tuple.

### 6. Misusing List Comprehension for Complex Logic
- *Error:* Writing nested, 3-line comprehensions that no one can read.
- *Fix:* If logic is complex, write a regular `for` loop with clear variable names.

### 7. Missing `return` Statement in Functions
- *Error:*
  ```python
  def double(x):
      result = x * 2
  val = double(5)  # val is None
  ```
- *Fix:* Explicitly return the value: `return result`.

### 8. Variable Shadowing (Scope Confusion)
- *Error:* Declaring a local variable inside a function with the same name as a global variable, causing confusion.
- *Fix:* Use unique variable names or pass the global variable explicitly as a parameter.

### 9. Attempting to Hash Mutable Types in Sets/Dict Keys
- *Error:* `my_set = {[1, 2], [3, 4]}` throws a `TypeError: unhashable type: 'list'`.
- *Fix:* Use tuples instead of lists: `my_set = {(1, 2), (3, 4)}`.

### 10. Forgetting to Call the Function
- *Error:* `print(calculate_bill)` prints the function address in memory instead of executing it.
- *Fix:* Add parentheses to execute: `print(calculate_bill(my_cart))`.

---

## 📋 Section 12: Interview Questions & Answers [01:50 - 01:55 | Duration: 5 mins]

### Beginner Level (10 Questions)

1. **What is the difference between a list and a tuple?**
   - *Answer:* Lists are mutable (can be changed) and use square brackets `[]`. Tuples are immutable (cannot be changed) and use parentheses `()`.

2. **How do you remove duplicates from a list?**
   - *Answer:* Convert the list to a set, then back to a list: `list(set(my_list))`.

3. **What is a dictionary key-value pair?**
   - *Answer:* It is a mapping structure where a unique Key (like an item name) points to a Value (like a price).

4. **What does the `len()` function do on a dictionary?**
   - *Answer:* It returns the number of key-value pairs in the dictionary.

5. **How do you check if a key exists in a dictionary?**
   - *Answer:* Using the `in` keyword: `"samosa" in menu`.

6. **What is the default return value of a function that does not have a `return` statement?**
   - *Answer:* It returns `None`.

7. **How do you add an item to the end of a list?**
   - *Answer:* Using `list.append(item)`.

8. **What is the difference between `remove()` and `pop()` in lists?**
   - *Answer:* `remove(value)` searches for and deletes the first occurrence of the specified value. `pop(index)` removes and returns the item at the specified index (defaults to the last index).

9. **Can a dictionary have duplicate keys?**
   - *Answer:* No. Keys must be unique. If you add a duplicate key, it overwrites the existing value.

10. **How do you merge two dictionaries in Python 3.9+?**
    - *Answer:* Using the union operator: `merged_dict = dict1 | dict2`.

### Intermediate Level (10 Questions)

11. **Explain what a list comprehension is and write one that squares even numbers.**
    - *Answer:* A list comprehension is a shorthand syntax to build lists. Example: `squares = [x**2 for x in numbers if x % 2 == 0]`.

12. **Why can't lists be used as dictionary keys?**
    - *Answer:* Dictionary keys must be hashable and immutable. Since lists are mutable, their values can change, which would corrupt the hash lookup index.

13. **What is the difference between `*args` and `**kwargs`?**
    - *Answer:* `*args` allows a function to accept any number of positional arguments as a tuple. `**kwargs` allows a function to accept any number of keyword arguments as a dictionary.

14. **What is the time complexity of searching for an element in a list vs. a set?**
    - *Answer:* Searching in a list takes $O(N)$ linear time (checks each item). Searching in a set takes $O(1)$ constant time (uses hash table indexing).

15. **Explain the behavior of `dict.get(key, default)`.**
    - *Answer:* It retrieves the value for `key` if it exists. If it does not, it returns the specified `default` value instead of raising a `KeyError`.

16. **How does Python handle memory allocation for a list as it grows?**
    - *Answer:* Python allocates extra capacity (overallocates) to avoid continuous resizing. When the list runs out of room, it allocates a larger chunk of memory and copies the references over.

17. **What is variable shadowing in Python?**
    - *Answer:* Variable shadowing occurs when a variable declared inside a local scope (like a function) shares the same name as a variable in the outer global scope. The local variable hides the global one inside the function.

18. **How do you unpack a tuple into separate variables?**
    - *Answer:* `lat, lng = (12.97, 77.59)`. The number of variables on the left must match the number of elements in the tuple.

19. **What is set intersection, union, and difference?**
    - *Answer:*
      - **Intersection (`&`):** Common elements in both sets.
      - **Union (`|`):** All unique elements from both sets combined.
      - **Difference (`-`):** Elements in the first set that are not in the second.

20. **Can a tuple contain mutable objects like lists? Give an example.**
    - *Answer:* Yes. `my_tuple = ([1, 2], 3)`. The tuple itself is immutable (you cannot change the list pointer or delete elements), but the list *inside* it can still be modified: `my_tuple[0].append(3)`.

### Advanced Level (10 Questions)

21. **Explain the hash collision resolution mechanism in Python dictionaries.**
    - *Answer:* Python uses open addressing with perturbation to resolve collisions. If two keys hash to the same bucket index, it computes a new index using a pseudo-random probe sequence until an empty slot is found.

22. **What is the difference between deep copy and shallow copy for nested lists?**
    - *Answer:* A shallow copy (`copy()`) copies the outer list structure but references the same nested object elements in memory. A deep copy (`copy.deepcopy()`) recursively copies both the outer list and all nested objects, creating completely independent memory trees.

23. **How does the global statement work in Python? Why is it generally avoided?**
    - *Answer:* The `global` keyword allows you to modify variables in the global scope from within a function. It is avoided because it introduces side effects, making state tracking, testing, and debugging difficult.

24. **Explain how Python's list comprehension avoids bytecode overhead compared to a traditional loop.**
    - *Answer:* List comprehensions are optimized at C-level in the interpreter. They emit a specialized `LIST_APPEND` bytecode instruction, which executes faster than standard method lookup and function call layers in a normal `list.append()` loop.

25. **What is the difference between local scope, global scope, and enclosing scope (LEGB rule)?**
    - *Answer:* Python resolves names using the LEGB order:
      - **L (Local):** Names assigned inside a function.
      - **E (Enclosing):** Names in local scope of enclosing functions (nested functions).
      - **G (Global):** Names assigned at top-level of module file.
      - **B (Built-in):** Predefined names (like `print`, `len`).

26. **What are function annotations/type hints in Python? Do they enforce types at runtime?**
    - *Answer:* Syntax to specify variable and return types (e.g., `def add(x: int) -> int:`). They do **not** enforce types at runtime; they are metadata used by static analyzers like `mypy` or IDEs for autocompletion and linting.

27. **How does Python's `set` ensure items are unique? What criteria must an object meet to be added to a set?**
    - *Answer:* Sets rely on hashing. To be added, an object must be **hashable** (must implement `__hash__()` and `__eq__()` methods) and immutable, guaranteeing its hash value never changes during its lifetime.

28. **Explain the concept of closures in Python.**
    - *Answer:* A closure is a nested function that retains access to variables from its outer (enclosing) scope even after the outer function has finished executing.

29. **What is the time complexity of adding an item at the beginning of a list vs. appending it? Why?**
    - *Answer:* Adding at the start (`insert(0, x)`) is $O(N)$ because all existing elements must be shifted right in memory. Appending is $O(1)$ on average because elements are added to the end where overallocated slots are available.

30. **How do you write a generator expression instead of a list comprehension? Why would you use it?**
    - *Answer:* Use parentheses instead of brackets: `gen = (x**2 for x in range(1000000))`. You use generator expressions to save memory because they yield items lazily one-by-one, rather than allocating memory for the entire list in RAM.

---

## ❓ Section 13: FAQs [01:55 - 01:58 | Duration: 3 mins]

**Q: Can a list contain different types of data, like integer, string, and list inside it?**  
**A:** Yes. Python lists are heterogeneous. You can store `[15, "Samosa", True, [10, 20]]` in one list. However, in professional production code, it is best practice to keep list elements of the same type for predictable processing.

**Q: Why does `x = my_list.sort()` set `x` to `None`?**  
**A:** The `sort()` method sorts the list **in-place** (modifying the original list) and returns `None`. If you want a *new* sorted list while keeping the original unchanged, use the `sorted(my_list)` function instead.

**Q: What is the difference between `dict.keys()` and a list of keys?**  
**A:** `dict.keys()` returns a dynamic **view object**. It reflects updates to the dictionary instantly and uses very little memory. You can convert it to a standard list using `list(dict.keys())` if needed.

**Q: Are python dictionaries ordered?**  
**A:** In Python 3.7+, dictionaries preserve the insertion order of keys as a language specification, but they do not support index-based lookups like `dict[0]`.

---

## 📋 Section 14: Assignment Brief [01:58 - 02:00 | Duration: 2 mins]

### Scenario
You are working as an intern at a tech agency in Coimbatore. The local merchant association wants simple, fast console utilities for small shopkeepers to manage customer phone contacts and track daily cash outflows.

### Objectives
Build a consolidated CLI suite containing:
1. **Smart Contact Book:** Uses a dictionary to store contact details, checks for duplicates using a set, and allows adding, searching, and deleting contacts.
2. **Personal Expense Tracker:** Uses list of dictionaries to track expenses, allows adding items with categories, and uses list comprehensions to filter expenses.

Refer to [04_Assignment.md](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day2_Python_Functions_and_Data_Structures/Day2_Teaching_content/04_Assignment.md) for full specs.

---

## 📋 Section 15: Assignment Solution Architecture

### Folder Structure
```
day2_assignment/
├── pyproject.toml
└── src/
    └── main.py
```

### Best Practices for Solutions
- Use dictionaries for quick key-value lookups.
- Enforce phone number uniqueness using a set.
- Filter category expenses using clean list comprehensions.
- Handle key errors gracefully using `dict.get()`.
