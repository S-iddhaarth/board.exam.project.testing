import PyPDF2
file = open(r'/Users/siddhaarthsekar/Desktop/page.pdf', "rb")
pdf_reader = PyPDF2.PdfFileReader(file)
page_1= pdf_reader.getPage(0)
print(page_1.extractText())