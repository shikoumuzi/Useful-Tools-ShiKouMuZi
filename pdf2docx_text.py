from pdf2docx import Converter
pdf_file = input("请输入源pdf路径： ")
docx_file = input("请输入目标owrd路径 ")
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()
