# Smart-Resume-Reviewer
An AI-powered resume analyzer and improvement assistant.
# Check out the app now
https://smart-resume-reviewer-oygjhtx9qnhf4iztnprmcg.streamlit.app/
# Smart Resume Reviewer 🧠📄

**Smart Resume Reviewer** is an open-source tool that helps job seekers improve their resumes with AI-powered suggestions. Upload your resume and get tips to enhance formatting, missing sections, relevant keywords, and more.

---

## 🚀 Features

- Upload PDF resume
- Extracts and displays resume content
- Highlights weak areas (e.g., no project section, outdated skills)
- Provides improvement suggestions based on selected job roles
- Beginner-friendly and extensible project

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









