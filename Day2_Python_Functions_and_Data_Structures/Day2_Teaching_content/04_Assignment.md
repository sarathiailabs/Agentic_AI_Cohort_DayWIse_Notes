# 📝 Day 2 Assignment: Contact Book & Expense Tracker

## 💼 Industry Scenario
You are a Junior Software Engineer at a boutique software consultancy in Coimbatore. The local merchant union has hired your team to build lightweight, fast command-line utilities. Many retail shopkeepers do not have access to laptops with heavy database software. They need efficient Python utilities that can run directly on cheap Linux/Windows cash registers to manage customer relationships and track daily cash outflows.

Your job is to build a consolidated Python CLI application containing two modules:
1.  **Smart Contact Book CLI**
2.  **Personal Expense Tracker CLI**

---

## 📌 Module 1: Smart Contact Book CLI

### Objectives
Build an interactive terminal menu that allows users to add, view, search, and delete customer contacts. Each contact must store a Name, Phone Number, Email, and a Set of Category tags (e.g., `"VIP"`, `"Retail"`, `"Credit"`).

### Core Functional Requirements
1.  **Unique Keys:** Store contacts in a dictionary where the **Phone Number** is the unique key:
    ```python
    contacts = {
        "9876543210": {
            "name": "Ramesh Kumar",
            "email": "ramesh@gmail.com",
            "tags": {"Retail", "Credit"}
        }
    }
    ```
2.  **Duplicate Protection:** When adding a contact, check if the phone number already exists in your dictionary. If it exists, raise a warning and do not overwrite it unless the user explicitly requests an update.
3.  **Tags Enforcements:** Let users assign multiple tags to a contact (e.g. VIP, Credit, Bulk). Store these tags in a **Set** to prevent duplicate tags for the same contact.
4.  **Lookup System:** Implement a search function where searching a phone number performs a direct dictionary lookup ($O(1)$ time complexity). Also allow searching contacts by Name (partial match, case-insensitive).

---

## 📌 Module 2: Personal Expense Tracker CLI

### Objectives
Build an interactive tool to manage daily restaurant expenses, supplier payouts, and fuel bills.

### Core Functional Requirements
1.  **Expense Log:** Store expenses in a list of dictionaries. Each expense must record:
    -   `description` (str)
    -   `amount` (float)
    -   `category` (str) (e.g., "Food", "Transport", "Supplies")
2.  **Category Validation:** Restrict allowed categories to a fixed set: `{"food", "transport", "supplies", "others"}`. Normalise inputs to lowercase before checking.
3.  **Comprehension Analytics:** Use **List Comprehensions** to perform data operations:
    -   Filter and display expenses belonging to a specific category.
    -   Filter and list high-value expenses above a threshold amount (e.g., above ₹500).
4.  **Summary Analytics:** Write a function that loops through the expenses and prints the total money spent today.

---

## 🚀 Combined CLI Menu System
Your main script must launch an interactive terminal menu:
```
======================================
     COIMBATORE RETAILERS TOOLKIT
======================================
1. Manage Contacts (Contact Book)
2. Manage Expenses (Expense Tracker)
3. Exit System
======================================
```
Selecting Option 1 or 2 should open a submenu for that specific toolkit.

---

## 🎁 Bonus Challenges (To score full marks!)
1.  **File Persistence:** Save your contact dictionary and expense list to JSON files (`contacts.json` and `expenses.json`) and load them automatically when the app starts.
2.  **Category Tag Venn Analysis:** (Contacts) Allow the merchant to enter two tags (e.g. "VIP" and "Credit") and display contacts that have **both** tags (using set intersection).

---

## 📊 Evaluation Rubric

| Criterion | Points | Focus Area |
| :--- | :---: | :--- |
| **Code Modularity** | 20% | Correct use of functions, input arguments, and returns. No giant blocks of code. |
| **Dictionary Operations** | 25% | Key lookup, addition, modification, safe lookup via `.get()`, list of dicts. |
| **Sets & Immutability** | 20% | Set logic for tags, duplicate removal, search checks. |
| **List Comprehensions** | 20% | Proper filtering syntax (no traditional multi-line loops for filters). |
| **UX & Error Handling** | 15% | Graceful menu loops, handling invalid entries, printing clear invoices. |

---

## 📤 Submission Format
-   Your code must be modular and contained in a directory named `day2_assignment`.
-   Use `pyproject.toml` to declare your package configuration.
-   Run your code using:
    ```bash
    uv run src/main.py
    ```
