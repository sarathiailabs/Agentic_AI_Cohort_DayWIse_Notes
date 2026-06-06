# 🎓 Student Reference Guide: Functions & Data Structures

## Welcome to Day 2! 🚀
This guide helps you review everything we covered in today's lecture. Keep this handy as a quick cheat sheet for syntax, methods, and concepts.

---

## 📌 Core Concepts Cheat Sheet

### 1. Functions (Reusable Code blocks)
Functions take inputs (parameters), run some code, and output a result (return).

```python
# 1. Defining a function with parameters and type hints
def calculate_gst(amount: float, tax_rate: float = 0.05) -> float:
    """Calculates GST amount for a given transaction."""
    gst_value = amount * tax_rate
    return gst_value  # Output

# 2. Calling the function
bill_gst = calculate_gst(amount=200.0)  # Uses default tax_rate=0.05
print(f"GST: ₹{bill_gst}")  # Output: GST: ₹10.0
```

---

### 2. Lists (Ordered, Modifiable/Mutable)
Used for items in a sequence (e.g., items in a shopping cart).

```python
# Create a list
cart = ["samosa", "tea", "biscuit"]

# Indexing & Slicing (0-indexed)
print(cart[0])       # "samosa" (first item)
print(cart[-1])      # "biscuit" (last item)

# List Methods
cart.append("chips") # Adds "chips" to the end
cart.pop(1)          # Removes and returns item at index 1 ("tea")
cart.remove("samosa")# Removes "samosa" by value
cart.insert(0, "poha")# Inserts "poha" at index 0

print(cart)          # Output: ['poha', 'biscuit', 'chips']
```

---

### 3. Tuples (Ordered, Unmodifiable/Immutable)
Used for constants or fixed logs (e.g., GPS coordinates).

```python
# Create a tuple
gps_coordinates = (12.9716, 77.5946)  # (Latitude, Longitude)

# Accessing elements
print(gps_coordinates[0])  # 12.9716

# Modifying a tuple throws an error!
# gps_coordinates[0] = 13.0  # TypeError

# Unpacking a tuple
lat, lng = gps_coordinates
```

---

### 4. Sets (Unordered, Unique/No Duplicates)
Used for fast lookups, removing duplicates, and mathematical set operations (Venn diagrams).

```python
# Create a set
visitor_numbers = {"9876543210", "9123456789", "9876543210"}
print(visitor_numbers)  # Duplicate is removed: {'9876543210', '9123456789'}

# Venn Diagram Operations
skills_python = {"amit", "rahul", "priya"}
skills_aws = {"rahul", "sneha"}

# Intersection (Common to both)
print(skills_python & skills_aws)  # {'rahul'}

# Union (All unique names)
print(skills_python | skills_aws)  # {'amit', 'rahul', 'priya', 'sneha'}

# Difference (Only in Python, not AWS)
print(skills_python - skills_aws)  # {'amit', 'priya'}
```

---

### 5. Dictionaries (Key-Value Pairs, Fast lookup)
Used to map relationships (e.g., menu items to their prices).

```python
# Create a dictionary
menu = {
    "samosa": 15,
    "tea": 10,
    "poha": 20
}

# Lookup value by key
print(menu["samosa"])  # 15

# Safe lookup using get() (prevents KeyErrors)
price = menu.get("maggi", 0)  # Returns default 0 if "maggi" doesn't exist

# Adding/Modifying key-value pairs
menu["biscuit"] = 5  # New entry
menu["samosa"] = 18  # Update existing

# Iterating dictionary
for item, price in menu.items():
    print(f"{item} costs ₹{price}")
```

---

### 6. List Comprehensions (Concise Loop Syntax)
Build new lists in a single line of code.

```python
# Traditional Way:
squares = []
for x in range(1, 6):
    squares.append(x * x)

# Pythonic Way (List Comprehension):
squares = [x * x for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Filtering with conditions (even squares only)
even_squares = [x * x for x in range(1, 6) if x % 2 == 0]
print(even_squares)  # [4, 16]
```

---

## 🛠️ Performance & Complexity Summary

| Structure | Syntax | Mutable? | Ordered? | Duplicate Keys? | Search Complexity | Key Use Case |
|-----------|--------|----------|----------|-----------------|-------------------|--------------|
| **List** | `[1, 2]` | Yes | Yes | Yes | $O(N)$ (slow) | Shopping carts, arrays |
| **Tuple** | `(1, 2)` | No | Yes | Yes | $O(N)$ (slow) | GPS coords, constants |
| **Set** | `{1, 2}` | Yes | No | No | $O(1)$ (fast) | Unique logs, filters |
| **Dict** | `{"a": 1}`| Yes | Yes (3.7+) | Keys: No | $O(1)$ (fast) | Ledger maps, databases |

---

## 📚 Practice Challenge of the Day

Try writing a small function in a file `practice.py`:
1. Create a function `get_student_details(roll_number)` that checks a dictionary of student profiles.
2. If the roll number is found, return the student name and score.
3. If not found, return "Not Found" using the `.get()` method.
4. Run the code locally using:
   ```bash
   uv run practice.py
   ```
