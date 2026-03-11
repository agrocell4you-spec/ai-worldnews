from fpdf import FPDF

def make_pdf(posts):

    pdf=FPDF()
    pdf.set_auto_page_break(auto=True,margin=15)

    for title,content in posts:

        pdf.add_page()
        pdf.set_font("Arial",size=12)

        pdf.cell(0,10,title,ln=True)

        pdf.multi_cell(0,8,content)

    pdf.output("daily_posts.pdf")