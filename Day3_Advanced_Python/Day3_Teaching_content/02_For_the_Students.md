# 🎓 Student Reference Guide: OOP, Exception Handling & File I/O

## Welcome to Day 3! 🚀
This guide helps you review everything we covered in today's lecture. Keep this handy as a quick cheat sheet for syntax, methods, and configurations.

---

## 📌 Core Concepts Cheat Sheet

### 1. Object-Oriented Programming (OOP)

OOP organizes code into blueprints (Classes) and instances (Objects).

```python
# 1. Defining a Class
class Book:
    # Class variable (shared by all instances)
    library_name = "Coimbatore Public Library"

    def __init__(self, title: str, author: str, price: float):
        # Instance variables (unique to each instance)
        self.title = title
        self.author = author
        
        # Encapsulation: Private variable (name mangled)
        self.__price = price

    # Getter Method to access private variable
    def get_price(self) -> float:
        return self.__price

    # Setter Method to modify private variable safely
    def set_price(self, new_price: float):
        if new_price > 0:
            self.__price = new_price
        else:
            raise ValueError("Price must be positive!")

    # Dunder method for user-friendly printing
    def __str__(self) -> str:
        return f"'{self.title}' by {self.author}"

# 2. Creating Object Instances
book1 = Book(title="Python Basics", author="Guido", price=450.0)
print(book1)             # Output: 'Python Basics' by Guido
print(book1.get_price()) # Output: 450.0

# 3. Inheritance & Polymorphism
class TextBook(Book):
    def __init__(self, title: str, author: str, price: float, subject: str):
        super().__init__(title, author, price) # Call parent constructor
        self.subject = subject

    # Override parent __str__ (Polymorphism)
    def __str__(self) -> str:
        return f"{super().__str__()} [Subject: {self.subject}]"

tb = TextBook("Machine Learning", "Alice", 800.0, "AI")
print(tb) # Output: 'Machine Learning' by Alice [Subject: AI]
```

---

### 2. Exception Handling

Prevents your program from crashing by catching errors at runtime.

```python
# Custom Exception Definition
class InsufficientStockError(Exception):
    """Raised when request exceeds stock."""
    pass

# Try-Except-Else-Finally Structure
try:
    stock = 5
    quantity = int(input("Enter purchase quantity: "))
    
    if quantity < 0:
        raise ValueError("Quantity cannot be negative!")
    if quantity > stock:
        raise InsufficientStockError("We don't have enough books!")

    total = quantity * 120.0
    print(f"Calculated bill total: ₹{total:.2f}")

except ValueError as ve:
    # Catches string inputs or negative numbers
    print(f"❌ Input Error: {ve}")

except InsufficientStockError as ise:
    # Catches custom stock error
    print(f"❌ Stock Error: {ise}")

except Exception as e:
    # Catch-all safety net for other unexpected errors
    print(f"❌ Unexpected Error: {e}")

else:
    # Runs ONLY if no exception occurred
    print("✅ Purchase processed successfully!")

finally:
    # ALWAYS runs, regardless of errors
    print("🔄 Thank you for visiting the store.")
```

---

### 3. File Handling

Allows data persistence on your local disk.

```python
# 1. Text File Reading & Writing
# Writing ("w") overwrites existing content. Use "a" to append.
with open("notes.txt", "w") as file:
    file.write("Day 3 Notes: OOP and Files\n")
    file.write("Line 2: Persistent Storage\n")

# Reading ("r")
with open("notes.txt", "r") as file:
    content = file.read() # Read entire file
    # file.readlines() reads file into list of strings line by line

print(content)

# 2. JSON Processing (Relational Structure Persistence)
import json

data = {
    "students": [
        {"name": "Amit", "score": 85},
        {"name": "Sneha", "score": 90}
    ]
}

# Serialize (Save python dict to JSON file)
with open("db.json", "w") as file:
    json.dump(data, file, indent=4)

# Deserialize (Load JSON file back to python dict)
with open("db.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data["students"][0]["name"]) # Output: Amit
```

---

## 🛠️ Methods and Modes Summary

### File Access Modes
| Mode | Action | File Exists? | Truncates Data? | Read/Write Target |
|---|---|---|---|---|
| **`r`** | Read | Must exist | No | Read from start |
| **`w`** | Write | Created if missing | Yes | Overwrite from start |
| **`a`** | Append | Created if missing | No | Write at end of file |
| **`r+`**| Read/Write | Must exist | No | Edit from start |

### Exception Classes
-   **`ValueError`**: Invalid value parameter (e.g. `int("abc")`).
-   **`TypeError`**: Incompatible operation types (e.g. `len(100)`).
-   **`IndexError`**: List index out of range.
-   **`KeyError`**: Dictionary key not found.
-   **`FileNotFoundError`**: Target file doesn't exist.
-   **`PermissionError`**: File locked or folder read-only.

---

## 📚 Practice Challenge of the Day

Try writing a small script in a file `practice.py`:
1.  Define a class `Vehicle` with private `__speed` attribute initialized to 0.
2.  Add a method `accelerate(amount)` that increments speed. Throw a `ValueError` if the acceleration amount is negative.
3.  Write the current speed to a `speed_log.txt` file inside a `try-except` block.
4.  Run it locally using:
    ```bash
    uv run practice.py
    ```
