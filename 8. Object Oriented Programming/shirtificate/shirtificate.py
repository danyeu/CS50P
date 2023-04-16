from fpdf import FPDF, XPos, YPos


name = input("Name: ").strip()
string = name + " took CS50"

pdf = FPDF(orientation="portrait", format="A4")
pdf.set_margin(0)
pdf.add_page()

pdf.set_font("helvetica", "B", 36)
pdf.cell(0, 45, "CS50 Shirtificate", align = 'C', new_x=XPos("LMARGIN"), new_y=YPos("NEXT"))

pdf.cell(0, 50, new_x=XPos("LMARGIN"), new_y=YPos("NEXT"))

pdf.image(name="shirtificate.png", x=((210 - 150) / 2), y=50, w=150)

pdf.set_font("helvetica", "", 18)
pdf.set_text_color(255, 255, 255)
pdf.cell(60, None, new_x=XPos("RIGHT"), new_y=YPos("TOP"))
pdf.multi_cell(90, None, string, align = 'C')

pdf.output("shirtificate.pdf")