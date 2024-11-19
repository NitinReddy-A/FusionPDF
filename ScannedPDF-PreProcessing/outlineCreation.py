from fpdf import FPDF

class PDFWithImages(FPDF):
    def header(self):
        self.image("Header.jpg", x=10, y=10, w=self.w - 20)

    def footer(self):
        self.set_y(-30)
        self.image("Footer.jpg", x=10, w=self.w - 20)

pdf = PDFWithImages()
pdf.add_page()
pdf.output("FinalOutput.pdf")
