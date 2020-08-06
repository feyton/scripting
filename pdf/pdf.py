
import os
import PyPDF2

# I assume that pdfs are in this current directory
# Make sure that the files are named using sorting
userfilename = input('Name of file: ')


pdf2merge = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf2merge.append(filename)

pdfWriter = PyPDF2.PdfFileWriter()

# loop through all PDFs
for filename in pdf2merge:
    # rb for read binary
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# Opening each page of the PDF
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
# save PDF to file, wb for write binary
pdfOutput = open(userfilename+'.pdf', 'wb')
# Outputting the PDF
pdfWriter.write(pdfOutput)
# Closing the PDF writer
pdfOutput.close()

"""
If you face an error regarding multiple dictionary keys,
you have to edit the source code of the pypdf in your 
site packages and pass the error part
"""
