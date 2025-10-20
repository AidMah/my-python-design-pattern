# Python Design Patterns - Course Branches Guide

## Overview
This repository contains the complete LinkedIn Learning course "Python Design Patterns" with all lesson branches available locally. Each branch represents either the starting code ("begin") or completed code ("end") for specific course sections.

## Repository Information
- **Course:** Python Design Patterns
- **Platform:** LinkedIn Learning (Original Source)
- **Repository:** python-design-patterns-2422610 (LOCAL COPY - Disconnected from remote)
- **Total Branches:** 31 local branches
- **Current Branch:** 02_06e
- **Status:** 🔓 Independent local repository (no remote connection)

## Branch Naming Convention
```
XX_YYz
├── XX = Chapter Number (02, 03, 04)
├── YY = Section Number (02, 06, 08, 12, 14, etc.)
└── z  = State (b = Begin, e = End)
```

---

## 📚 Chapter 2: Creational Patterns

### Section 2.2 - Singleton Pattern
- **02_02b** - Singleton Pattern (Begin)
- **02_02e** - Singleton Pattern (End)

### Section 2.6 - Abstract Factory Pattern
- **02_06b** - Abstract Factory Pattern (Begin)
- **02_06e** - Abstract Factory Pattern (End) ⭐ *Current Branch*

### Section 2.8 - Builder Pattern
- **02_08b** - Builder Pattern (Begin)
- **02_08e** - Builder Pattern (End)

### Section 2.12 - Prototype Pattern
- **02_12b** - Prototype Pattern (Begin)
- **02_12e** - Prototype Pattern (End)

### Section 2.14 - Factory Method Pattern
- **02_14b** - Factory Method Pattern (Begin)
- **02_14e** - Factory Method Pattern (End)

---

## 📚 Chapter 3: Structural Patterns

### Section 3.2 - Decorator Pattern
- **03_02b** - Decorator Pattern (Begin)
- **03_02e** - Decorator Pattern (End)

### Section 3.6 - Adapter Pattern
- **03_06b** - Adapter Pattern (Begin)
- **03_06e** - Adapter Pattern (End)

### Section 3.8 - Composite Pattern
- **03_08b** - Composite Pattern (Begin)
- **03_08e** - Composite Pattern (End)

### Section 3.10 - Bridge Pattern
- **03_10b** - Bridge Pattern (Begin)
- **03_10e** - Bridge Pattern (End)

### Section 3.14 - Facade Pattern
- **03_14b** - Facade Pattern (Begin)
- **03_14e** - Facade Pattern (End)

---

## 📚 Chapter 4: Behavioral Patterns

### Section 4.2 - Observer Pattern
- **04_02b** - Observer Pattern (Begin)
- **04_02e** - Observer Pattern (End)

### Section 4.6 - Strategy Pattern
- **04_06b** - Strategy Pattern (Begin)
- **04_06e** - Strategy Pattern (End)

### Section 4.8 - Command Pattern
- **04_08b** - Command Pattern (Begin)
- **04_08e** - Command Pattern (End)

### Section 4.10 - State Pattern
- **04_10b** - State Pattern (Begin)
- **04_10e** - State Pattern (End)

### Section 4.14 - Template Method Pattern
- **04_14b** - Template Method Pattern (Begin)
- **04_14e** - Template Method Pattern (End)

---

## 🚀 Quick Start Commands

### Switch to a specific pattern
```bash
# Example: View the completed Singleton pattern
git checkout 02_02e

# Example: Start working on the Adapter pattern
git checkout 03_06b

# Example: See the finished Observer pattern implementation
git checkout 04_02e
```

### Compare patterns
```bash
# Compare begin vs end state of a pattern
git diff 02_06b 02_06e

# View files changed in a specific pattern
git diff --name-only 03_08b 03_08e
```

### List all branches
```bash
# Show all local branches
git branch

# Show all branches (local and remote)
git branch -a
```

### Return to main course branch
```bash
git checkout main
```

---

## 📋 Study Workflow Suggestions

### 1. **Linear Learning Path**
Follow chapters in order: Ch2 → Ch3 → Ch4

### 2. **Pattern-by-Pattern Study**
For each pattern:
1. Start with the "begin" branch (`XX_YYb`)
2. Study the existing code structure
3. Switch to "end" branch (`XX_YYe`) 
4. Compare the differences
5. Practice implementing on your own

### 3. **Pattern Comparison**
Compare similar patterns:
- Factory Method vs Abstract Factory (02_14e vs 02_06e)
- Decorator vs Adapter (03_02e vs 03_06e)
- Strategy vs State (04_06e vs 04_10e)

---

## 🎯 Design Pattern Categories

### **Creational Patterns** (Chapter 2)
Focus on object creation mechanisms
- Singleton, Abstract Factory, Builder, Prototype, Factory Method

### **Structural Patterns** (Chapter 3) 
Deal with object composition and relationships
- Decorator, Adapter, Composite, Bridge, Facade

### **Behavioral Patterns** (Chapter 4)
Concerned with communication between objects and assignment of responsibilities
- Observer, Strategy, Command, State, Template Method

---

## 📝 Notes
- Each branch is set up to track its corresponding remote branch
- All remote branches have been checked out locally for offline access
- The `main` branch contains the base course structure
- Use `git status` to check your current branch
- Files may vary between branches - this is expected as each represents different lesson states

---

## 🔓 Repository Status: DISCONNECTED

This repository has been **disconnected from the original LinkedIn Learning remote repository**. 

### What this means:
- ✅ All course content remains available locally across 31 branches
- ✅ You can make changes, commits, and modifications freely
- ✅ No risk of accidentally pushing changes to the original course repository
- ❌ Cannot pull updates from the original repository (not needed for course content)
- ❌ No remote backup (consider setting up your own remote if needed)

### If you want to reconnect or create your own remote:
```bash
# To add your own remote repository
git remote add origin <your-repository-url>

# To push to your own repository
git push -u origin main
```

---

*Generated on: October 20, 2025*  
*Last Updated: Disconnected from original remote repository*