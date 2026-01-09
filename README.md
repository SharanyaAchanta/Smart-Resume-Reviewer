<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<div align="center"><img src="assets/SRR-logo.png" style="width: 220px; height: 220px;"  alt="Smart-Resume-Review Logo" /></div>

<h1 align="center">Smart Resume reviewer</h1>

<div align="center" style="margin: 10px 0 24px;">
  <a href="https://github.com/SharanyaAchanta/Smart-Resume-Reviewer/issues">🐛 Report Bug</a>
  •
  <a href="https://github.com/SharanyaAchanta/Smart-Resume-Reviewer/issues">💡 Request Feature</a>
  
</div>

 <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<!-- Add Table of Content -->

## 📑 Table of Contents

- [🔍 Overview](#overview)
- [🤔 Why Smart-Resume-Reviewer?](#why-smart-resume-reviewer?)

  - [🔐 Privacy & Trust](#citizen-portal)
  - [⚡ Fast & Distraction-Free](#employee-portal)
  - [🏆 Proven Results](#admin-portal)
  - [🎯 Flexible for All Career Paths](#admin-portal)

- [🚀 Live Demo](#demo)
- [🌟 Key Features](#key-features)
  - [👤 Citizen Portal](#citizen-portal)
  - [🧑‍💼 Employee Portal](#employee-portal)
  - [🛡️ Admin Portal](#admin-portal)
- [🛠️ Technologies Used](#technologies-used)
  - [Frontend](#frontend)
  - [Backend](#backend)
  - [DevOps & Automation](#devops--automation)
- [🤖 Automated Dependency Management](#automated-dependency-management)
- [🧭 Project Flowchart](#flowchart)
- [⚙️ Installation and Setup](#installation-setup)
  - [📋 Prerequisites](#prerequisites)
  - [Backend Setup](#installation-setup)
  - [Frontend Setup](#installation-setup)
- [🛠️ Troubleshooting](#troubleshooting)
- [✴ Issue Creation](#issue-creation)
- [📑 Contribution Guidelines](#contribution-guidelines)
- [📞 Contact](#contact)
- [🤝 Contributing](#contributing)
  - [Ways to Contribute](#ways-to-contribute)
- [📜 Code of Conduct](#code-of-conduct)
- [💡 Suggestions & Feedback](#suggestions-feedback)
- [🙌 Show Your Support](#show-your-support)
- [📄 License](#license)
- [⭐ Stargazers](#stargazers)
- [🍴 Forkers](#forkers)

---

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<!-- Rest of existing content continues... -->

<h2 id="overview">🔍 Overview</h2>

Smart Resume Reviewer is a privacy-first, AI-powered resume analysis tool designed to help users create highly ATS-compatible resumes with clarity and confidence.

It analyzes resumes to identify:

- Missing or weak sections
- Outdated or irrelevant skills
- Formatting issues that reduce ATS shortlisting chances

Users can upload their resume and receive instant, actionable AI-driven suggestions to improve content, structure, and overall resume quality — without distractions or delays.

Built for real-world hiring standards, this project is trusted by students, freshers, and professionals preparing for competitive job applications across industries.

<h2 id="why-smart-resume-reviewer?">🤔 Why Smart-Resume-Reviewer?</h2>

### 🔐 Privacy & Trust

Smart Resume Reviewer is built with user trust as a top priority.

- We do **not store resumes**
- We do **not collect personal data**
- We do **not sell or share data for ads**
- Uploaded resumes are processed instantly and removed after analysis

Your resume stays private, secure, and under your control at all times.

### ⚡ Fast & Distraction-Free

This app is designed for users who want results — not distractions.

- No unnecessary sign-ups
- No ads or pop-ups
- No long waiting times

Users upload a resume and receive analysis within a few seconds.
The interface is simple, clean, and focused only on resume improvement.

### 🏆 Proven Results

Many users of Smart Resume Reviewer have successfully improved their resumes
and secured opportunities at top tech companies, including FAANG-level organizations.

The tool focuses on real ATS requirements and industry expectations,
making it practical and result-oriented rather than theoretical.

### 🎯 Flexible for All Career Paths

Smart Resume Reviewer supports a wide range of roles and disciplines.

- Software & IT roles
- Data, AI, and ML profiles
- Core engineering branches
- Management, business, and non-tech roles

It provides multiple resume templates and suggestions
tailored to different career paths and experience levels.

## 🔍 How This App Is Different

Unlike many resume tools that focus only on scores or visuals,
Smart Resume Reviewer focuses on clarity, trust, and real-world hiring needs.

- Privacy-first approach with zero data retention
- ATS-focused analysis instead of surface-level feedback
- Instant results without distractions
- Open-source and transparent logic
- Designed to help users learn and improve, not confuse them

The goal is simple: help users submit better resumes with confidence.

 <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 id="demo">🚀 Live Demo</h2>

- **[Smart-Resume-Reviewer](https://gamehub-codesocial.netlify.app/)**

 <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

---

## 🚀 Features

### i) Resume Analysis

- Upload PDF resume
- Extracts and displays resume content

### ii) AI Suggestions

- Highlights weak areas (missing sections, outdated skills)
- Provides role-based improvement suggestions

### iii) Developer Friendly

- Beginner-friendly codebase
- Easy to extend and customize

---

## 🌐 Tech Stack

- **Frontend**: HTML/CSS(For styling purpose)
- **Backend**: Python (Streamlit)
- **AI Logic**: Rule-based or prompt-based suggestions
- **PDF Parsing**: PyMuPDF / pdfminer.six

---

## 📁 Project Structure

```C:.
Smart-Resume-Reviewer/
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
│
├── assets/
│   └── logo_Pixel.png
│
├── components/
│   ├── contributors.py
│   ├── features.py
│   ├── footer.py
│   ├── header.py
│   ├── styles.py
│   ├── suggestions.py
│   └── upload_card.py
│
├── data/
│   ├── Resume1.pdf
│   └── Resume2.pdf
│
├── static/
│   ├── css/
│   └── prevent_double_submit.js
│
├── utils/
│   ├── analyze_resume.py
│   ├── job_roles.json
│   └── resume_parser.py
│
├── .gitignore
├── app.py
├── CONTRIBUTING.md
├── LICENSE
├── package-lock.json
├── README.md
├── requirements.txt
└── SECURITY.md

```

---

## 🚀 Project Setup

### 1️⃣ Create Virtual Environment

    virtualenv venv
    ./venv/Scripts/activate

### 2️⃣ Install Dependencies

    pip install -r requirements.txt

### 3️⃣ Run the Application

    streamlit run app.py

---

## ✨ Contributors

Thanks to all the wonderful contributors 💖

<a href="https://github.com/SharanyaAchanta/Smart-Resume-Reviewer/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=SharanyaAchanta/Smart-Resume-Reviewer" />
</a>

See full list of contributors 👉 [Contribution Graph](https://github.com/SharanyaAchanta/Smart-Resume-Reviewer/graphs/contributors)

  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 id="suggestions-feedback">💡 Suggestions & Feedback</h2>

Feel free to open issues or discussions if you have any feedback, feature suggestions, or want to collaborate!

  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 id="show-your-support">🙌 Show Your Support</h2>

_If you find Smart-Resume-Reviewer project helpful, give it a star! ⭐ to support more such educational initiatives:_

- ⭐ **Starring the repository**
- 🐦 **Sharing on social media**
- 💬 **Telling your friends and colleagues**
- 🤝 **Contributing to the project**

  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 id="license">📄 License</h2>

This project is licensed under the MIT License - see the [`License`](https://github.com/SharanyaAchanta/Smart-Resume-Reviewer?tab=MIT-1-ov-file) file for details.

  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 id="stargazers">⭐ Stargazers</h2>

<div align="center">
  <a href="https://github.com/SharanyaAchanta/Smart-Resume-Reviewer/stargazers">
    <img 
      src="https://reporoster.com/stars/SharanyaAchanta/Smart-Resume-Reviewer?type=svg&limit=20&names=false" 
      alt="Stargazers"
    />
  </a>
</div>

<h2 id="forkers">🍴 Forkers</h2>

<div align="center">
  <a href="https://github.com/SharanyaAchanta/Smart-Resume-Reviewer/network/members">
    <img 
      src="https://reporoster.com/forks/SharanyaAchanta/Smart-Resume-Reviewer?type=svg&limit=20&names=false" 
      alt="Forkers"
    />
  </a>
</div>

---

<h1 align="center"><img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Glowing%20Star.png" alt="Glowing Star" width="25" height="25" />  Loved by the community👥, trusted by contributors 🧑‍🤝‍🧑 worldwide 🌍 <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Glowing%20Star.png" alt="Glowing Star" width="25" height="25" /></h1>

<h3 align="center"> 👨‍💻 Built with care 🫶 to create ATS-friendly resumes — fast, smart, and distraction-free ✨</h3>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=65&section=footer"/>

<p align="center">
  <a href="#top" style="font-size: 18px; padding: 8px 16px; display: inline-block; border: 1px solid #ccc; border-radius: 6px; text-decoration: none;">
    ⬆️ Back to Top
  </a>
</p>

> Ready to show off your coding achievements? Get started with **Smart-Resume-Reviewer** today! 🚀

 <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">
