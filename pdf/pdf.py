
import os
import time
import tkinter as tk
from shutil import move as file_mover
from tkinter import filedialog

import PyPDF2
from tqdm import tqdm

# I assume that pdfs are in this current directory
# Make sure that the files are named using sorting


userfilename = input('Name of file: ')
if userfilename == "":
    userfilename = "r_name"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

destination = os.path.join(BASE_DIR, "final")
if not os.path.isdir(destination):
    os.mkdir(destination)

root = tk.Tk()
root.withdraw()
filepath = filedialog.askopenfilenames()
print(filepath)

# pdf2merge = []
# os.chdir(BASE_DIR)
# for filename in os.listdir('.'):
#     if filename.endswith('.pdf'):
#         pdf2merge.append(filename)

# print("The following files were detected:")
# for i in pdf2merge:
#     print(i)

# print('To change order. Please, sort files based on number.')

# proceed = input("Press enter key to continue, or press any key to continue")


def merge_pdf(files):
    pdfWriter = PyPDF2.PdfFileWriter()

    # loop through all PDFs
    for filename in files:
        # rb for read binary
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # Opening each page of the PDF
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
    # save PDF to file, wb for write binary
    pdfOutput = open(userfilename.title()+'.pdf', 'wb')
    # Outputting the PDF
    pdfWriter.write(pdfOutput)
    # Closing the PDF writer
    pdfOutput.close()
    destination = filedialog.askdirectory()

    file_mover(os.path.join(BASE_DIR, userfilename.title()+".pdf"),
               os.path.join(destination, userfilename.title()+".pdf"))


# if proceed == '':
#     merge_pdf()
#     print("Done")
#     print("This window will close in:")
#     for i in tqdm(range(0, 10)):
#         time.sleep(0.5)
#     exit()

# else:
#     print("Thank you for checking out with us")
#     for i in tqdm(range(0, 30)):
#         time.sleep(0.1)
#     exit()


"""
If you face an error regarding multiple dictionary keys,
you have to edit the source code of the pypdf in your 
site packages and pass the error part
"""
