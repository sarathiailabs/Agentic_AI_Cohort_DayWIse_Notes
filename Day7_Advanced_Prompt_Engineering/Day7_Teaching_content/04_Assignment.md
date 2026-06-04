# 📝 Day 7 Assignment: Command-Line Resume Analyzer

---

## 🏢 Business Scenario

You work as a **Junior AI Engineer** at **TalentScout**, a rapidly growing HR-Tech startup. Recruiters at TalentScout review hundreds of resumes daily. They complain that:
1. Extracting candidate details manually is slow and error-prone.
2. Comparing candidates to diverse Job Descriptions (JDs) is highly subjective.
3. Giving constructive feedback and learning resources (courses/projects) to rejected candidates is time-consuming.

The CTO has tasked you with building a **proof-of-concept Command-Line Resume Analyzer**. The tool will take a candidate's resume (raw text) and a target Job Description, extract structured details, score the candidate's alignment, identify skill gaps, and query a local database tool to suggest learning resources for missing skills.

If the prototype succeeds, it will be integrated into the talent dashboard.

---

## 🎯 Project Objective

Build a modular, production-ready **Command-Line CLI tool** in Python that implements:
1. **System Prompt Rules**: Make the LLM act as an elite technical recruiter who is objective and detail-oriented.
2. **Structured Outputs**: Extract candidate metadata and alignment details into strict Pydantic schemas.
3. **Function/Tool Calling**: Register and execute a local database lookup function that retrieves course and project recommendations for identified skill gaps.
4. **Interactive CLI Loop**: Keep the application running with commands to `analyze`, view session `stats` (token usage and costs), `save` the JSON report, or `quit`.

---

## 📋 Technical & Functional Requirements

### 1. Project Directory Structure
All assignment code and files must reside inside:
`Day7_Advanced_Prompt_Engineering/Day7_Teaching_content/`

The required files are:
- `04_Assignment.md`: This instruction document.
- `05_Assignment_Solution.ipynb`: The complete runnable notebook solution.

*(Note: There is no separate duplicate assignment directory — all code solutions must be written and validated within the notebook `05_Assignment_Solution.ipynb`)*.

---

### 2. Functional Specifications

#### A. Structured Recruiter Output Schema
You must define a Pydantic model (`ResumeAnalysis`) containing the following structure:
- **Candidate Metadata**:
  - `candidate_name` (string)
  - `email` (string)
  - `phone` (string)
  - `current_role` (string)
  - `skills` (list of strings)
  - `years_of_experience` (float)
- **JD Alignment Analysis**:
  - `match_score` (integer, scale 0 to 100)
  - `missing_skills` (list of strings)
  - `alignment_explanation` (string, max 3 sentences explaining the rating)
- **Recommended Upskilling**:
  - `recommended_resources` (list of strings, populated by the database tool call)

#### B. Tool Calling: Upskilling Database
Define a local Python function to act as a database tool:
```python
def get_upskilling_resources(missing_skills: list[str]) -> str:
    \"\"\"Queries the TalentScout database to retrieve training courses and 
    practical projects for a list of missing technical skills.
    
    Args:
        missing_skills: A list of skill names (e.g. ['Docker', 'FastAPI'])
    \"\"\"
```
- Provide a mock dataset inside the function mapping common tech terms (e.g., *Kubernetes, FastAPI, Docker, PyTorch, React*) to specific courses and projects.
- The model must identify skill gaps, trigger the tool call with those gaps, and embed the results into the final `recommended_resources` output.

#### C. Interactive Console Interface
When run, the program must display a menu:
```
===================================================
      TALENTSCOUT: AI RESUME ANALYZER (CLI)
===================================================
Commands:
- analyze : Parse a resume against a job description
- stats   : Show total tokens consumed and session cost
- save    : Save the last analysis report to a JSON file
- quit    : Exit the program
===================================================
```
- **`analyze`**: Prompts the user to paste the raw resume text and job description, executes the agent, and displays the structured output neatly formatted in the terminal.
- **`stats`**: Keeps track of prompt tokens, completion tokens, and estimates costs using:
  - Input: $0.075 / 1 Million tokens
  - Output: $0.30 / 1 Million tokens
- **`save`**: Saves the last analyzed Pydantic report into a JSON file (e.g., `parsed_resume_[name].json`).

---

## 🏆 Evaluation Rubric

| Criteria | 4 Points (Exemplary) | 3 Points (Proficient) | 2 Points (Developing) | 1 Point (Unacceptable) |
| :--- | :--- | :--- | :--- | :--- |
| **System Prompt & Persona** | Detailed recruiter system prompt setting clear guidelines and security checks; model adheres strictly. | Recruiter system prompt is defined but lacks security parameters or details. | Rules are defined in user prompt instead of native system_instruction. | No system prompt or recruiter persona defined. |
| **Structured Output Schema** | Pydantic schema is fully defined with descriptions for all fields; data validation works perfectly. | Pydantic schema is defined, but missing fields or lacking field descriptions. | JSON mode is used but parsed manually via string manipulation or regex. | Output is returned as unstructured conversational text. |
| **Function Calling Loop** | Function calling correctly registered, automatically loops, handles errors, and populates resources. | Function calling registered, but fails to handle edge cases like empty skill inputs. | Mock resource outputs are hardcoded in prompts instead of calling the function. | Function calling is not implemented. |
| **CLI & State Management** | Robust command menu loop; `stats` and `save` commands work without crashing; logs token costs correctly. | Menu loop works, but missing `stats` or `save` functionality, or cost estimation is incorrect. | Interactive loop exists but crashes on invalid inputs or wrong commands. | Commands must be ran by modifying variables in the script manually. |
| **Code Quality & uv Setup** | Clean, modular code; functions have detailed docstrings; uses env variables; runs via `uv`. | Script runs, but lacks modularity (e.g. written in a single block) or has poor error handling. | API keys are hardcoded in code; no try-except safety. | Code contains syntax errors and does not compile. |

---

## 📥 Submission Instructions
Students must write the solution directly within the Jupyter Notebook file [05_Assignment_Solution.ipynb](file:///d:/New_Code_file/sarathiAILabsTeachingNotes/Agentic_AI_Cohort_DayWIse_Notes/Day7_Advanced_Prompt_Engineering/Day7_Teaching_content/05_Assignment_Solution.ipynb) located in their Day 7 workspace directory.
All code cells must be runnable, clean, and well-commented.
