from pdf2docx import Converter

pdf = "sample.pdf"
docx = "sample.docx"

cv = Converter(pdf_file=pdf)
cv.convert(docx_filename=docx)
cv.close()
