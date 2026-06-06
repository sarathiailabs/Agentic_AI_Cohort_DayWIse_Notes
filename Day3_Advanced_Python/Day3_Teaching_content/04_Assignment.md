# 📝 Day 3 Assignment: Library Management System

## 💼 Industry Scenario
You are a Junior Software Engineer at a civic tech agency in Coimbatore. The local municipal library has hired your team to build a lightweight, fast, and local console-based cataloging tool. The library operates in areas with poor internet connectivity and cannot run heavy web servers or SQL database software. They require a Python terminal utility running on local desktop machines that:
1.  **Saves catalog state permanently** to local files so data is preserved across system restarts and power cuts.
2.  **Enforces library rules** (e.g., maximum borrow limits, stock constraints) using object properties and actions.
3.  **Handles scanner and operator mistakes gracefully** (like typing text where numbers are expected) using exception loops instead of crashing.

Your task is to build a consolidated Python CLI application named **Library Management System**.

---

## 📌 Module 1: System Domain Classes (OOP Design)

### Objectives
Create object-oriented models representing books, members, and transactions. Wrap attributes inside private variables where appropriate and validate changes using getter/setter methods.

### Core Domain Specifications

1.  **`Book` Class**:
    -   Attributes: `isbn` (str, unique), `title` (str), `author` (str), `quantity` (int, total copies owned), and `__borrowed_count` (int, private - tracks copies currently checked out).
    -   Methods:
        -   `get_available_copies() -> int`: Returns `quantity - borrowed_count`.
        -   `borrow_copy()`: Increments `borrowed_count`. Throws `BookUnavailableError` if no copies are available.
        -   `return_copy()`: Decrements `borrowed_count`. Throws a `ValueError` if borrowed count drops below zero.
        -   `to_dict() -> dict`: Converts attributes to a dictionary helper for JSON serialization.
        -   `__str__() -> str`: Returns a clean representation: `"'Python 101' by Guido van Rossum (ISBN: 1234) | Available: 3/5"`.

2.  **`Member` Class**:
    -   Attributes: `member_id` (str, unique), `name` (str), and `borrowed_books` (list of ISBN strings, tracks checked-out books).
    -   Methods:
        -   `borrow_book(isbn: str)`: Appends ISBN to the list. Throws `MemberLimitExceededError` if the member has already borrowed the maximum limit of **3 books**.
        -   `return_book(isbn: str)`: Removes ISBN from the list. Throws `ValueError` if the member did not borrow this book.
        -   `to_dict() -> dict`: Helper structure for JSON serialization.
        -   `__str__() -> str`: Returns status: `"Member: Priya Nair (ID: M101) | Borrowed: 2 books"`.

3.  **`Library` Class**:
    -   Attributes: `books` (dict mapping `isbn` -> `Book` object), `members` (dict mapping `member_id` -> `Member` object), and `db_file` (str, path to local JSON database).
    -   Methods:
        -   `load_data()`: Reads JSON database file, parses dictionaries, instantiates `Book` and `Member` objects, and populates the engine memory. Handles missing file gracefully (starts with clean empty state).
        -   `save_data()`: Serializes `books` and `members` collections into JSON format and writes back to disk.
        -   `add_book(isbn, title, author, quantity)`: Registers a book or updates the total quantity of an existing one.
        -   `register_member(member_id, name)`: Creates a member profile if the ID is unique.
        -   `checkout_book(member_id, isbn)`: Handles transactional operations: fetches book and member, verifies limits, deducts book copy, appends ISBN to member, and updates JSON on disk.
        -   `process_return(member_id, isbn)`: Returns a checked-out book copy to inventory.

---

## 📌 Module 2: Exception Boundaries (Safety Nets)

### Objectives
Define and trigger custom domain exceptions to enforce library rules, and intercept input value errors to prevent CLI menu loops from crashing.

### Requirements

1.  **Custom Exceptions**: Declare the following classes:
    -   `LibraryError(Exception)`: Parent exception base.
    -   `BookNotFoundError(LibraryError)`: Raised when searching for a book not in the catalog.
    -   `BookUnavailableError(LibraryError)`: Raised when a member checks out a book that has 0 available copies.
    -   `MemberNotFoundError(LibraryError)`: Raised when looking up a member ID not in registers.
    -   `MemberLimitExceededError(LibraryError)`: Raised when a member attempts to borrow a 4th book.

2.  **Input Exception Safety**: Wrap input requests in validation loops. If an operator enters negative integers or non-numeric strings for book counts, catch the `ValueError` and prompt them again.

---

## 🚀 Interactive CLI Submenu System

Your main script must run an interactive terminal menu:
```
======================================
     COIMBATORE PUBLIC LIBRARY
======================================
1. Book Catalog Operations
2. Member Registry Operations
3. Issue & Return Transactions
4. Save & Exit
======================================
```
Selecting Options 1, 2, or 3 must open respective submenus:

-   **Book Submenu**:
    -   `1. Add Book`
    -   `2. Search Book (by Title / Author - case-insensitive partial match)`
    -   `3. List All Books`
    -   `4. Back to Main Menu`
-   **Member Submenu**:
    -   `1. Register Member`
    -   `2. List All Members`
    -   `3. Back to Main Menu`
-   **Issue/Return Submenu**:
    -   `1. Checkout Book`
    -   `2. Return Book`
    -   `3. Back to Main Menu`

---

## 🎁 Bonus Challenges (To score full marks!)

1.  **Export Current Borrowed List to CSV**: Add an option to the Main Menu to export a report of all currently active loans to `active_loans.csv` containing columns: `Member ID, Member Name, Book Title, ISBN`.
2.  **Overdue Fine Calculator**: When issuing a book, save the checkout date as a string (format `YYYY-MM-DD`). When returning, ask the operator for the return date. If the borrow duration exceeds **14 days**, calculate an overdue fine of **₹5 per day** and print the total fine. (Hint: Use Python's built-in `datetime.strptime()` function to calculate day difference).

---

## 📊 Evaluation Rubric

| Criterion | Points | Focus Area |
| :--- | :---: | :--- |
| **OOP & Encapsulation** | 25% | Correct definitions of `Book`, `Member`, and `Library` classes. Proper use of private variables, getters, and constructor delegators. |
| **Exception Handling** | 25% | Declaring custom exceptions, raising them at appropriate validation boundaries, and wrapping console input parsing to avoid code crashes. |
| **File Persistence** | 20% | Correct implementation of JSON loading/saving of class states. Handling empty file scenarios cleanly. |
| **Modularity & DRY** | 15% | Avoiding large spaghetti blocks. Placing logic in appropriate class methods. |
| **Submenu CLI Experience** | 15% | Clean formatting of invoices, lists, and intuitive submenu navigation loops. |

---

## 📤 Submission Format
-   Your code must be modular and contained in a directory named `day3_assignment`.
-   Use `pyproject.toml` to declare your package configuration.
-   Run your code using:
    ```bash
    uv run src/main.py
    ```
