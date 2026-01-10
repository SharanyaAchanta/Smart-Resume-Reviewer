from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Title
        # self.cell(0, 10, 'Resume', 0, 1, 'C')
        # Line break
        # self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

def generate_resume_pdf(data):
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # --- NAME & CONTACT ---
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(0, 10, data.get('name', 'Your Name'), 0, 1, 'L')
    
    pdf.set_font('Arial', '', 10)
    contact_info = f"{data.get('email', '')} | {data.get('phone', '')}"
    if data.get('linkedin'):
        contact_info += f" | {data.get('linkedin')}"
    if data.get('portfolio'):
        contact_info += f" | {data.get('portfolio')}"
        
    pdf.cell(0, 8, contact_info, 0, 1, 'L')
    pdf.ln(5)
    
    # --- LINE SEPARATOR ---
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)

    # --- SUMMARY ---
    if data.get('summary'):
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, 'Professional Summary', 0, 1, 'L')
        pdf.set_font('Arial', '', 11)
        pdf.multi_cell(0, 6, data.get('summary', ''))
        pdf.ln(5)

    # --- EXPERIENCE ---
    if data.get('experience'):
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, 'Experience', 0, 1, 'L')
        
        for exp in data.get('experience', []):
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(100, 7, exp.get('title', ''), 0, 0)
            
            pdf.set_font('Arial', 'I', 11)
            pdf.cell(0, 7, f"{exp.get('company', '')}  ({exp.get('dates', '')})", 0, 1, 'R')
            
            pdf.set_font('Arial', '', 11)
            pdf.multi_cell(0, 6, exp.get('description', ''))
            pdf.ln(3)
        pdf.ln(2)

    # --- EDUCATION ---
    if data.get('education'):
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, 'Education', 0, 1, 'L')
        
        for edu in data.get('education', []):
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(0, 7, edu.get('degree', ''), 0, 1)
            
            pdf.set_font('Arial', '', 11)
            pdf.cell(0, 6, f"{edu.get('school', '')}, {edu.get('year', '')}", 0, 1)
            pdf.ln(3)
        pdf.ln(2)

    # --- SKILLS ---
    if data.get('skills'):
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, 'Skills', 0, 1, 'L')
        pdf.set_font('Arial', '', 11)
        pdf.multi_cell(0, 6, data.get('skills', ''))
        pdf.ln(5)
        
    # --- OUTPUT ---
    # Ensure generated directory exists
    os.makedirs("generated", exist_ok=True)
    filename = f"generated/Resume_{data.get('name', 'User').replace(' ', '_')}.pdf"
    pdf.output(filename)
    return filename
