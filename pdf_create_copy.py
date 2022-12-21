from PyPDF2 import PdfFileWriter as w
from pathlib import Path
import PyPDF2

# Create
pdf = w()
file = open(Path.home() / Path('Desktop', 'pdf_file.pdf'), 'wb')
# create pages
for i in range(5):
    pdf.addBlankPage(219, 297)  # A4 size dimensions
pdf.write(file)

# Copy Phase
# read pdf file
pdf_file = open(Path.home() / Path('Desktop', 'book.pdf'), 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

for page_num in range(pdf_reader.numPages):
    page_copy_obj = pdf_reader.getPage(page_num)
    pdf.addPage(page_copy_obj)

pdf.write(file)

file.close()
