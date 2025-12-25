import json

def detect_sections(text):
    text_lower = text.lower()

    sections = {
        "Education": ["education", "qualification", "academics"],
        "Skills": ["skills", "technical skills", "skills summary"],
        "Projects": ["projects", "project experience"],
        "Experience": ["experience", "work experience", "employment"],
        "Certifications": ["certification", "certifications", "courses"],
        "Achievements": ["achievements", "awards", "honors"],
    }

    missing_sections = []

    for section, keywords in sections.items():
        if not any(keyword in text_lower for keyword in keywords):
            missing_sections.append(section)

    return missing_sections


def get_resume_feedback(text, selected_role, job_description="", experience_level="Mid Level"):
    text_lower = text.lower()
    suggestions = []
    
    # --- 1. Basic Checks ---
    if "project" not in text.lower():
        suggestions.append("Add a 'Projects' section to highlight your work.")
    if "internship" not in text.lower() and experience_level in ["Entry Level", "Mid Level"]:
        suggestions.append("Include details of any internships you've completed.")
    if "github" not in text.lower() and "portfolio" not in text.lower():
        suggestions.append("Add your GitHub or portfolio link.")
    if "objective" not in text.lower() and experience_level == "Entry Level":
        suggestions.append("Consider adding an objective or summary at the top.")

    # --- 2. Missing Sections ---
    missing_sections = detect_sections(text)
    if missing_sections:
        suggestions.append(f"Missing important sections: {', '.join(missing_sections)}.")

    # --- 3. Keyword Matching ---
    try:
        with open("utils/job_roles.json", "r") as f:
            job_roles = json.load(f)
        
        # Flattens nested dictionary structure to find role keywords
        role_keywords = []
        for cat in job_roles.values():
            if selected_role in cat:
                role_keywords = cat[selected_role].get("required_skills", [])
                break
    except Exception:
        role_keywords = []

    # Enhance with JD keywords if provided
    if job_description:
        # Simple extraction of long words
        jd_words = [w.strip(".,()") for w in job_description.lower().split() if len(w) > 5]
        role_keywords.extend(jd_words[:5]) # add top 5 long words from JD
        role_keywords = list(set(role_keywords))

    missing_keywords = []
    for keyword in role_keywords:
        if keyword.lower() not in text_lower:
            missing_keywords.append(keyword)

    if missing_keywords:
        suggestions.append(f"Missing key skills for {selected_role}: {', '.join(missing_keywords[:7])}.")

    # --- 4. Scoring ---
    total_keywords = len(role_keywords)
    matched_keywords = total_keywords - len(missing_keywords)
    
    if total_keywords > 0:
        keyword_match = int((matched_keywords / total_keywords) * 100)
    else:
        keyword_match = 100

    resume_score = 50 + (keyword_match * 0.4)
    if not missing_sections: resume_score += 10
    
    # Experience Level Penalties
    word_count = len(text.split())
    if experience_level == "Entry Level" and word_count > 700:
        resume_score -= 5
        suggestions.append("Resume is a bit long for Entry Level. Try to keep it under 1 page.")
    elif experience_level == "Senior" and word_count < 400:
        resume_score -= 5
        suggestions.append("Senior resumes should usually elaborate more on leadership and impact.")

    resume_score = min(100, int(resume_score))
    
    # --- 5. Prediction ---
    predicted_role = predict_role_from_resume(text)
    if predicted_role != "Unknown" and predicted_role != selected_role:
        suggestions.append(f"AI suggests your resume looks like a **{predicted_role}**.")

    return suggestions, resume_score, keyword_match, predicted_role

# --- MODEL INTEGRATION ---
import pickle
import os
import pandas as pd

# Global cache for model
_MODEL = None
_VECTORIZER = None

def load_model_artifacts():
    global _MODEL, _VECTORIZER
    if _MODEL is None or _VECTORIZER is None:
        try:
            with open("models/resume_classifier.pkl", "rb") as f:
                _MODEL = pickle.load(f)
            with open("models/tfidf_vectorizer.pkl", "rb") as f:
                _VECTORIZER = pickle.load(f)
        except Exception as e:
            print(f"Error loading model: {e}")
            return None, None
    return _MODEL, _VECTORIZER

def predict_role_from_resume(text):
    clf, tfidf = load_model_artifacts()
    if not clf or not tfidf:
        return "Unknown"
    
    # Vectorize text
    text_vector = tfidf.transform([text])
    
    # Predict
    prediction = clf.predict(text_vector)
    return prediction[0]
