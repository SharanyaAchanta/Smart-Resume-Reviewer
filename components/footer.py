import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64

def show_footer():

    footer_html = """
    <style>

    /* MAIN FIX: footer container becomes fixed, full width, and readable */
    .footer-container {
        position: fixed !important;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 330px;
        overflow: hidden;
        z-index: 9999999;
        padding-left: 20px;
        padding-right: 20px;
        box-sizing: border-box;
    }

    /* Add extra space so content is not hidden behind footer */
    .block-container {
        padding-bottom: 360px !important;
    }

    .footer-wrapper {
        width: 100%;
        margin-top: 0px; /* removed top margin to reduce extra space */
    }

    .footer-container {
        background: #0E1117;
        color: #ffffff;
        padding-top: 25px;
        padding-bottom: 25px;
        border-top: 1px solid rgba(255,255,255,0.08);
        font-family: 'Segoe UI', sans-serif;
        box-sizing: border-box;
    }

    /* Footer grid takes full width without extra gaps */
    .footer-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 20px;
        max-width: 100%; /* full width */
        margin: 0 auto;
        padding: 0 10px; /* small padding for inner spacing */
    }

    .footer-section h4 {
        font-size: 16px; /* slightly larger and readable */
        color: #ffffff;
        margin-bottom: 10px;
        font-weight: 600;
    }

    .footer-section p,
    .footer-section a,
    .footer-section li,
    .footer-section span {
        font-size: 14px; /* slightly larger */
        color: #d8d8d8;
        text-decoration: none;
        line-height: 1.5;
    }

    .footer-section a:hover {
        color: #ffffff;
        text-decoration: underline;
    }

    .footer-list { list-style: none; padding: 0; margin: 0; }
    .footer-list li { margin-bottom: 5px; }

    .newsletter-text { margin-bottom: 6px; }

    .newsletter-input {
        margin-top: 6px;
        display: flex;
        gap: 6px;
        flex-wrap: wrap;
    }

    .newsletter-input input[type="email"] {
        flex: 1 1 150px;
        padding: 8px 10px;
        border-radius: 4px;
        border: 1px solid rgba(255,255,255,0.2);
        background: #050814;
        color: #ffffff;
        font-size: 14px;
    }

    .newsletter-input button {
        padding: 8px 14px;
        border-radius: 4px;
        border: none;
        background: #ffffff;
        color: #0E1117;
        font-size: 14px;
        cursor: pointer;
        font-weight: 600;
    }

    .newsletter-input button:hover { filter: brightness(0.9); }

    .social-icons a {
        margin-right: 12px;
        font-size: 20px;
        color: #d8d8d8;
        transition: 0.3s;
    }

    .social-icons a:hover { color: #ffffff; }

    .contact-item {
        display: flex;
        align-items: flex-start;
        gap: 6px;
        margin-bottom: 6px;
        font-size: 14px;
    }

    .contact-icon { font-size: 16px; }

    .footer-bottom {
        margin-top: 20px;
        text-align: center;
        font-size: 13px;
        color: #b6b6b6;
        padding-top: 10px;
        border-top: 1px solid rgba(255,255,255,0.05);
    }

    .footer-bottom span {
        display: block;
        margin-top: 4px;
        font-size: 12px;
        color: #8c8c8c;
    }

    @media (max-width: 600px) {
        .footer-container {
            padding: 20px 10px 15px;
            height: 380px;
        }
        .block-container { padding-bottom: 400px !important; }
        .footer-section h4 { font-size: 15px; }
        .footer-section p, .footer-section a, .footer-section li, .footer-section span {
            font-size: 13px;
        }
    }
    </style>

    <div class="footer-wrapper">
        <div class="footer-container">

            <div class="footer-grid">

                <div class="footer-section">
                    <h4>Smart Resume Analyzer</h4>
                    <p>
                        AI-powered resume analysis to identify keyword gaps,
                        score resumes, and align them with job descriptions.
                    </p>
                    <p style="margin-top: 8px; font-size: 13px; color: #bfbfbf;">
                        Crafted for job seekers, recruiters & career coaches.
                    </p>
                </div>

                <div class="footer-section">
                    <h4>Quick Links</h4>
                    <ul class="footer-list">
                        <li><a href="#home">Home</a></li>
                        <li><a href="#analyzer">Upload Resume</a></li>
                        <li><a href="#features">Features</a></li>
                        <li><a href="#hiw">How It Works</a></li>
                        <li><a href="#about">About</a></li>
                        <li><a href="#faq">FAQ</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h4>Resources</h4>
                    <ul class="footer-list">
                        <li><a href="#docs">Documentation</a></li>
                        <li><a href="#templates">Resume Templates</a></li>
                        <li><a href="#blog">Blog & Guides</a></li>
                        <li><a href="#support">Support</a></li>
                    </ul>

                    <h4 style="margin-top: 14px;">Legal</h4>
                    <ul class="footer-list">
                        <li><a href="#privacy">Privacy Policy</a></li>
                        <li><a href="#terms">Terms of Use</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h4>Stay Connected</h4>
                    <p class="newsletter-text">
                        Get feature updates & resume tips.
                    </p>

                    <div class="newsletter-input">
                        <input type="email" placeholder="Enter your email"/>
                        <button type="button">Notify me</button>
                    </div>

                    <div style="margin-top: 14px;">
                        <div class="contact-item">
                            <span class="contact-icon">📍</span>
                            <span>Smart Resume Team</span>
                        </div>
                        <div class="contact-item">
                            <span class="contact-icon">📧</span>
                            <span>support@smartresume-analyzer.app</span>
                        </div>
                    </div>

                    <div style="margin-top: 10px;">
                        <h4 style="margin-bottom: 8px;">Follow Us</h4>
                        <div class="social-icons">
                            <a href="https://github.com/SharanyaAchanta" target="_blank" title="GitHub">🐙</a>
                            <a href="#" target="_blank" title="LinkedIn">💼</a>
                            <a href="#" target="_blank" title="Website">🌐</a>
                            <a href="mailto:support@smartresume-analyzer.app" target="_blank" title="Email">📧</a>
                        </div>
                    </div>
                </div>

            </div>

            <div class="footer-bottom">
                © 2025 Smart Resume Analyzer • Built with ❤️ by Team
                <span>Made with Streamlit • Minimal White Theme</span>
            </div>

        </div>
    </div>
    """

    components.html(footer_html, height=380, scrolling=False)
