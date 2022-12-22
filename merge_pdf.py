import PyPDF2, os
from pathlib import Path

pdf_files = []
for file_name in os.listdir(Path('D:\_Python_Projects\Python-Pdf\pdf')):
    if file_name.endswith('.pdf'):
        pdf_files.append(file_name)

pdf_files.sort(key=str.lower)

pdf_writer = PyPDF2.PdfFileWriter()

for file_name in pdf_files:
    pdf_file_object = open(Path('D:\_Python_Projects\Python-Pdf\pdf', file_name), 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_object)

    # start for page number 2 index 1
    for page_number in range(1, pdf_reader.numPages):
        pdf_object = pdf_reader.getPage(page_number)
        pdf_writer.addPage(pdf_object)

pdf_output = open(Path('D:\_Python_Projects\Python-Pdf\pdf', 'article.pdf'), 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()
