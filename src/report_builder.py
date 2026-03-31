from fpdf import FPDF

def create_pdf(ddr_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in ddr_text.split("\n"):
        pdf.multi_cell(0, 8, line)

    pdf.output("outputs/ddr_report.pdf")