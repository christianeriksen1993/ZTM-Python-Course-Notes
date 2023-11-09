import PyPDF2
import sys

"""with open("dummy.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]
    page.rotate(270)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open("tilt.pdf", "wb") as new_file:
        writer.write(new_file)"""

"""inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("super.pdf")

pdf_combiner(inputs)"""


# Watermark exercise
"""
# Open input pdf and watermark
pdf = PyPDF2.PdfReader(open("super.pdf", "rb"))
watermark = PyPDF2.PdfReader(open("wtr.pdf", "rb"))
writer = PyPDF2.PdfWriter() # Creates writer object class
# determine number of pages
numPages = len(pdf.pages)
# Loop through each page of PDF
for i in range(0, numPages):
    current_page = pdf.pages[i]
    watermark_page = watermark.pages[0] 

    current_page.merge_page(watermark_page) # Merge current page with watermark
    writer.add_page(current_page) # Add current page to writer

with open("watermarked_output.pdf", "wb") as file: # Write pages to new file
    writer.write(file)
"""


