# 🎓 Student Reference Guide: Python Fundamentals & UV

## Welcome to Day 1! 🚀
This guide helps you review everything we covered in today's lecture. Keep this handy as you work through your assignments.

---

## 📌 Core Concepts Cheat Sheet

### 1. Variables & Data Types
Variables are containers for storing data values. In Python, you do not need to declare types manually.

```python
# Variables and assignments
samosa_price = 15            # Integer (int)
gst_percentage = 0.05        # Floating point number (float)
shop_name = "Apna Canteen"   # String (str)
is_open = True              # Boolean (bool)

# Displaying data
print(type(samosa_price))    # Output: <class 'int'>
```

### 2. Basic Arithmetic Operators
- `+` Addition: `10 + 5 = 15`
- `-` Subtraction: `10 - 5 = 5`
- `*` Multiplication: `10 * 5 = 50`
- `/` Division (always returns float): `10 / 5 = 2.0`
- `//` Floor Division (rounds down): `10 // 3 = 2`
- `%` Modulo (remainder): `10 % 3 = 1`

### 3. Comparison & Logical Operators
- Comparison: `==` (equal), `!=` (not equal), `>`, `<`, `>=`, `<=`
- Logical: `and`, `or`, `not`

```python
# Examples
is_eligible = (attendance_percentage >= 75) and (fees_paid == True)
```

### 4. Input & Output (I/O)
- `print()` displays messages.
- `input()` grabs user text from terminal (always returned as string).

```python
# Read input and convert to number
username = input("Enter your name: ")
age = int(input("Enter your age: "))  # Casting str to int
```

### 5. Control Flow: Conditions
Use `if`, `elif` (else if), and `else` to control which code runs.

```python
bill = 120

if bill > 100:
    discount = bill * 0.10
    print("Discount applied!")
else:
    discount = 0

final_bill = bill - discount
```

### 6. Control Flow: Loops
- **`for` loop**: Best when you know the number of iterations in advance (e.g. going through a range).
- **`while` loop**: Best when you want to loop until a specific condition becomes false.

```python
# For loop printing 1 to 5
for i in range(1, 6):
    print(f"Token number: {i}")

# While loop countdown
queue_size = 3
while queue_size > 0:
    print(f"Serving customer. Queue size: {queue_size}")
    queue_size -= 1
```

---

## 🛠️ Local Environment Setup Guide (Windows)

We use **UV**, the fastest package manager in the Python ecosystem. Follow these steps to set it up on your laptop:

### Step 1: Install UV
Open **PowerShell** as an administrator on your Windows laptop (Search for "PowerShell", right-click, select "Run as Administrator") and run:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Step 2: Verify Installation
Restart your terminal and run:
```bash
uv --version
```
If you see the version number, installation was successful!

### Step 3: Run your first Python file
Create a folder named `day1_practice` and initialize a project:
```bash
uv init day1_practice
cd day1_practice
```
This automatically creates a `main.py` file. Run it using:
```bash
uv run main.py
```
`uv` will automatically download Python if you don't have it installed, compile, and execute your code in milliseconds.

---

## 🐢 Troubleshooting: Slow internet/college labs
If you have slow cellular internet or lab networks, installing standard tools can be slow.
- **UV Cache:** Once `uv` downloads Python or packages once, it caches them globally. It will never download them again for other folders on your PC.
- **Offline mode:** If you need to run things in a pinch without any internet, `uv` will run cached environments completely offline.

---

## 📚 Resources & Learning Links
- [Official Python Documentation](https://docs.python.org/3/tutorial/index.html)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [UV Documentation](https://docs.astral.sh/uv/)
