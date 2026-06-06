# 📖 Day 4 Complete Guide: Git & GitHub Fundamentals

## Master Reference Document

**Day:** 4 of 20  
**Topic:** Git & GitHub Fundamentals  
**Duration:** 2 Hours (120 Minutes)  
**Difficulty Level:** Beginner  
**Prerequisites:** Python Fundamentals (Day 1–3)

---

## 🎯 Executive Summary
Welcome to Day 4 of the AI Engineer & Agentic AI Engineer Bootcamp. Today, we bridge the gap between solo scripting and team-based production engineering by mastering **Version Control using Git and GitHub**. 

Students will move away from risky, manual file tracking (e.g., `main_v2_final.py`) to professional local repository management and remote collaboration workflows. By the end of this session, students will understand how Git operates under the hood (snapshots vs. deltas), manage branching structures, write conventional commits, intentionally trigger and resolve merge conflicts, and collaborate using GitHub Pull Requests.

---

## 📅 2-Hour Session Timing and Timeline

| Time Slot | Elapsed Time | Duration | Section / Focus | Description |
|-----------|--------------|----------|-----------------|-------------|
| 1 | 00:00 - 00:10 | 10 mins | Intro & Scenario | The nightmare of code deletion, naming confusion, and manual collaboration. |
| 2 | 00:10 - 00:25 | 15 mins | Conceptual & Story | Google Docs vs. Git, RPG Savepoints, and the Canteen developer story. |
| 3 | 00:25 - 00:45 | 20 mins | Git Architecture | Working Directory, Staging Area, Local Repo, and Git's DAG (snapshots). |
| 4 | 00:45 - 00:55 | 10 mins | Whiteboard Diagrams | Mapping files through states, branching visuals, and merge conflict layouts. |
| 5 | 00:55 - 01:10 | 15 mins | Teaching Script | Live instructor commentary for variables vs. files, and branching. |
| 6 | 01:10 - 01:40 | 30 mins | Live CLI Demo | Step-by-step local repo creation, commits, branches, conflict generation, and resolution. |
| 7 | 01:40 - 01:50 | 10 mins | GitHub & Collaboration | Remotes, pushes, clones, forks, pulls, and the Pull Request (PR) review cycle. |
| 8 | 01:50 - 01:55 | 5 mins | Best Practices & Traps | `.gitignore` setup, Conventional Commits, Detached HEAD, and security hygiene. |
| 9 | 01:55 - 02:00 | 5 mins | Review & Assignment | 30 QA review, student assignment briefing, and grading rubrics. |

> [!TIP]
> **Pacing Reminder:** Git concepts can feel highly abstract to beginners. Spend less time explaining theoretical graph theories and more time showing visual "snapshots" on the whiteboard. Ensure every student initializes a local repo during the live demo.

---

## 📚 Section 1: Problem Statement [00:00 - 00:10 | Duration: 10 mins]

### What problem existed before version control?
Imagine you are building a billing engine for a retail store in Coimbatore. 
*   **Version Naming Chaos:** You start writing code in `billing.py`. You add a feature and save it as `billing_v2.py`. You fix a bug and save it as `billing_v2_final.py`, and later `billing_v2_final_final_fixed.py`. Within a week, your folder is cluttered with 20 confusing, redundant files.
*   **The Overwrite Catastrophe:** You and your colleague are working on the same file over a shared drive or email. They send you their changes. You copy them into your folder, accidentally overwriting a critical tax calculation feature you spent three days building. Your code is gone forever.
*   **No Time Machine:** Your system breaks on production night. You need to quickly undo the last two hours of code modifications. However, since you didn't save manual backups of that exact hour, you have to guess and manually rewrite/delete code, introducing new bugs.

### What is Git?
Git is a **Distributed Version Control System (DVCS)** created by Linus Torvalds (the creator of Linux) in 2005. 
*   **Distributed:** Every developer has a complete copy of the repository, including its entire history, on their local machine. If the main server crashes, any developer's local machine can restore the codebase.
*   **Snapshot-based:** Unlike older systems that track individual line modifications (deltas), Git takes a snapshot of your entire workspace every time you save your progress (commit).

### Why Git for AI Engineers?
AI Engineering moves exceptionally fast. You will constantly experiment with different prompt layouts, model hyperparameters, RAG retrieval pipelines, and agentic loops. Git allows you to:
1.  Safely experiment in isolated branches (e.g., `experiment-rag-claude` vs `experiment-rag-gemini`) without breaking working production code.
2.  Instantly roll back failed model integrations.
3.  Protect sensitive API keys using `.gitignore` configurations, preventing devastating cloud billing charges.

---

## 📚 Section 2: Real World Story & Analogies [00:10 - 00:25 | Duration: 15 mins]

### The Coimbatore Smart Canteen Code Crash
Akash and Divya are junior AI developers working on an automated kiosk for a popular college canteen in Coimbatore. The kiosk uses a Python CLI script. 

One Friday evening, they needed to add two features:
1.  **Akash's Task:** Add UPI payment status updates.
2.  **Divya's Task:** Add student bulk discount calculations.

Since they did not use Git, Akash edited the local file `kiosk.py` on the laboratory computer. At the same time, Divya copied `kiosk.py` to her USB drive to work from her laptop. 
*   Akash finished his UPI logic, saved it, and went home.
*   Divya returned, plugged in her USB, and copied her version of `kiosk.py` back to the laboratory computer, completely overwriting Akash's UPI code.
*   The next morning, the canteen opened. When students tried paying via UPI, the kiosk crashed, resulting in massive queues and angry customers. Akash and Divya spent the weekend arguing and manually rewriting the lost code.

On Monday, their team lead introduced them to Git. Now, they work on separate branches (`feature-upi` and `feature-discount`) and merge their code seamlessly. If a conflict occurs, Git alerts them immediately instead of silently overwriting.

---

### Core Analogies for Git

#### 1. RPG Savepoints (The Commit)
Think of Git like playing an adventure role-playing game (RPG) like Elden Ring or GTA. Before entering a dangerous boss fight, you save your game. 
*   If you fight the boss and die (your code breaks), you don't start the entire game from zero. You simply reload your last save point (commit).
*   In Git, a **commit** is your code's manual save point.

#### 2. The Kitchen Prep Station (The Staging Area)
Imagine you are a chef in a restaurant:
1.  **Working Directory:** Your chopping board. You chop onions, tomatoes, and herbs. Not everything on the board goes into the dish.
2.  **Staging Area:** The prep bowl. You select the exact amounts of chopped onions and tomatoes needed and place them in a bowl. You leave the raw scraps on the chopping board.
3.  **Local Repository:** The cooking pot. You dump the prep bowl contents into the hot oil. They are now cooked and permanently part of the meal (committed).

```
[ Chopping Board ]   ====== git add ======>   [ Prep Bowl ]   ====== git commit ======>   [ Cooking Pot ]
(Working Directory)                          (Staging Area)                                (Local Repo)
```

---

## 📚 Section 3: Git Architecture & States [00:25 - 00:45 | Duration: 20 mins]

### The 3 Local Git Areas
A local Git project is divided into three logical stages:

1.  **Working Directory (Sandbox):** The actual directory on your computer where you write, edit, and delete files. Git tracks these files, but they are not saved in your history yet.
2.  **Staging Area / Index (The Queue):** A conceptual middle area where you organize files that you want to include in your next commit. This allows you to selectively group changes.
3.  **Local Repository (The Vault):** The hidden `.git` folder where Git stores the metadata and database containing all snapshots (commits) of your project's history.

---

### File Status Lifecycle
Inside your working directory, files can be in one of the following states:

```
                  +--------------------------------+
                  |           Untracked            |
                  +---------------+----------------+
                                  |
                              git add
                                  |
                                  v
+-----------------+   git add   +------------------+
|    Modified     |------------>|      Staged      |
+--------+--------+             +--------+---------+
         ^                               |
         |  File                         | git commit
         |  Edited                       |
         |                               v
+--------+-------------------------------+---------+
|                   Unmodified                     |
+--------------------------------------------------+
```

*   **Untracked:** Git sees a new file in your directory but is ignoring it. It won't be saved in commits.
*   **Staged:** An untracked or modified file has been added to the staging area via `git add`. It is queued for the next snapshot.
*   **Committed (Unmodified):** The file has been safely saved in your local repository database.
*   **Modified:** A committed file has been changed in your working directory, but the changes are not yet staged.

---

### Branches: Parallel Universes
A branch in Git is simply a lightweight pointer to a specific commit. 
*   **`main` (or `master`):** The default branch representing your production-ready, stable codebase.
*   **Feature Branches (e.g., `feature-billing`):** Isolated sandbox branches where developers work on new tasks. They can commit changes independently without affecting the `main` branch.
*   **Merging:** Combining the changes from one branch into another.
*   **Merge Conflict:** Occurs when two branches modify the *same line* of the *same file* in different ways. Git doesn't know which version is correct and stops to ask the developer to manually select the correct code.

---

## 🎨 Section 4: Whiteboard Diagrams [00:45 - 00:55 | Duration: 10 mins]

### 1. Git Architecture Workflow
```
+------------------+         git add <file>        +------------------+
|                  | ----------------------------> |                  |
|  Working Dir     |                               |   Staging Area   |
|  (Local Files)   | <---------------------------- |     (Index)      |
|                  |     git restore <file>        |                  |
+------------------+                               +------------------+
         ^                                                   |
         |                                                   | git commit -m "msg"
         |                                                   v
         |                                         +------------------+
         |                                         |                  |
         +---------------------------------------- |    Local Repo    |
                    git checkout <commit>          |   (.git folder)  |
                                                   |                  |
                                                   +------------------+
                                                             |
                                                             | git push
                                                             v
                                                   +------------------+
                                                   |                  |
                                                   |    Remote Repo   |
                                                   |     (GitHub)     |
                                                   |                  |
                                                   +------------------+
```

### 2. Branching and Merging (Fast-Forward vs. Conflict Resolution)
**Scenario A: Fast-Forward Merge**
```
(Commit A) ➔ (Commit B) [main]
                    \
                     ➔ (Commit C) ➔ (Commit D) [feature-upi]
                     
After merging feature-upi into main:
(Commit A) ➔ (Commit B) ➔ (Commit C) ➔ (Commit D) [main, feature-upi]
```

**Scenario B: Three-Way Merge (Conflict Zone)**
```
                      ➔ (Commit C: Edited line 10 to 'X') [main]
                     /
(Commit A) ➔ (Commit B)
                     \
                      ➔ (Commit D: Edited line 10 to 'Y') [feature-upi]
```
*   *Result:* Git halts, highlighting line 10 with conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).

---

## 💬 Section 5: Teaching Script [00:55 - 01:10 | Duration: 15 mins]

**Instructor:** "Class, let's look at this blackboard. Let's say you are building a house. If you want to paint a room, you don't paint the final walls immediately. First, you might try a swatch on a piece of paper, tape it to the wall, and see how it looks. If it looks great, you apply it permanently. 

In programming, your **Working Directory** is your room. The swatch is the **Staging Area**. And the permanent paint is your **Commit**.

Let's do a quick roleplay. Divya, please stand up. You are the developer working on adding a GST calculator. Akash, you are working on a service tax calculator. Both of you start with the same baseline code from Wednesday. 

Divya, you open your terminal, type `git branch feature-gst` and hit enter. Git creates a parallel universe for you. Akash, you type `git branch feature-tax` and hit enter. Now, you both edit the exact same file, `billing.py`. 

Divya adds GST calculations to line 15. Akash adds service tax calculations to line 15. 

If Divya pushes her code first, it merges fine. But when Akash tries to merge his code, Git yells: *'Stop! Conflict detected on line 15!'* 

Why? Because Git is a machine. It doesn't know if we need GST, service tax, or both! It refuses to make a guess. It outputs markers showing Divya's changes and Akash's changes side-by-side. 

Now, they must sit together, decide to keep both lines, delete the markers, and make a new commit. This is the heart of version control: safety, clarity, and collaboration."

---

## 💻 Section 6: Live CLI Demo [01:10 - 01:40 | Duration: 30 mins]

Follow these exact steps in your terminal to practice Git workflows locally.

### Step 1: Initialize Git and Configure Profile
First, open your terminal and configure your identity. Git records this information with every commit so your team knows who wrote the code.

```powershell
# Configure global username and email
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Initialize a new project directory
mkdir coimbatore_billing
cd coimbatore_billing
git init
```
*Expected Output:*
```
Initialized empty Git repository in D:/New_Code_file/coimbatore_billing/.git/
```

---

### Step 2: Track Files and Make First Commit
Create a file, view its tracking state, stage it, and commit it.

```powershell
# Create main billing file
echo "print('=== COIMBATORE RETAIL BILLING SYSTEM ===')" > billing.py

# Check status
git status
```
*Expected Output:*
```
On branch main
No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        billing.py

nothing added to commit but untracked files present (use "git add" to track)
```

```powershell
# Stage the file
git add billing.py
git status
```
*Expected Output:*
```
On branch main
No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   billing.py
```

```powershell
# Commit with message
git commit -m "feat: initial release of billing core"
```
*Expected Output:*
```
[main (root-commit) 8a1f3c2] feat: initial release of billing core
 1 file changed, 1 insertion(+)
 create mode 100644 billing.py
```

---

### Step 3: Create a Branch and Add a Feature
Now, create a branch to build a discount calculation feature without affecting the `main` code.

```powershell
# Create and switch to new branch
git checkout -b feature-discount
# Alternatively in modern git: git switch -c feature-discount

# Add discount code to billing.py
echo "def calculate_discount(amount): return amount * 0.10" >> billing.py

# Stage and Commit on feature-discount branch
git add billing.py
git commit -m "feat: add 10% discount calculation logic"
```
*Expected Output:*
```
[feature-discount fc52b12] feat: add 10% discount calculation logic
 1 file changed, 1 insertion(+)
```

---

### Step 4: Induce a Merge Conflict (The Practical Lab)
We will now intentionally force a merge conflict to learn how to resolve it.

1.  **Modify the same line on `main` branch:**
    ```powershell
    # Switch back to main branch
    git checkout main
    
    # Notice that billing.py does not contain the discount function here!
    # Let's add a conflicting calculation to billing.py
    echo "def calculate_discount(amount): return amount * 0.05" >> billing.py
    
    # Stage and commit this change on main
    git add billing.py
    git commit -m "feat: add 5% promo discount core"
    ```

2.  **Attempt to merge the feature branch:**
    ```powershell
    # Merge feature-discount into main
    git merge feature-discount
    ```
    *Expected Output:*
    ```
    Auto-merging billing.py
    CONFLICT (content): Merge conflict in billing.py
    Automatic merge failed; fix conflicts and then commit the result.
    ```

---

### Step 5: Resolve the Merge Conflict
Open `billing.py` in your code editor. You will see the conflict markers inserted by Git:

```python
print('=== COIMBATORE RETAIL BILLING SYSTEM ===')
<<<<<<< HEAD
def calculate_discount(amount): return amount * 0.05
=======
def calculate_discount(amount): return amount * 0.10
>>>>>>> feature-discount
```

*   `<<<<<<< HEAD` represents the changes on your current branch (`main`).
*   `=======` separates the two versions.
*   `>>>>>>> feature-discount` represents the changes from the incoming branch (`feature-discount`).

**Resolution Action:**
Let's decide to merge both features or choose the higher 10% discount. Edit the file to remove conflict markers and keep the 10% logic:

```python
print('=== COIMBATORE RETAIL BILLING SYSTEM ===')
def calculate_discount(amount): return amount * 0.10
```

Now, finalize the merge:
```powershell
# Re-stage the resolved file
git add billing.py

# Commit the merge resolution
git commit -m "merge: resolve discount rate conflict by keeping 10% rate"
```
*Expected Output:*
```
[main 7d21ab3] merge: resolve discount rate conflict by keeping 10% rate
```

Check the log to verify your version history timeline:
```powershell
git log --oneline --graph
```
*Expected Output:*
```
*   7d21ab3 merge: resolve discount rate conflict by keeping 10% rate
|\  
| * fc52b12 feat: add 10% discount calculation logic
* | c410a56 feat: add 5% promo discount core
|/  
* 8a1f3c2 feat: initial release of billing core
```

---

## 📚 Section 7: GitHub & Collaboration Workflows [01:40 - 01:50 | Duration: 10 mins]

While Git runs locally on your machine, **GitHub** is a cloud-based hosting service for Git repositories, enabling collaborative development.

### Collaboration Concepts

*   **Remote:** A copy of your repository hosted on the internet (e.g., on GitHub).
*   **Clone:** Downloading an existing GitHub repository to your local machine:
    ```bash
    git clone https://github.com/user/repository.git
    ```
*   **Push:** Uploading your local commits to GitHub:
    ```bash
    git push origin main
    ```
*   **Fetch vs. Pull:**
    *   `git fetch` downloads remote updates but does *not* merge them into your local files. It is safe.
    *   `git pull` runs `git fetch` and then automatically merges the updates into your current branch.
*   **Forking:** Creating a personal copy of someone else's repository on your GitHub account, allowing you to freely experiment without affecting the original project.

---

### The Pull Request (PR) Lifecycle
A Pull Request is a proposal to merge changes from your branch into another developer's branch (usually `main`).

```
[ Developer ] -- Push branch --> [ GitHub Repo ] -- Open PR --> [ Tech Lead Review ]
                                                                      |
                                                                  Approve
                                                                      |
                                                                      v
                                                              [ Merge to Main ]
```

1.  Create a branch locally: `git checkout -b feature-alerts`.
2.  Write code, commit locally: `git commit -m "feat: notify user on low balance"`.
3.  Push the branch to GitHub: `git push origin feature-alerts`.
4.  Navigate to GitHub and click **"New Pull Request"**.
5.  Assign reviewers. They view the visual diff of your changes, comment on your code, and run automated tests.
6.  Once approved, the Tech Lead clicks **"Merge pull request"**, merging your changes into the production codebase.

---

## 📚 Section 8: Best Practices & Traps [01:50 - 01:55 | Duration: 5 mins]

### 1. The Power of `.gitignore`
Never commit temporary files, configuration settings, or system files. Create a `.gitignore` file in your repository root to tell Git what to ignore.

**Standard Python `.gitignore` Template:**
```gitignore
# Virtual environments
.venv/
env/
venv/
ENV/

# Python execution cache
__pycache__/
*.py[cod]
*$py.class

# Environment variables containing sensitive API keys
.env
secrets.json

# IDE config folders
.vscode/
.idea/

# Jupyter Notebook checkpoints
.ipynb_checkpoints/
```

---

### 2. Conventional Commit Messages
Write messages that describe *what* and *why* changes were made, not just *how*. Follow the Conventional Commits structure:

`type(scope): description`

*   `feat`: A new feature (e.g., `feat(auth): add google login`).
*   `fix`: A bug fix (e.g., `fix(billing): repair decimal rounding error`).
*   `docs`: Documentation changes (e.g., `docs: update setup instructions`).
*   `style`: Code style changes (whitespace, formatting, missing semi-colons).
*   `refactor`: Code restructuring without changing functional behavior.
*   `test`: Adding or correcting tests.

---

### 3. Git Security: Never Commit Secrets
> [!WARNING]
> **API Key Leakage:** Scraping bots crawl GitHub 24/7 searching for leaked API keys (OpenAI, Gemini, AWS). Committing an API key to a public repository can result in thousands of dollars of unauthorized API usage within minutes.
> **Action:** Always save keys in a local `.env` file, add `.env` to `.gitignore`, and use `os.environ` to access keys in Python.

---

## 📋 Section 9: Interview Questions & Answers [01:55 - 02:00 | Duration: 5 mins]

### Beginner Level (10 Questions)

1.  **What is the difference between Git and GitHub?**
    *   *Answer:* Git is a command-line tool that manages your project's version control locally. GitHub is a cloud hosting platform for Git repositories that enables sharing, collaboration, and project management.
2.  **What does `git init` do?**
    *   *Answer:* It creates a hidden `.git` folder in your current directory, initializing it as a Git repository.
3.  **What is the staging area in Git?**
    *   *Answer:* A middle ground between your working directory and local repository where you list and organize changes before committing them.
4.  **How do you view your commit history?**
    *   *Answer:* Using the `git log` command. To see a cleaner one-line graph, use `git log --oneline --graph`.
5.  **How do you stage a specific file named `app.py`?**
    *   *Answer:* Using `git add app.py`. To stage all modified files, use `git add .`.
6.  **What is a commit?**
    *   *Answer:* A snapshot of staged changes saved to your local repository database.
7.  **What is the default main branch name in modern Git?**
    *   *Answer:* `main` (historically `master`).
8.  **How do you create and switch to a new branch named `bugfix-login` in a single command?**
    *   *Answer:* `git checkout -b bugfix-login` (or `git switch -c bugfix-login`).
9.  **What command shows you which files are modified, staged, or untracked?**
    *   *Answer:* `git status`.
10. **How do you discard modifications in a file named `config.py` in your working directory?**
    *   *Answer:* `git restore config.py` (older Git used `git checkout -- config.py`).

---

### Intermediate Level (10 Questions)

11. **Explain the difference between `git merge` and `git rebase`.**
    *   *Answer:* `git merge` combines changes from a target branch into your current branch by creating a new merge commit, preserving historical timeline structures. `git rebase` moves the base of your current branch commits to the tip of the target branch, rewriting history to create a clean, linear sequence.
12. **What is a merge conflict and when does it occur?**
    *   *Answer:* A merge conflict occurs when Git attempts to merge two branches that modified the same line of the same file in different ways, or if a file was deleted in one branch but modified in another. Git stops and requires human intervention to select the final state.
13. **How does `git pull` differ from `git fetch`?**
    *   *Answer:* `git fetch` downloads remote tracking metadata and branches without modifying local working files. `git pull` fetches the remote changes and immediately attempts to merge them into the current active branch.
14. **What is the purpose of a `.gitignore` file? Give three examples of files that belong inside.**
    *   *Answer:* It tells Git which files or directories to permanently ignore from tracking. Examples: `.env` (secrets), `.venv/` (virtual environments), and `__pycache__/` (compiled bytecode).
15. **How do you undo a commit that has already been pushed to GitHub without rewriting history?**
    *   *Answer:* Using `git revert <commit-hash>`. This creates a new commit that performs the exact opposite changes of the target commit, keeping the version history linear and safe for teams.
16. **What does the command `git reset --hard HEAD~1` do?**
    *   *Answer:* It resets the current branch pointer to the previous commit, completely deleting all changes in the staging area and working directory. Any unsaved changes are permanently lost.
17. **What is a Detached HEAD state in Git?**
    *   *Answer:* A state where your HEAD pointer is pointing to a specific commit hash directly rather than to a local branch. Any new commits made here will not belong to a branch and can be lost during garbage collection unless committed to a new branch.
18. **How do you rename your last commit message?**
    *   *Answer:* Using `git commit --amend -m "new message"`. (Only do this for commits that haven't been pushed to a public remote).
19. **What is a "Fork" on GitHub?**
    *   *Answer:* A copy of a remote repository hosted on your personal account, allowing you to propose changes via Pull Requests to the original repository.
20. **How do you check what changes exist between your working directory and the staging area?**
    *   *Answer:* Using `git diff`. To check changes between the staging area and the local repository, use `git diff --staged`.

---

### Advanced Level (10 Questions)

21. **How does Git store commit structures internally? Explain the relationship between commits, trees, and blobs.**
    *   *Answer:* Git uses a content-addressed storage system. 
        *   **Blobs:** Store file contents (raw data) indexed by their SHA-1 hash (no filenames/metadata).
        *   **Trees:** Represent directory structures, holding lists of filenames, permissions, and pointers to blobs or other trees.
        *   **Commits:** Store pointers to a root tree (the directory state), parent commit hashes, author metadata, and message strings.
22. **What is the significance of the DAG (Directed Acyclic Graph) in Git?**
    *   *Answer:* Git represents commit history as a DAG, where each commit points backwards to its parent commit(s). It is "directed" (links go back in time) and "acyclic" (you cannot loop back to a future commit), enabling clean branch merges and historical lookups.
23. **What is the difference between `git reset --soft`, `--mixed`, and `--hard`?**
    *   *Answer:* 
        *   `--soft`: Moves the branch pointer but leaves the staging area and working directory unchanged (your changes remain staged).
        *   `--mixed` (default): Moves the branch pointer and updates the staging area to match, but leaves the working directory unchanged (changes are unstaged).
        *   `--hard`: Moves the branch pointer and clears the staging area and working directory (all changes are lost).
24. **How does Git detect that a file has been renamed?**
    *   *Answer:* Git does not store rename metadata. It evaluates file contents dynamically. If a deleted file and a newly added file share a high percentage of matching content (default 50% similarity index), Git shows it as a rename in `git status` or `git log`.
25. **What is `git cherry-pick` and when should you use it?**
    *   *Answer:* It applies the changes introduced by a specific, existing commit from another branch onto your current branch, creating a new commit. Use it when you need to merge a specific bugfix or feature commit from an experimental branch without merging the entire branch history.
26. **Explain the Reflog (`git reflog`) and how it can save lost work.**
    *   *Answer:* The reference log records every change made to local branch tips and HEAD (e.g., checkouts, resets, commits, rebases). Even if commits are deleted via a hard reset, they remain in the object database for a period. `git reflog` allows you to find their hashes and recover them.
27. **What are Git Hooks and how can you use them in production pipelines?**
    *   *Answer:* Git Hooks are scripts that run automatically at key points in the Git lifecycle (e.g., `pre-commit`, `commit-msg`, `pre-push`). They can block bad commits (e.g., rejecting commits containing API keys or failing PEP8 checks).
28. **How does Git handle garbage collection (`git gc`)?**
    *   *Answer:* Git optimizes the object database by packing loose objects (blobs, trees, commits) into compressed index packfiles and cleaning up dangling or unreachable objects that have been orphaned for longer than a specified expiry period.
29. **What is a Fast-Forward merge and when does it happen?**
    *   *Answer:* A merge where the target branch has no commits beyond the merged branch's base. Instead of creating a merge commit, Git simply moves the target branch pointer forward to point to the incoming branch's tip.
30. **Explain how `git bisect` works to find bugs.**
    *   *Answer:* It uses a binary search algorithm to find the exact commit that introduced a bug. You mark a "bad" commit where the bug is present, and a "good" commit in the past. Git checkouts commits in the middle, asking you to flag them as "good" or "bad" until it pinpoints the culprit.

---

## ❓ Section 10: FAQs [01:55 - 01:58 | Duration: 3 mins]

**Q: I ran `git add .` on my `.env` file containing API keys! Is it safe if I add it to `.gitignore` now?**  
**A:** No. `.gitignore` only ignores *untracked* files. Since the file was staged/tracked, it will still be committed. You must run `git rm --cached .env` to untrack it first, then commit.

**Q: My merge conflict markers look confusing. Can I abort the merge and start over?**  
**A:** Yes! Run `git merge --abort` to return your repository to the exact state before the merge attempt.

**Q: Can I use Git without GitHub?**  
**A:** Absolutely. Git operates entirely on your local machine. GitHub is only needed when sharing your repository with others or storing backups in the cloud.

---

## 📋 Section 11: Assignment Brief [01:58 - 02:00 | Duration: 2 mins]

### Coimbatore Smart Retail Kiosk Version Control
The student will create a local Git repository for a retail billing system. They will implement features, simulate team work by branching, create a merge conflict, resolve it, add a `.gitignore`, and tag the version as `v1.0.0`.

Refer to [04_Assignment.md](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day4_Git_and_GitHub/Day4_Teaching_content/04_Assignment.md) for full specifications.
