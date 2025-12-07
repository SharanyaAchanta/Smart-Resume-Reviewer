

---

# 🔐 SECURITY POLICY

**Smart-Resume-Reviewer**

This document defines how the Smart-Resume-Reviewer project handles uploaded resume data, what security practices contributors must follow, and how vulnerabilities should be reported.

The project processes **highly sensitive personal information** (resume PDFs), therefore all contributors must strictly follow this policy.

---

## 📌 1. Scope of Data Processed

The Smart-Resume-Reviewer application accepts **PDF resume files** from users and extracts text for analysis.

The data may include:

* Full name
* Contact details
* Education & work history
* Skills, projects, and personal information

No other user data is collected or required.

---

## 📁 2. Handling of Uploaded Resume Files

### ✔ File Storage

* Uploaded resumes should **only be stored temporarily** for extraction.
* Files must be processed **in-memory whenever possible**.
* If temporary disk storage is necessary, files must be saved only in the system’s **temporary directory**.

### ✔ Retention

* Uploaded resume files must be **deleted immediately after processing**.
* The project **must not** retain, store, or reuse user resumes for training, testing, or analytics.

### ✔ Access Control

* No uploaded resume should be accessible through publicly exposed URLs.
* Only the server process handling the request may access the file.

---

## 🧹 3. Temporary Files & Cleanup Rules

* Any temporary files created during PDF extraction must be **removed as soon as parsing is complete**.
* No resume files should remain on disk after the request is processed.
* Contributors must ensure no temporary folders containing user files get committed.

Add any temporary directories in local development to `.gitignore`.

---

## 📄 4. Logging & Debugging Policy

Because resumes contain personal data:

### ❌ Not Allowed

* Logging **full resume text**
* Logging **personal information** such as email, phone number, address, education, or experience
* Printing sensitive data during debugging

### ✔ Allowed

* Logging status messages such as:

  * “File upload received”
  * “Extraction successful”
  * “Invalid PDF format”
* Error logs must **never** include the content of the uploaded file.
* Debug messages must be strictly metadata-only.

---

## 🛡 5. Contributor Security Requirements

### ✔ Use Only Dummy / Synthetic Resumes for Testing

* Contributors must **never use real personal resumes** for debugging or testing.
* Only anonymized or fake sample PDFs should be used.

### ✔ Git Hygiene

* Never commit any uploaded user files to the repository.
* Ensure directories used for uploads are added to `.gitignore`.
* Remove any sensitive artifacts before pushing code.

### ✔ Code Practices

* Avoid adding any functionality that exposes uploaded files publicly.
* Keep dependencies updated, especially PDF parsers used by the project.
* Review library versions for known vulnerabilities.

---

## 🔒 6. Privacy & Data Protection

* Smart-Resume-Reviewer does **not store**, **share**, or **reuse** user resume data.
* Data is used *only once* for extracting text and generating feedback.
* No data is transmitted to third-party services.
* The system performs **stateless processing**, ensuring no personal data remains after completion.

---

## 🚨 7. Reporting Vulnerabilities

We welcome responsible disclosure.

If you discover a security issue in this project:

### 📩 Report via:

* GitHub **Security Advisories**
* GitHub **Issues** (with the “Security” label)

### When reporting, please include:

* Description of the vulnerability
* Steps to reproduce
* Impact assessment (if known)
* Recommended mitigation (optional)

### We Will:

* Acknowledge receipt
* Investigate promptly
* Provide a fix or mitigation as soon as possible

---

## 📎 8. Related Documentation

The main `README.md` will include a link pointing to this security policy.

---
