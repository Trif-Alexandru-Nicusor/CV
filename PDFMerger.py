import PyPDF2
import os
directory = 'B:/Projects/Teste/New folder'
pdf_files = []
for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        pdf_files.append(os.path.join(directory, filename))
pdf_files.sort()
pdf_writer = PyPDF2.PdfWriter()
for pdf_file in pdf_files:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])
with open('combined.pdf', 'wb') as out_file:
    pdf_writer.write(out_file)
print('PDF files merged into combined.pdf')
