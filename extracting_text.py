import PyPDF2
from pathlib import Path

pdf_file_object = open(Path.home() / Path('Desktop', 'hello.pdf'), 'rb')

pdf_reader = PyPDF2.PdfFileReader(pdf_file_object)

# pages number
print('Page number :', pdf_reader.numPages)

# read
page_obj = pdf_reader.getPage(0)
print('Text in file :', page_obj.extractText())

pdf_file_object.close()
