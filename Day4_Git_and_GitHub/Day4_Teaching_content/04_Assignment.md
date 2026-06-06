# 📝 Day 4 Assignment: Coimbatore Retail Kiosk Version Control

## 💼 Industry Scenario
You are a Junior Software Engineer at a fast-growing retail tech startup in Coimbatore. The company is developing a localized, lightweight cash register kiosk software (`kiosk.py`) that stores transaction records on offline machines inside rural retail shops.

Your lead has requested you to establish proper **version control guidelines** using Git. To demonstrate your version control discipline, you must set up the local repository, configure Git parameters, manage parallel feature developments using branches, handle a merge conflict when two different developers edit the price discount strategies, and publish the release snapshot.

---

## 📌 Module 1: Repository Initialization & Ignored files (25 Points)

### Objectives
Initialize a local Git repository, configure your user profile details, and write a strict `.gitignore` to protect sensitive local transaction databases and virtual environment files from being checked in.

### Specifications
1.  Create a folder named `coimbatore_retail_kiosk`.
2.  Initialize the repository using `git init`.
3.  Configure repository-specific local identity variables (do not use `--global` to avoid overriding global settings):
    *   Set user name to `Your Name`.
    *   Set user email to `your.email@example.com`.
4.  Write a `.gitignore` containing rules to ignore:
    *   Any Python virtual environments (`.venv/`, `venv/`).
    *   Python cache files (`__pycache__/`, `*.pyc`).
    *   Your local database file `transactions_db.json`.
5.  Stage and commit `.gitignore` with the message: `chore: initialize repository with ignore lists`.

---

## 📌 Module 2: Base Feature Development (25 Points)

### Objectives
Develop the baseline billing application, stage it, and commit it with a conventional commit message.

### Specifications
1.  Create `kiosk.py` containing a function `run_kiosk()` that:
    *   Prompts the operator to enter a product's base price (INR).
    *   Prompts the operator to enter the quantity.
    *   Calculates the gross total.
    *   Prints: `Gross Total: INR <amount>`.
2.  Test the script locally to make sure it executes without syntax errors.
3.  Stage `kiosk.py` and commit with message: `feat: implement basic price inputs and totals calculations`.

---

## 📌 Module 3: Branching and Merge Conflict Simulation (30 Points)

### Objectives
Simulate collaborative parallel workflows. You will create a feature branch to write a retail discount rule, while simultaneously committing a different discount strategy on the `main` branch to induce a merge conflict.

### Specifications
1.  Create and checkout a new branch named `feature-billing` using `git checkout -b feature-billing`.
2.  Modify `kiosk.py` on the `feature-billing` branch to include a **flat rate discount**:
    *   If the gross total exceeds ₹100, subtract a flat **₹20** discount.
    *   Compute the final `net_payable = gross_total - discount`.
    *   Print both the discount and net payable amounts.
3.  Stage and commit the changes on `feature-billing` branch with message: `feat: integrate flat rate retail discounts logic`.
4.  Switch back to the `main` branch: `git checkout main`.
5.  Modify `kiosk.py` on the `main` branch at the *same position* in the code. Implement a **percentage promotional discount**:
    *   Apply a flat **10%** discount to the gross total.
    *   Compute final payable amounts.
    *   Stage and commit these changes on `main` branch with message: `feat: implement 10% promotional discount scheme`.
6.  Merge `feature-billing` into `main`:
    ```bash
    git merge feature-billing
    ```
7.  Verify that the merge fails with a conflict status. Show `git status` output.

---

## 📌 Module 4: Conflict Resolution and Release Tagging (20 Points)

### Objectives
Manually resolve the merge conflict, finalize the commit, and tag the release in Git.

### Specifications
1.  Open `kiosk.py` in your editor. Locate conflict markers.
2.  Select the **10% promotional discount** strategy as the preferred business calculation. Delete the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) and keep the 10% code. Clean up any broken logic.
3.  Test your code to ensure it runs correctly.
4.  Stage the resolved file and commit:
    ```bash
    git add kiosk.py
    git commit -m "merge: resolve billing conflicts by selecting 10% promo rate"
    ```
5.  Create a Git version tag named `v1.0.0` with an annotated comment:
    ```bash
    git tag -a v1.0.0 -m "Release version 1.0.0 for deployment to kiosks"
    ```
6.  Print your commit history graph to verify structural logs:
    ```bash
    git log --oneline --graph
    ```

---

## 🎁 Bonus Challenges (To score full marks!)

1.  **Branch Cleanups:** Delete the `feature-billing` branch now that it has been safely merged into `main` (`git branch -d feature-billing`). Verify that the branch is gone using `git branch`.
2.  **Automated Git Status Script:** Write a short PowerShell script (`git_status_backup.ps1`) or Bash script (`git_status_backup.sh`) that runs `git status`, writes the output to `git_status_report.txt`, and automatically adds and commits that text file if modifications are detected.

---

## 📊 Evaluation Rubric

| Criterion | Points | Focus Area |
| :--- | :---: | :--- |
| **Git Initialization & Config** | 15% | Correct directory initializations and local user profiles (no global pollution). |
| **`.gitignore` Rules** | 10% | Correct placement and formatting of rules to block virtual environments and cache directories. |
| **Branching Integrity** | 20% | Successful creation, execution, and movement between `main` and `feature-billing` branches. |
| **Merge Conflict Execution** | 30% | Correctly editing identical sections of files, generating a merge conflict, and manually resolving markers. |
| **Tagging & Logs** | 15% | Generating version tag `v1.0.0` and outputting clean `--oneline --graph` history structures. |
| **Modularity & Execution** | 10% | Code runs properly after merge resolution with clean terminal I/O. |

---

## 📤 Submission Format
-   All files must be saved within a directory named `coimbatore_retail_kiosk`.
-   Provide the outputs of `git status` showing conflicts and `git log --oneline --graph` showing final history.
