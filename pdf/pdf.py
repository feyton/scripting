
import os
import random
import shutil
import time
import tkinter as tk
import warnings
from datetime import datetime
from tkinter import filedialog

import PyPDF2
from art import tprint

# I assume that pdfs are in this current directory
# Make sure that the files are named using sorting
tprint("PDF Tools")

print("""
Use this tool to combine pdf files.
Please select files in order of ranking as the 
order will not be changed in merging.

        Thank you!!!
""")
print("##################################\n")
userfilename = input(
    'Enter name of file or \n Press enter to assign randomly:\n>>> ')
if userfilename == "":
    date = datetime.now().date()
    userfilename = "1_Combined_on_%s" % date


def change_files_order(l1, l2):
    new_list = []
    return new_list


def get_file():
    directory = os.getcwd()
    path = os.path.join(
        directory, f"{userfilename.title()}.pdf")
    return path


def move_pdf(destination):
    files = get_file()
    try:
        shutil.move(files, destination)
    except shutil.Error:
        proceed = input(
            "The file with same name exists:\nReplace? .... 'Y' or 'N'\n### ")
        if proceed.lower() == 'y':
            shutil.move(files, os.path.join(
                destination, f"{userfilename.title()}.pdf"))
        elif proceed.lower() == 'n':
            shutil.move(files, os.path.join(
                destination, f"{userfilename.title()}_{random.randint(10,50)}.pdf"))
        else:
            exit()


def merge_pdf(files):
    warnings.filterwarnings('ignore')
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
    print("##############\nSelect where the file will be saved.\n########\n")
    destination = filedialog.askdirectory()
    move_pdf(destination)
    print("\n################\nFiles have been merged.\n########\n")


root = tk.Tk()
root.withdraw()
print("##################################\n")
print("Please, choose the files to merge.")
print("##################################\n")
filepath = filedialog.askopenfilenames()
if len(filepath) <= 1:
    print("You did not choose files.")
    tprint("BYE")
    time.sleep(3)
    exit()
print("##################################\n")
print("The following files will be merged.")
for (i, item) in enumerate(filepath, start=1):
    item = item.split("/")[-1]
    print("# %s. >>%s" % (i, item))
time.sleep(1)


merge_pdf(filepath)
tprint("Thank You")
time.sleep(3)
