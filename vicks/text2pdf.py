# pip install fpdf

def convert(pdf_path = 'myfile.txt'):
    from fpdf import FPDF
    # save FPDF() class into
    # a variable pdf
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)

    # open the text file in read mode
    f = open(pdf_path, "r")

    # insert the texts in pdf
    for x in f:
        pdf.cell(200, 10, txt = x, ln = 1)

    # save the pdf with name .pdf
    pdf.output(f'{pdf_path.split(".")[0]}.pdf')

    # uncomment to ...password protect
    # from vicks import encrypt as enc
    # enc.encryptpdf("/myfile.pdf")

# convert('comments.json')

# from PyPDF2 import PdfMerger, PdfReader
# merger = PdfMerger()

# merger.append(PdfReader(open(pdfname1 + ".pdf", 'rb')))
# merger.append(PdfReader(open(pdfname2 + ".pdf", 'rb')))
# merger.write("merged.pdf")
