
# 🌟 Contributing to **Smart Resume Reviewer**

Thank you for your interest in contributing to **Smart Resume Reviewer**!
Your contributions help improve the project and empower users to review resumes smarter and faster.
Please follow the guidelines below to ensure smooth collaboration.

---

## 🚀 Contribution Workflow (Must Follow)

### **1. Create an Issue First**

Before starting any work:

* Open a **new issue** describing your feature, improvement, or bug fix.
* Provide as much detail as possible:

  * What you plan to change
  * Why the change is important
  * Screenshots/logs (if applicable)

This avoids duplicate work and helps maintainers review the proposal.

### **2. Wait Until the Issue Is Assigned**

**Do NOT start working immediately.**
A maintainer will:

* Review your issue
* Ask clarifying questions (if needed)
* Assign the issue to you

Only start contributing **after you are officially assigned** to avoid conflicts with other contributors.

### **3. Fork the Repository**

Once assigned, click **Fork** on GitHub to copy the project to your account.

### **4. Clone Your Fork**

```bash
git clone https://github.com/your-username/Smart-Resume-Reviewer.git
cd Smart-Resume-Reviewer
```

### **5. Create a New Branch**

Use a descriptive branch name:

```bash
git checkout -b issue-<number>-short-description
```

Example:

```
git checkout -b issue-12-add-dark-mode
```

### **6. Make Your Changes**

* Follow project structure
* Write clean, commented, and modular code
* Ensure performance and readability
* Update documentation if needed

### **7. Install Dependencies & Test Locally**

```bash
pip install -r requirements.txt
streamlit run app.py
```

Verify your changes thoroughly before submitting.

### **8. Commit and Push**

```bash
git add .
git commit -m "Fix: detailed description (issue #<number>)"
git push origin issue-<number>-short-description
```

### **9. Open a Pull Request**

Go to the **original repo** → **Pull Requests** → **New Pull Request**

In your PR description:

* Clearly explain what you changed
* Link the issue using:

  ```
  Closes #<issue-number>
  ```
* Include screenshots (if UI-related)

---

## 🐞 Reporting Issues

If you find a bug or want a feature:

1. Open an issue
2. Provide clear reproduction steps
3. Add screenshots/logs if applicable
4. Wait for a maintainer to assign you

---

## 📐 Coding Standards

* Follow **PEP8** for Python
* Use meaningful variable and function names
* Keep code modular and maintainable
* Add docstrings where helpful
* Avoid unused imports and redundant code

---

## 📄 Commit Message Guidelines

Follow conventional commits:

```
feat: add new resume section analyzer
fix: resolve file upload crash
docs: improve README and contributing guide
refactor: optimize text preprocessing logic
style: formatting and indentation fixes
```

---

## 🧪 Pull Request Checklist

Before submitting your PR:

* [ ] Issue created and assigned
* [ ] Branch name follows convention
* [ ] Code runs without errors
* [ ] No debug prints left
* [ ] Documentation updated if necessary
* [ ] PR description is clear and complete

---

## 🤝 Need Help?

If you’re unsure about anything:

* Ask in the issue
* Start a discussion
* Tag a maintainer

We’re here to help you contribute comfortably!

---

## ❤️ Thank You!

Every contribution — big or small — helps improve **Smart Resume Reviewer**.
We truly appreciate your efforts and enthusiasm! 🚀✨

