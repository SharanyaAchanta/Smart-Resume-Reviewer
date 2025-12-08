# components/footer.py
import streamlit as st
import streamlit.components.v1 as components

def render_footer():
    theme = st.session_state.get('theme', 'Light')
    
    # Theme-aware colors
    if theme == 'Dark':
        bg_color = '#0e1117'
        text_color = '#e8f1f2'
        card_bg = '#1b1f24'
        muted_color = '#a0aec0'
        link_color = '#cbd5e0'
        input_bg = '#1a202c'
        input_border = 'rgba(255,255,255,0.15)'
        social_bg = 'rgba(255,255,255,0.08)'
        shadow = 'rgba(0,0,0,0.4)'
    else:
        bg_color = '#fafbfc'
        text_color = '#1a202c'
        card_bg = '#f7fafc'
        muted_color = '#718096'
        link_color = '#4a5568'
        input_bg = '#ffffff'
        input_border = 'rgba(0,0,0,0.1)'
        social_bg = 'rgba(0,0,0,0.06)'
        shadow = 'rgba(0,0,0,0.08)'
    
    footer_html = f"""
    <head>
      <link rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
        referrerpolicy="no-referrer"
      />
      <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet"/>
      <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
      <script>
        document.addEventListener('DOMContentLoaded', () => {{
          AOS.init({{
            duration: 1000,
            easing: 'ease-in-out',
          }});
        }});
      </script>
    </head>

    <body>
      <div style="width:100%; background:{bg_color}; color:{text_color}; padding:56px 12px 40px 12px; box-shadow:0 18px 40px {shadow};">
        <div data-aos="fade-up" style="max-width:1200px; margin:0 auto; display:grid; grid-template-columns: repeat(auto-fit, minmax(200px,1fr)); gap:28px; align-items:start;">
         <div style="min-width:200px;">
           <h4 style="margin:0 0 8px 0; color:{text_color};">Smart Resume Analyzer</h4>
           <p style="margin:0 0 8px 0; color:{muted_color};">AI-powered resume analysis to identify keyword gaps, score resumes, and align them with job descriptions.</p>
           <p style="margin-top:8px;color:{link_color};">Crafted for job seekers, recruiters & career coaches.</p>
         </div>

         <div style="min-width:180px;">
           <h4 style="margin:0 0 8px 0; color:{text_color}">Quick Links</h4>
           <ul style="list-style:none; padding:0; margin:0; color:{muted_color};">
             <li style="margin:6px 0;"><a href='#' style='color:{link_color}; text-decoration:none;'>Home</a></li>
             <li style="margin:6px 0;"><a href='#' style='color:{link_color}; text-decoration:none;'>Upload Resume</a></li>
             <li style="margin:6px 0;"><a href='#' style='color:{link_color}; text-decoration:none;'>Features</a></li>
             <li style="margin:6px 0;"><a href='#' style='color:{link_color}; text-decoration:none;'>How It Works</a></li>
           </ul>
         </div>

         <div style="min-width:180px;">
           <h4 style="margin:0 0 8px 0; color:{text_color}">Resources</h4>
           <ul style="list-style:none; padding:0; margin:0; color:{muted_color};">
             <li style="margin:6px 0;"><a href='#' style='color:{link_color}; text-decoration:none;'>Documentation</a></li>
             <li style="margin:6px 0;"><a href='#' style='color:{link_color}; text-decoration:none;'>Resume Templates</a></li>
             <li style="margin:6px 0;"><a href='#' style='color:{link_color}; text-decoration:none;'>Blog & Guides</a></li>
             <li style="margin:6px 0;"><a href='#' style='color:{link_color}; text-decoration:none;'>Support</a></li>
           </ul>
         </div>

         <div style="min-width:220px;">
           <h4 style="margin:0 0 8px 0; color:{text_color}">Stay Connected</h4>
           <p style="color:{link_color}; margin:0 0 8px 0;">Get feature updates & resume tips.</p>
           <div style="margin:8px 0 14px 0;">
             <input placeholder="Enter your email" style="padding:10px;border-radius:10px;border:1px solid {input_border};width:100%;max-width:260px;background:{input_bg};color:{text_color}"/>
           </div>
           <div style="display:flex; gap:12px; flex-wrap:wrap;">
             <a href="#" title="Twitter" style="display:inline-flex;align-items:center;justify-content:center;width:50px;height:50px;border-radius:10px;background:{social_bg};text-decoration:none;">
               <i class="fa-brands fa-x-twitter" style="color:{text_color}; font-size:20px;"></i>
             </a>
             <a href="#" title="LinkedIn" style="display:inline-flex;align-items:center;justify-content:center;width:50px;height:50px;border-radius:10px;background:{social_bg};text-decoration:none;">
               <i class="fa-brands fa-linkedin" style="color:{text_color}; font-size:20px;"></i>
             </a>
             <a href="#" title="GitHub" style="display:inline-flex;align-items:center;justify-content:center;width:50px;height:50px;border-radius:10px;background:{social_bg};text-decoration:none;">
               <i class="fa-brands fa-github" style="color:{text_color}; font-size:20px;"></i>
             </a>
             <a href="#" title="Website" style="display:inline-flex;align-items:center;justify-content:center;width:50px;height:50px;border-radius:10px;background:{social_bg};text-decoration:none;">
               <i class="fa-solid fa-globe" style="color:{text_color}; font-size:20px;"></i>
             </a>
           </div>
         </div>
        </div>
      </div>
    </body>
    """
    # Render the footer; height larger to ensure nothing is cropped.
    components.html(footer_html, height=520, scrolling=False)

# Backwards-compatible alias
try:
    show_footer = render_footer
except Exception:
    def show_footer():
        pass
