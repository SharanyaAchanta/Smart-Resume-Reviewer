import streamlit as st

def show_service_page():
    """Aesthetic Services page with modern design."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');
        </style>
        <div style="text-align: center; padding: 0 20px 80px;">
            <h1 style="
                font-size: 3.5rem; 
                font-weight: 800; 
                margin-bottom: 20px; 
                background: linear-gradient(135deg, #EC4899 0%, #DB2777 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: 'Outfit', sans-serif;
            ">Our Services</h1>
            <p style="
                font-size: 1.3rem; 
                color: #64748B; 
                max-width: 700px; 
                margin: 0 auto 60px;
                font-family: 'Outfit', sans-serif;
                line-height: 1.6;
            ">Powering your career journey with next-gen AI tools and intelligent insights.</p>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px; max-width: 1200px; margin: 0 auto;">
                
                <div style="
                    background: rgba(255, 255, 255, 0.7);
                    backdrop-filter: blur(12px);
                    border: 1px solid rgba(255, 255, 255, 0.6);
                    border-radius: 24px;
                    padding: 40px;
                    box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.05);
                    transition: all 0.3s ease;
                    text-align: left;
                " onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 25px 50px -12px rgba(236, 72, 153, 0.15)'" 
                   onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 20px 40px -10px rgba(0, 0, 0, 0.05)'">
                    <div style="
                        background: linear-gradient(135deg, #FCE7F3 0%, #FDF2F8 100%); 
                        width: 70px; 
                        height: 70px; 
                        border-radius: 16px; 
                        display: flex; 
                        align-items: center; 
                        justify-content: center; 
                        font-size: 36px; 
                        margin-bottom: 24px;
                        box-shadow: 0 8px 16px rgba(236, 72, 153, 0.15);
                    ">🚀</div>
                    <h3 style="margin: 0 0 12px; color: #1E293B; font-size: 1.5rem; font-weight: 700; font-family: 'Outfit', sans-serif;">Resume Analyzer</h3>
                    <p style="color: #64748B; font-size: 1rem; line-height: 1.7; font-family: 'Outfit', sans-serif; margin: 0;">Instant, detailed feedback on your resume's impact, ATS compatibility, and structure using advanced NLP and machine learning algorithms.</p>
                </div>

                <div style="
                    background: rgba(255, 255, 255, 0.7);
                    backdrop-filter: blur(12px);
                    border: 1px solid rgba(255, 255, 255, 0.6);
                    border-radius: 24px;
                    padding: 40px;
                    box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.05);
                    transition: all 0.3s ease;
                    text-align: left;
                " onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 25px 50px -12px rgba(244, 114, 182, 0.15)'" 
                   onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 20px 40px -10px rgba(0, 0, 0, 0.05)'">
                    <div style="
                        background: linear-gradient(135deg, #FDF2F8 0%, #FCE7F3 100%); 
                        width: 70px; 
                        height: 70px; 
                        border-radius: 16px; 
                        display: flex; 
                        align-items: center; 
                        justify-content: center; 
                        font-size: 36px; 
                        margin-bottom: 24px;
                        box-shadow: 0 8px 16px rgba(244, 114, 182, 0.15);
                    ">📝</div>
                    <h3 style="margin: 0 0 12px; color: #1E293B; font-size: 1.5rem; font-weight: 700; font-family: 'Outfit', sans-serif;">Resume Builder</h3>
                    <p style="color: #64748B; font-size: 1rem; line-height: 1.7; font-family: 'Outfit', sans-serif; margin: 0;">Create a professional, ATS-optimized resume in minutes with our smart, auto-formatting templates and intelligent content suggestions.</p>
                </div>

                <div style="
                    background: rgba(255, 255, 255, 0.7);
                    backdrop-filter: blur(12px);
                    border: 1px solid rgba(255, 255, 255, 0.6);
                    border-radius: 24px;
                    padding: 40px;
                    box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.05);
                    transition: all 0.3s ease;
                    text-align: left;
                " onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 25px 50px -12px rgba(245, 158, 11, 0.15)'" 
                   onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 20px 40px -10px rgba(0, 0, 0, 0.05)'">
                    <div style="
                        background: linear-gradient(135deg, #FEF3C7 0%, #FFFBEB 100%); 
                        width: 70px; 
                        height: 70px; 
                        border-radius: 16px; 
                        display: flex; 
                        align-items: center; 
                        justify-content: center; 
                        font-size: 36px; 
                        margin-bottom: 24px;
                        box-shadow: 0 8px 16px rgba(245, 158, 11, 0.15);
                    ">🎯</div>
                    <h3 style="margin: 0 0 12px; color: #1E293B; font-size: 1.5rem; font-weight: 700; font-family: 'Outfit', sans-serif;">Job Match</h3>
                    <p style="color: #64748B; font-size: 1rem; line-height: 1.7; font-family: 'Outfit', sans-serif; margin: 0;">Find the perfect roles that align with your unique skill set and experience level using our intelligent matching algorithm.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def show_blogs_page():
    """Aesthetic Blogs page with modern design."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');
        </style>
        <div style="padding: 0 20px 80px; max-width: 1000px; margin: 0 auto;">
            <h1 style="
                text-align: center; 
                font-size: 3.5rem; 
                font-weight: 800; 
                margin-bottom: 20px;
                background: linear-gradient(135deg, #EC4899 0%, #DB2777 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: 'Outfit', sans-serif;
            ">Career Insights & Blog</h1>
            <p style="
                text-align: center;
                color: #64748B; 
                font-size: 1.2rem; 
                margin-bottom: 60px;
                font-family: 'Outfit', sans-serif;
            ">Expert advice, industry trends, and career tips to help you succeed.</p>
            
            <div style="display: grid; gap: 30px;">
                <!-- Blog Post 1 -->
                <div style="
                    background: rgba(255, 255, 255, 0.7);
                    backdrop-filter: blur(12px);
                    border: 1px solid rgba(255, 255, 255, 0.6);
                    border-radius: 24px;
                    padding: 35px;
                    box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.05);
                    display: flex;
                    gap: 30px;
                    align-items: start;
                    transition: all 0.3s ease;
                " onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 25px 50px -12px rgba(236, 72, 153, 0.15)'" 
                   onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 20px 40px -10px rgba(0, 0, 0, 0.05)'">
                    <div style="
                        background: linear-gradient(135deg, #FCE7F3 0%, #FDF2F8 100%); 
                        width: 140px; 
                        height: 120px; 
                        border-radius: 16px; 
                        flex-shrink: 0; 
                        display: flex; 
                        align-items: center; 
                        justify-content: center; 
                        font-size: 50px;
                        box-shadow: 0 8px 16px rgba(236, 72, 153, 0.15);
                    ">🚀</div>
                    <div style="flex: 1;">
                        <div style="
                            color: #EC4899; 
                            font-weight: 700; 
                            font-size: 0.85rem; 
                            text-transform: uppercase; 
                            letter-spacing: 1px;
                            margin-bottom: 8px;
                            font-family: 'Outfit', sans-serif;
                        ">Resume Tips</div>
                        <h3 style="
                            margin: 0 0 12px; 
                            color: #1E293B; 
                            font-size: 1.6rem;
                            font-weight: 700;
                            font-family: 'Outfit', sans-serif;
                        ">5 Tips to Beat the ATS in 2025</h3>
                        <p style="
                            color: #64748B; 
                            margin-bottom: 18px; 
                            line-height: 1.7;
                            font-size: 1rem;
                            font-family: 'Outfit', sans-serif;
                        ">Learn how Application Tracking Systems filter resumes and what you can do to ensure yours gets seen by a human recruiter. Master the art of keyword optimization and formatting.</p>
                        <a href="#" style="
                            color: #EC4899; 
                            font-weight: 700; 
                            text-decoration: none; 
                            border-bottom: 2px solid #FBCFE8;
                            font-family: 'Outfit', sans-serif;
                            transition: all 0.2s;
                        " onmouseover="this.style.color='#DB2777'" onmouseout="this.style.color='#EC4899'">Read Article →</a>
                    </div>
                </div>
                
                <!-- Blog Post 2 -->
                <div style="
                    background: rgba(255, 255, 255, 0.7);
                    backdrop-filter: blur(12px);
                    border: 1px solid rgba(255, 255, 255, 0.6);
                    border-radius: 24px;
                    padding: 35px;
                    box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.05);
                    display: flex;
                    gap: 30px;
                    align-items: start;
                    transition: all 0.3s ease;
                " onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 25px 50px -12px rgba(220, 38, 38, 0.15)'" 
                   onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 20px 40px -10px rgba(0, 0, 0, 0.05)'">
                    <div style="
                        background: linear-gradient(135deg, #FEE2E2 0%, #FECACA 100%); 
                        width: 140px; 
                        height: 120px; 
                        border-radius: 16px; 
                        flex-shrink: 0; 
                        display: flex; 
                        align-items: center; 
                        justify-content: center; 
                        font-size: 50px;
                        box-shadow: 0 8px 16px rgba(220, 38, 38, 0.15);
                    ">💡</div>
                    <div style="flex: 1;">
                        <div style="
                            color: #DC2626; 
                            font-weight: 700; 
                            font-size: 0.85rem; 
                            text-transform: uppercase; 
                            letter-spacing: 1px;
                            margin-bottom: 8px;
                            font-family: 'Outfit', sans-serif;
                        ">Interview Skills</div>
                        <h3 style="
                            margin: 0 0 12px; 
                            color: #1E293B; 
                            font-size: 1.6rem;
                            font-weight: 700;
                            font-family: 'Outfit', sans-serif;
                        ">Top Soft Skills Employers Look For</h3>
                        <p style="
                            color: #64748B; 
                            margin-bottom: 18px; 
                            line-height: 1.7;
                            font-size: 1rem;
                            font-family: 'Outfit', sans-serif;
                        ">Beyond technical expertise, discover the key interpersonal skills that can set you apart in interviews and workplace dynamics. Learn how to showcase your emotional intelligence.</p>
                        <a href="#" style="
                            color: #DC2626; 
                            font-weight: 700; 
                            text-decoration: none; 
                            border-bottom: 2px solid #FECACA;
                            font-family: 'Outfit', sans-serif;
                            transition: all 0.2s;
                        " onmouseover="this.style.color='#991B1B'" onmouseout="this.style.color='#DC2626'">Read Article →</a>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def show_about_page():
    """Aesthetic About page with modern design."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');
        </style>
        <div style="text-align: center; padding: 0 20px 80px;">
            <h1 style="
                color: #1E293B; 
                margin-bottom: 20px; 
                font-size: 3.5rem;
                font-weight: 800;
                font-family: 'Outfit', sans-serif;
            ">About <span style="
                background: linear-gradient(135deg, #EC4899 0%, #DB2777 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            ">Resulyze</span></h1>
            <p style="
                font-size: 1.25rem; 
                color: #64748B; 
                max-width: 700px; 
                margin: 0 auto 60px; 
                line-height: 1.8;
                font-family: 'Outfit', sans-serif;
            ">We are a team of data scientists and HR professionals dedicated to democratizing career success. Our mission is to provide every job seeker with the same level of resume feedback that expensive career coaches charge hundreds of dollars for.</p>
            
            <div style="display: flex; justify-content: center; gap: 30px; flex-wrap: wrap; max-width: 1000px; margin: 0 auto;">
                <div style="
                    background: rgba(255, 255, 255, 0.7);
                    backdrop-filter: blur(12px);
                    border: 1px solid rgba(255, 255, 255, 0.6);
                    border-radius: 24px;
                    padding: 40px;
                    box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.05);
                    text-align: left;
                    width: 100%;
                    max-width: 450px;
                    transition: all 0.3s ease;
                " onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 25px 50px -12px rgba(236, 72, 153, 0.15)'" 
                   onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 20px 40px -10px rgba(0, 0, 0, 0.05)'">
                    <h4 style="
                        margin-bottom: 12px; 
                        color: #EC4899; 
                        font-size: 1.4rem;
                        font-weight: 700;
                        font-family: 'Outfit', sans-serif;
                    ">Our Vision</h4>
                    <p style="
                        color: #64748B; 
                        line-height: 1.7;
                        font-size: 1rem;
                        font-family: 'Outfit', sans-serif;
                        margin: 0;
                    ">A world where talent, not keyword stuffing, determines hiring success. We believe everyone deserves access to professional career guidance.</p>
                </div>
                
                <div style="
                    background: rgba(255, 255, 255, 0.7);
                    backdrop-filter: blur(12px);
                    border: 1px solid rgba(255, 255, 255, 0.6);
                    border-radius: 24px;
                    padding: 40px;
                    box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.05);
                    text-align: left;
                    width: 100%;
                    max-width: 450px;
                    transition: all 0.3s ease;
                " onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 25px 50px -12px rgba(16, 185, 129, 0.15)'" 
                   onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 20px 40px -10px rgba(0, 0, 0, 0.05)'">
                    <h4 style="
                        margin-bottom: 12px; 
                        color: #10B981; 
                        font-size: 1.4rem;
                        font-weight: 700;
                        font-family: 'Outfit', sans-serif;
                    ">Our Technology</h4>
                    <p style="
                        color: #64748B; 
                        line-height: 1.7;
                        font-size: 1rem;
                        font-family: 'Outfit', sans-serif;
                        margin: 0;
                    ">Powered by advanced NLP and machine learning models trained on thousands of successful resumes. We continuously improve our algorithms to provide the most accurate insights.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def show_pricing_page():
    """Aesthetic Pricing page with modern design."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');
        </style>
        <div style="text-align: center; padding: 0 20px 80px;">
            <h1 style="
                color: #1E293B; 
                margin-bottom: 12px; 
                font-size: 3.5rem;
                font-weight: 800;
                font-family: 'Outfit', sans-serif;
            ">Simple, Transparent Pricing</h1>
            <p style="
                color: #64748B; 
                margin-bottom: 60px;
                font-size: 1.2rem;
                font-family: 'Outfit', sans-serif;
            ">Start for free, upgrade for more power.</p>
            
            <div style="display: flex; justify-content: center; gap: 30px; flex-wrap: wrap; align-items: stretch; max-width: 1100px; margin: 0 auto;">
                <!-- Free Plan -->
                <div style="
                    background: rgba(255, 255, 255, 0.7);
                    backdrop-filter: blur(12px);
                    border: 1px solid rgba(255, 255, 255, 0.6);
                    border-radius: 24px;
                    padding: 45px 35px;
                    width: 100%;
                    max-width: 340px;
                    text-align: left;
                    display: flex;
                    flex-direction: column;
                    box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.05);
                    transition: all 0.3s ease;
                " onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 25px 50px -12px rgba(0, 0, 0, 0.1)'" 
                   onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 20px 40px -10px rgba(0, 0, 0, 0.05)'">
                    <h3 style="
                        font-size: 1.6rem; 
                        margin-bottom: 12px; 
                        color: #1E293B;
                        font-weight: 700;
                        font-family: 'Outfit', sans-serif;
                    ">Free</h3>
                    <div style="
                        font-size: 3rem; 
                        font-weight: 800; 
                        color: #1E293B; 
                        margin-bottom: 30px;
                        font-family: 'Outfit', sans-serif;
                    ">$0 <span style="font-size: 1rem; color: #94A3B8; font-weight: 400;">/mo</span></div>
                    <ul style="
                        list-style: none; 
                        padding: 0; 
                        margin-bottom: auto; 
                        color: #64748B; 
                        line-height: 2.2;
                        font-family: 'Outfit', sans-serif;
                        font-size: 1rem;
                    ">
                        <li>✅ 5 Resume Scans / month</li>
                        <li>✅ Basic Score Breakdown</li>
                        <li>✅ 1 Job Description Match</li>
                    </ul>
                    <button style="
                        width: 100%; 
                        background: #F1F5F9; 
                        color: #1E293B; 
                        border: none; 
                        padding: 16px; 
                        border-radius: 12px; 
                        font-weight: 700; 
                        cursor: pointer; 
                        margin-top: 35px;
                        font-family: 'Outfit', sans-serif;
                        font-size: 1rem;
                        transition: all 0.2s;
                    " onmouseover="this.style.background='#E2E8F0'" onmouseout="this.style.background='#F1F5F9'">Current Plan</button>
                </div>
                
                <!-- Pro Plan -->
                <div style="
                    background: linear-gradient(135deg, #EC4899 0%, #DB2777 100%); 
                    border-radius: 28px; 
                    padding: 50px 40px; 
                    width: 100%;
                    max-width: 340px;
                    text-align: left; 
                    color: white; 
                    position: relative; 
                    box-shadow: 0 25px 50px -12px rgba(236, 72, 153, 0.4); 
                    transform: scale(1.05);
                    display: flex;
                    flex-direction: column;
                ">
                    <div style="
                        position: absolute; 
                        top: -15px; 
                        right: 25px; 
                        background: linear-gradient(90deg, #F59E0B, #D97706); 
                        color: white; 
                        font-size: 12px; 
                        font-weight: 800; 
                        padding: 8px 18px; 
                        border-radius: 25px; 
                        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.4);
                        font-family: 'Outfit', sans-serif;
                        letter-spacing: 0.5px;
                    ">POPULAR</div>
                    <h3 style="
                        font-size: 1.6rem; 
                        margin-bottom: 12px; 
                        color: white;
                        font-weight: 700;
                        font-family: 'Outfit', sans-serif;
                    ">Pro</h3>
                    <div style="
                        font-size: 3rem; 
                        font-weight: 800; 
                        margin-bottom: 30px;
                        font-family: 'Outfit', sans-serif;
                    ">$19 <span style="font-size: 1rem; opacity: 0.85; font-weight: 400;">/mo</span></div>
                    <ul style="
                        list-style: none; 
                        padding: 0; 
                        margin-bottom: 30px; 
                        line-height: 2.2;
                        color: #FDF2F8;
                        font-family: 'Outfit', sans-serif;
                        font-size: 1rem;
                    ">
                        <li style="color: white; font-weight: 500;">✅ Unlimited Scans</li>
                        <li style="color: white; font-weight: 500;">✅ Detailed Action Plan</li>
                        <li style="color: white; font-weight: 500;">✅ Keyword Optimization</li>
                        <li style="color: white; font-weight: 500;">✅ LinkedIn Profile Review</li>
                    </ul>
                    <button style="
                        width: 100%; 
                        background: white; 
                        color: #EC4899; 
                        border: none; 
                        padding: 16px; 
                        border-radius: 12px; 
                        font-weight: 800; 
                        cursor: pointer; 
                        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
                        font-family: 'Outfit', sans-serif;
                        font-size: 1rem;
                        transition: all 0.2s;
                    " onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 12px 24px rgba(0, 0, 0, 0.2)'" 
                       onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 20px rgba(0, 0, 0, 0.15)'">Get Started</button>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def show_faq_page():
    """Aesthetic FAQ page with modern design."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');
        </style>
        <div style="max-width: 900px; margin: 0 auto; padding: 0 20px 80px;">
            <h1 style="
                text-align: center; 
                margin-bottom: 50px; 
                font-size: 3.5rem;
                font-weight: 800;
                background: linear-gradient(135deg, #EC4899 0%, #DB2777 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: 'Outfit', sans-serif;
            ">Frequently Asked Questions</h1>
            
            <div style="
                background: rgba(255, 255, 255, 0.7);
                backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.6);
                border-radius: 24px;
                padding: 0;
                overflow: hidden;
                box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.05);
            ">
                <details style="
                    padding: 30px; 
                    border-bottom: 1px solid #F1F5F9; 
                    cursor: pointer; 
                    transition: background 0.2s;
                " onmouseover="this.style.background='rgba(236, 72, 153, 0.03)'" onmouseout="this.style.background='transparent'">
                    <summary style="
                        font-weight: 700; 
                        color: #1E293B; 
                        font-size: 1.2rem; 
                        list-style: none;
                        font-family: 'Outfit', sans-serif;
                        display: flex;
                        align-items: center;
                        gap: 12px;
                    ">🔹 <span>How is the resume score calculated?</span></summary>
                    <p style="
                        margin-top: 18px; 
                        color: #64748B; 
                        line-height: 1.8; 
                        padding-left: 32px;
                        font-family: 'Outfit', sans-serif;
                        font-size: 1rem;
                    ">Our algorithm analyzes your resume against thousands of job descriptions and industry standards, checking for formatting compliance (ATS), keyword relevance, and quantifiable impact metrics. The score is weighted across multiple dimensions including structure, content quality, and role-specific keyword matching.</p>
                </details>
                
                <details style="
                    padding: 30px; 
                    border-bottom: 1px solid #F1F5F9; 
                    cursor: pointer; 
                    transition: background 0.2s;
                " onmouseover="this.style.background='rgba(236, 72, 153, 0.03)'" onmouseout="this.style.background='transparent'">
                    <summary style="
                        font-weight: 700; 
                        color: #1E293B; 
                        font-size: 1.2rem; 
                        list-style: none;
                        font-family: 'Outfit', sans-serif;
                        display: flex;
                        align-items: center;
                        gap: 12px;
                    ">🔹 <span>Is my data secure?</span></summary>
                    <p style="
                        margin-top: 18px; 
                        color: #64748B; 
                        line-height: 1.8; 
                        padding-left: 32px;
                        font-family: 'Outfit', sans-serif;
                        font-size: 1rem;
                    ">Yes! We use <strong style="color: #EC4899;">bank-level encryption</strong> and do not share your personal data with third parties. Your resume is processed in-memory and deleted immediately after analysis. We are GDPR compliant and take your privacy seriously.</p>
                </details>
                
                <details style="
                    padding: 30px; 
                    cursor: pointer; 
                    transition: background 0.2s;
                " onmouseover="this.style.background='rgba(236, 72, 153, 0.03)'" onmouseout="this.style.background='transparent'">
                    <summary style="
                        font-weight: 700; 
                        color: #1E293B; 
                        font-size: 1.2rem; 
                        list-style: none;
                        font-family: 'Outfit', sans-serif;
                        display: flex;
                        align-items: center;
                        gap: 12px;
                    ">🔹 <span>Can I use this for any industry?</span></summary>
                    <p style="
                        margin-top: 18px; 
                        color: #64748B; 
                        line-height: 1.8; 
                        padding-left: 32px;
                        font-family: 'Outfit', sans-serif;
                        font-size: 1rem;
                    ">Absolutely. While our system is optimized for corporate roles (Tech, Finance, Marketing, Sales), the core principles of clear structure, strong verbs, and keyword optimization apply to all fields. We support over 50+ job categories and continuously expand our database.</p>
                </details>
            </div>
        </div>
    """, unsafe_allow_html=True)
