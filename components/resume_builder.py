import streamlit as st
from utils.pdf_generator import generate_resume_pdf
import os

def show_resume_builder():
    st.markdown("<h1 style='text-align: center; background: linear-gradient(135deg, #EC4899 0%, #DB2777 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800;'>📝 AI Resume Builder</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Fill in your details below and generate a professional PDF resume instantly.</p>", unsafe_allow_html=True)

    with st.form("resume_builder_form"):
        # --- PERSONAL INFO ---
        st.subheader("👤 Personal Information")
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Full Name", placeholder="e.g. John Doe")
            email = st.text_input("Email", placeholder="john@example.com")
            linkedin = st.text_input("LinkedIn URL", placeholder="linkedin.com/in/johndoe")
        with c2:
            phone = st.text_input("Phone Number", placeholder="+1 234 567 890")
            portfolio = st.text_input("Portfolio/Website", placeholder="johndoe.com")
            
        # --- SUMMARY ---
        st.subheader("📝 Professional Summary")
        summary = st.text_area("Write a brief summary of your professional background", height=100)
        
        # --- EXPERIENCE ---
        st.subheader("💼 Work Experience")
        st.info("Add your 2 most recent roles here.")
        
        experiences = []
        for i in range(1, 3):
            with st.expander(f"Experience {i}"):
                c1, c2 = st.columns(2)
                title = c1.text_input(f"Job Title #{i}")
                company = c2.text_input(f"Company #{i}")
                dates = st.text_input(f"Dates (e.g. Jan 2022 - Present) #{i}")
                desc = st.text_area(f"Description #{i}", height=100)
                
                if title and company:
                    experiences.append({
                        "title": title,
                        "company": company,
                        "dates": dates,
                        "description": desc
                    })

        # --- EDUCATION ---
        st.subheader("🎓 Education")
        educations = []
        with st.expander("Add Education"):
            c1, c2 = st.columns(2)
            degree = c1.text_input("Degree (e.g. B.Sc in Computer Science)")
            school = c2.text_input("University/School")
            year = st.text_input("Year of Graduation")
            
            if degree and school:
                educations.append({
                    "degree": degree,
                    "school": school,
                    "year": year
                })

        # --- SKILLS ---
        st.subheader("🛠 Skills")
        skills = st.text_area("List your skills (comma separated)", placeholder="Python, React, Data Analysis, Leadership")

        # --- SUBMIT ---
        submitted = st.form_submit_button("Generate Resume PDF 📄", type="primary")

        if submitted:
            if not name or not email:
                st.error("Please fill in at least Name and Email.")
            else:
                data = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "linkedin": linkedin,
                    "portfolio": portfolio,
                    "summary": summary,
                    "experience": experiences,
                    "education": educations,
                    "skills": skills
                }
                
                try:
                    pdf_path = generate_resume_pdf(data)
                    with open(pdf_path, "rb") as f:
                        pdf_bytes = f.read()
                    
                    # Store PDF data in session state (outside form)
                    st.session_state.resume_pdf_bytes = pdf_bytes
                    st.session_state.resume_pdf_filename = f"Resume_{name.replace(' ', '_')}.pdf"
                    st.session_state.resume_generated = True
                    st.rerun()
                except Exception as e:
                    st.error(f"An error occurred during PDF generation: {e}")
    
    # Download button outside the form
    if st.session_state.get("resume_generated", False):
        st.markdown("---")
        st.success("✅ Resume Generated Successfully!")
        st.download_button(
            label="📥 Download Resume PDF",
            data=st.session_state.get("resume_pdf_bytes"),
            file_name=st.session_state.get("resume_pdf_filename", "Resume.pdf"),
            mime="application/pdf",
            width="stretch",
            type="primary"
        )
        if st.button("Generate New Resume", width="stretch"):
            st.session_state.resume_generated = False
            st.session_state.resume_pdf_bytes = None
            st.session_state.resume_pdf_filename = None
            st.rerun()
