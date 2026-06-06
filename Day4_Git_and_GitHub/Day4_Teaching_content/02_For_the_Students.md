# 📚 Day 4: Git & GitHub Student Cheat Sheet

This is your quick reference guide for all version control operations. Save this sheet as a study guide for classroom labs, assignments, and professional projects.

---

## ⚡ Git Commands Quick Reference

| Command | Action | When to Use |
| :--- | :--- | :--- |
| **`git init`** | Initializes a local Git repository. | Once at the start of a project. |
| **`git status`** | Shows tracked/untracked/modified files. | Run constantly to check files state. |
| **`git add <file>`** | Stages specific changes for the next commit. | When a file is ready to be committed. |
| **`git add .`** | Stages all changes in the directory. | To queue all modifications. |
| **`git commit -m "<msg>"`** | Saves your staged snapshot. | After reaching a logical milestone. |
| **`git log`** | Lists commit history. | To see past snapshots. |
| **`git log --oneline --graph`**| Visualizes history as a linear graph. | For clean branch timelines. |
| **`git diff`** | Shows modifications in the workspace. | To see edits before staging. |
| **`git checkout -b <name>`** | Creates and switches to a new branch. | Before starting a new feature. |
| **`git checkout <name>`** | Switches to an existing branch. | To return to another workspace branch. |
| **`git merge <branch>`** | Merges target branch into current branch. | When a feature branch is ready. |
| **`git clone <url>`** | Clones a remote repository locally. | To download a project from GitHub. |
| **`git remote add origin <url>`**| Links local repository to a remote repository.| Once when setting up a remote backup. |
| **`git push origin <branch>`** | Uploads local commits to GitHub. | To share changes or backup work. |
| **`git pull origin <branch>`** | Fetches and merges remote changes. | At start of session to get team updates.|
| **`git revert <commit-hash>`** | Undoes a commit by creating a new commit. | To safely undo pushed changes. |
| **`git reset --hard HEAD~1`** | Deletes last commit and working edits! | **Warning:** Destructive. Use with care. |

---

## 🛑 Step-by-Step: Resolving Merge Conflicts

When Git shows `CONFLICT (content): Merge conflict in <file>`, do not panic! Follow these 5 steps:

1.  **Locate the Conflict:**
    Open the conflicted file in VS Code. Conflicted blocks are wrapped inside Git conflict markers:
    ```python
    <<<<<<< HEAD
    def apply_discount(total): return total * 0.05
    =======
    def apply_discount(total): return total * 0.10
    >>>>>>> feature-discount
    ```
2.  **Evaluate the Options:**
    *   `<<<<<<< HEAD` is your current branch's code.
    *   `>>>>>>> feature-discount` is the incoming branch's code.
    *   `=======` divides them.
3.  **Resolve the Code:**
    Edit the file. Manually delete the lines `<<<<<<< HEAD`, `=======`, and `>>>>>>> feature-discount`. Keep the correct code or merge both features:
    ```python
    def apply_discount(total): return total * 0.10
    ```
4.  **Mark as Resolved:**
    Tell Git the file is fixed by staging it:
    ```bash
    git add <filename>
    ```
5.  **Finalize the Merge:**
    Commit the resolution:
    ```bash
    git commit -m "merge: resolve discount rate conflict"
    ```

---

## 🐍 Production Python `.gitignore` Template

Create a file named `.gitignore` in your repository root directory. Copy and paste these lines:

```gitignore
# --- Python Virtual Environments ---
.venv/
env/
venv/
ENV/
.env

# --- Python Execution Cache ---
__pycache__/
*.py[cod]
*$py.class

# --- System and IDE Settings ---
.vscode/
.idea/
.DS_Store
Thumbs.db

# --- Notebook & Logs ---
.ipynb_checkpoints/
*.log
```

---

## 🚀 Standard Development Loop

To work on features and collaborate, follow this loop:

```
[ Start Day ] ➔ git pull origin main
      │
[ Create Task ] ➔ git checkout -b feature-my-task
      │
[ Code & Test ] ➔ Make changes in editor
      │
[ Stage Files ] ➔ git add .
      │
[ Save Progress] ➔ git commit -m "feat: implement task core logic"
      │
[ Share & Review ] ➔ git push origin feature-my-task (Create PR on GitHub)
```
