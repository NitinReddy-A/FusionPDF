from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.add_font('NotoSansKannada', '', 'NotoSansKannada-VariableFont_wdth,wght.ttf', uni=True) 
pdf.set_font('NotoSansKannada', '', 14)
pdf.write(8, u'Kannada: ಹಿಂದಿನ ಬಗ್ಗೆ ನಾವು ಏನು ತಿಳಿಯಬಹುದು?')
pdf.ln(20)
pdf.output('oopsie.pdf')