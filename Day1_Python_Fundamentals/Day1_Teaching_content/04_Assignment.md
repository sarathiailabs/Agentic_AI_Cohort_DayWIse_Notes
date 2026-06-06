# 📝 Day 1 Assignment: Python CLI Utilities Suite

## 💼 Business Scenario
You have joined a local tech software agency in Coimbatore as a Junior Software Engineer. The agency is building console-based terminal applications for schools and local retail shops. Your team lead has tasked you with building a consolidated Python CLI tool that hosts three useful utilities.

---

## 🎯 Objectives
You must build a single, modular Python script containing three distinct CLI applications:
1. **Interactive Calculator**
2. **Number Guessing Game**
3. **Student Grade Analyzer**

---

## 📋 Detailed Requirements

### Project 1: Multi-functional Calculator
- **Inputs:** Prompts user for `num1`, `num2`, and an operator (`+`, `-`, `*`, `/`).
- **Logic:**
  - Performs the correct arithmetic operation.
  - **Critical:** Checks if `num2` is zero before attempting division, printing a user-friendly error instead of crashing the program.
- **Output:** Format the result to two decimal places (e.g. `Result: 10.50`).

### Project 2: Number Guessing Game
- **Setup:** The program generates a target number between `1` and `100` (Hint: use Python's built-in `random` module: `import random; target = random.randint(1, 100)`).
- **Core Loop:**
  - Repeatedly asks the user to guess the number.
  - If the guess is higher than the target, print `"Too High! Try again."`
  - If the guess is lower, print `"Too Low! Try again."`
  - If the guess is correct, print a congratulations message showing the **total number of attempts** the user took.
  - **Exit Condition:** Loop runs until the correct number is guessed.

### Project 3: Student Grade Calculator
- **Inputs:** Prompts for student name and marks obtained in three subjects (out of 100 each): **Mathematics**, **Science**, and **English**.
- **Logic:**
  - Calculate average marks.
  - Check pass status: A student passes only if they score **at least 35 marks in each individual subject**. If they score less than 35 in any subject, they automatically fail.
  - Assign division grades based on average:
    - **First Division:** Average >= 60%
    - **Second Division:** Average between 50% and 59.9%
    - **Third Division:** Average between 35% and 49.9%
    - **Fail:** Average < 35% or failed in individual subject checks.
- **Output:** A neat report card showing subject marks, pass/fail status, average, and assigned division grade.

---

## 🌟 Bonus Tasks (For Extra Credit)
1. **Replay Functionality:** Add a loop around the Number Guessing Game so that when a game ends, it asks `"Do you want to play again? (y/n)"`.
2. **Input Validation:** In all three apps, handle cases where the user inputs alphabetical letters instead of numbers (e.g. typing `"five"` instead of `5`) using conditional checks or `try-except` blocks.

---

## 📊 Evaluation Rubric (100 Marks Total)

| Criteria | Max Marks | Description |
| :--- | :--- | :--- |
| **Logic & Correctness** | 40 Marks | All three utilities run correctly without crashing. Edge cases like division by zero are handled. |
| **Code Structure & Comments** | 20 Marks | Clean code formatting with standard indentation (4 spaces), descriptive variable names, and clear explanatory comments. |
| **Input Validation** | 20 Marks | Handles invalid string input gracefully (doesn't crash on bad inputs). |
| **CLI Layout & Design** | 10 Marks | Beautifully formatted output using dashes, borders, and clear textual feedback. |
| **Bonus Features** | 10 Marks | Implementation of guessing game replay loops and currency formatting elements. |

---

## 📂 Submission Format
Create your project folder using `uv`:
```bash
uv init day1_assignment
cd day1_assignment
```
Implement your code in `src/main.py` (or `main.py`).

Your submission folder must have this layout:
```
day1_assignment/
├── pyproject.toml
└── main.py
```
Submit the `main.py` file to your instructor via the designated Google Form or GitHub repository.
