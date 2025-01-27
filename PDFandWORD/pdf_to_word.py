from pdf2docx import Converter

pdf = 'academy_1.pdf'
docx = 'docx_academy_1.docx'



cv = Converter(pdf)

# # convert from the second page to the end (by default)
# cv.convert(docx, start=1)

# # convert from the first page (by default) to the third (end=3, excluded)
# cv.convert(docx, end=3)

# # convert from the second page and the third
# cv.convert(docx, start=1, end=3)

cv.convert(docx)
cv.close()

