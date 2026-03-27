# Copilot Instructions for Python Design Patterns

## Project Overview

This is a **LinkedIn Learning course repository** showcasing 15 essential design patterns in Python. It's structured as a teaching tool with branches corresponding to course videos, not a traditional library or framework.

### Key Context
- **Purpose**: Educational examples of design patterns (creational, structural, behavioral)
- **Branch Structure**: Branches follow naming convention `CHAPTER#_MOVIE#` with `b` (beginning) and `e` (end) states for each lesson
- **Current Branch**: `04_06e` (Chapter 4, Movie 6, end state)
- **Learning Flow**: Switch between branches to see code at different lesson stages

## Architecture & Patterns

Each branch demonstrates a specific design pattern through self-contained Python examples. The `visitor_final.py` exemplifies the **Visitor Pattern**:

- **Element class** (`House`): Defines `accept(visitor)` method to receive visitors
- **Visitor classes** (`HvacSpecialist`, `Electrician`): Implement pattern-specific logic through `visit(element)` method
- **Pattern benefit**: Separates concerns—House doesn't know about specialist behaviors; specialists encapsulate their work

### Design Pattern Template
When implementing patterns in this repo:
1. Create a minimal **Element/Subject class** with `accept()` method
2. Define an **abstract Visitor class** with interface contract
3. Implement **concrete Visitor subclasses** with pattern-specific behavior
4. Keep examples simple—illustrate the pattern, not production code

## Workflow & Development

### Branch Navigation
```powershell
# View all available branches (tagged by CHAPTER#_MOVIE#)
git branch -a

# Switch to a specific lesson branch
git checkout 02_03b  # Chapter 2, Movie 3, beginning

# View changes from beginning to end of a lesson
git diff 02_03b..02_03e
```

### Before Switching Branches
Always commit or stash local changes to avoid checkout errors:
```powershell
git add .
git commit -m "Lesson notes: [topic]"
# OR: git stash
```

### File Locations
- **Main pattern examples**: Root-level `.py` files (e.g., `visitor_final.py`, `factory_pattern.py`)
- **Diagrams**: PlantUML files (`.puml`) show pattern relationships (see `visitor_diagram.puml`)
- **Docs**: `README.md` explains course structure; `CONTRIBUTING.md` notes this is read-only

## Code Conventions

### Python Style
- **Simple, readable examples**: Prioritize clarity over Pythonic idioms
- **Comments**: Explain *why* the pattern is used, not just *what* code does (see `visitor_final.py` inline comments)
- **Class docstrings**: Use single-line docstrings describing role in pattern
- **Print statements**: Use `print()` for demo output (not logging)

### Naming
- **Element/Subject**: Named descriptively (e.g., `House`, `Document`)
- **Visitors**: Concrete visitors describe their specialization (e.g., `HvacSpecialist`, `Electrician`)
- **Abstract base**: Use `Visitor(object)` pattern; docstring clarifies it's abstract

## Key Files to Reference

| File | Purpose |
|------|---------|
| `visitor_final.py` | Complete Visitor pattern example—reference for pattern structure |
| `visitor_diagram.puml` | UML diagram of pattern relationships—good for understanding connections |
| `README.md` | Course metadata, branch structure explanation |
| `.github/ISSUE_TEMPLATE.md` | PR/issue guidelines (read-only repo) |

## Common Tasks

### Analyze a Pattern Implementation
1. Read the `.py` file to see concrete classes
2. Check the corresponding `.puml` diagram for relationships
3. Identify Element (accepts visitors) vs. Visitor (performs work) separation

### Switch to a New Lesson
1. Commit current changes: `git commit -m "msg"`
2. List branches: `git branch -a` (filter by chapter if large number)
3. Checkout: `git checkout CHAPTER#_MOVIE#[b|e]`
4. Review differences: `git diff HEAD..origin/HEAD`

### Extend an Example (Advanced)
- Follow the Visitor pattern template (Element + Abstract Visitor + Concrete Visitors)
- Keep examples under 100 lines for clarity
- Add comments explaining pattern role
- Update `.puml` diagram if modifying relationships

## No External Dependencies

This repo has **no package requirements**—use only Python stdlib. Examples run directly:
```powershell
python visitor_final.py
```

## Important Notes

- **No Contributions Accepted**: This is a read-only educational repo (see `CONTRIBUTING.md`)
- **Master Branch**: Contains final state of all course material
- **Commit Changes Locally**: Use git commits to track your learning progress across branches
