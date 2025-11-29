# components/footer.py
import streamlit.components.v1 as components

def render_footer():
    # Inline styles used here to avoid being overridden; also includes solid background & padding.
    footer_html = """
    <div style="width:100%; background:#0b0f14; color:#ffffff; padding:56px 12px 40px 12px; box-shadow:0 18px 40px rgba(2,6,23,0.22);">
      <div style="max-width:1200px; margin:0 auto; display:grid; grid-template-columns: repeat(auto-fit, minmax(200px,1fr)); gap:28px; align-items:start;">
        <div style="min-width:200px;">
          <h4 style="margin:0 0 8px 0; color:#fff;">Smart Resume Analyzer</h4>
          <p style="margin:0 0 8px 0; color:#dfeaf6;">AI-powered resume analysis to identify keyword gaps, score resumes, and align them with job descriptions.</p>
          <p style="margin-top:8px;color:#bfcfe0;">Crafted for job seekers, recruiters &amp; career coaches.</p>
        </div>

        <div style="min-width:180px;">
          <h4 style="margin:0 0 8px 0; color:#fff;">Quick Links</h4>
          <ul style="list-style:none; padding:0; margin:0; color:#dfeaf6;">
            <li style="margin:6px 0;"><a href='#' style='color:inherit; text-decoration:none;'>Home</a></li>
            <li style="margin:6px 0;"><a href='#' style='color:inherit; text-decoration:none;'>Upload Resume</a></li>
            <li style="margin:6px 0;"><a href='#' style='color:inherit; text-decoration:none;'>Features</a></li>
            <li style="margin:6px 0;"><a href='#' style='color:inherit; text-decoration:none;'>How It Works</a></li>
          </ul>
        </div>

        <div style="min-width:180px;">
          <h4 style="margin:0 0 8px 0; color:#fff;">Resources</h4>
          <ul style="list-style:none; padding:0; margin:0; color:#dfeaf6;">
            <li style="margin:6px 0;"><a href='#' style='color:inherit; text-decoration:none;'>Documentation</a></li>
            <li style="margin:6px 0;"><a href='#' style='color:inherit; text-decoration:none;'>Resume Templates</a></li>
            <li style="margin:6px 0;"><a href='#' style='color:inherit; text-decoration:none;'>Blog & Guides</a></li>
            <li style="margin:6px 0;"><a href='#' style='color:inherit; text-decoration:none;'>Support</a></li>
          </ul>
        </div>

        <div style="min-width:220px;">
          <h4 style="margin:0 0 8px 0; color:#fff;">Stay Connected</h4>
          <p style="color:#bfcfe0; margin:0 0 8px 0;">Get feature updates &amp; resume tips.</p>
          <div style="margin:8px 0 14px 0;">
            <input placeholder="Enter your email" style="padding:10px;border-radius:10px;border:1px solid rgba(255,255,255,0.08);width:100%;max-width:260px;background:#071018;color:#fff"/>
          </div>
          <div style="display:flex; gap:12px; flex-wrap:wrap;">
            <a href="#" title="Twitter" style="display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;border-radius:10px;background:rgba(255,255,255,0.03);text-decoration:none;">🐦</a>
            <a href="#" title="LinkedIn" style="display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;border-radius:10px;background:rgba(255,255,255,0.03);text-decoration:none;">🔗</a>
            <a href="#" title="GitHub" style="display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;border-radius:10px;background:rgba(255,255,255,0.03);text-decoration:none;">🐙</a>
            <a href="#" title="Website" style="display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;border-radius:10px;background:rgba(255,255,255,0.03);text-decoration:none;">🌐</a>
          </div>
        </div>
      </div>
    </div>
    """
    # Render the footer; height larger to ensure nothing is cropped.
    components.html(footer_html, height=520, scrolling=False)

# Backwards-compatible alias
try:
    show_footer = render_footer
except Exception:
    def show_footer():
        pass
