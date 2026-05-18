# AI Agents Learning Journey

## Folder Structure
<img width="478" height="598" alt="Screenshot 2026-05-18 at 10 56 56 AM" src="https://github.com/user-attachments/assets/d7c48237-02cf-41d6-9cc7-004a4992af23" />

## Mono repo Pros and Cons 
<img width="485" height="109" alt="Screenshot 2026-05-18 at 10 57 12 AM" src="https://github.com/user-attachments/assets/748815da-1ad4-4687-b4da-bb5c0bd06c66" />

## How to add a new project

### Step 1 — Create the folder structure

```bash
# From inside ai-agents-journey/ (always start from root)
mkdir -p phase-X-name/project-name
cd phase-X-name/project-name
```

### Step 2 — Create the project files

```bash
# Create a .env file for secrets (never commit this)
touch .env

# Create a .env.example (safe to commit, has dummy values)
cat > .env.example << 'EOF'
API_KEY=your_key_here
EOF

# Create the main file
touch main.py

# Create a project README
touch README.md
```

### Step 3 — Set up an isolated Python environment (venv)

Each project gets its own venv — like a separate pom.xml in Spring Boot.
Never share a venv between projects.

```bash
# Run this once when starting a new project
python3 -m venv .venv

# Activate it (run this every time you open a terminal)
source .venv/bin/activate        # Mac/Linux
# .venv\Scripts\activate         # Windows

# Your terminal should now show (.venv) prefix
# Install dependencies
pip install <package-name>

# Always save dependencies after installing
pip freeze > requirements.txt

# When done working, deactivate
deactivate
```

### Step 4 — Commit to GitHub

```bash
# Always run from repo root, not from inside the project folder
cd ../../

git add phase-X-name/
git commit -m "phase-X: add project-name"
git push
```

---

## Cheatsheet

| Task | Command |
|---|---|
| Create new project folder | `mkdir -p phase-X/project-name` |
| Create venv | `python3 -m venv .venv` |
| Activate venv (Mac/Linux) | `source .venv/bin/activate` |
| Activate venv (Windows) | `.venv\Scripts\activate` |
| Install a package | `pip install package-name` |
| Save dependencies | `pip freeze > requirements.txt` |
| Restore dependencies | `pip install -r requirements.txt` |
| Deactivate venv | `deactivate` |
| Commit and push | `git add . && git commit -m "msg" && git push` |

---

## Rule to remember

> One project folder = one venv.
> Always activate the venv before writing or running any code.
> Always run git commands from the repo root.

