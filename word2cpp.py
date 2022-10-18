import os
from win32com import client as wc
import docx
srcpath = input("请输入源文件夹路径： ")

files = os.listdir(srcpath)
word = wc.Dispatch("Word.Application")

for file in files:
    if os.path.splitext(file)[-1] == ".doc":
        cppfile = open(srcpath + os.path.sep + os.path.splitext(file)[0] + ".cpp", "w+", encoding="utf-8")
        # docfile = open(srcpath + os.path.sep + file, "r", encoding="utf-8", errors="ignore")
        # docfilelines = docfile.readlines()
        # for lines in docfilelines:
        #     cppfile.write(lines + "\n")
        filename = os.path.splitext(file)[0]
        doc = word.Documents.Open(srcpath + os.path.sep + file)
        doc.SaveAs(srcpath + os.path.sep + filename + ".docx", 12)
        doc.Close()

        docstr = docx.Document(srcpath + os.path.sep + filename + ".docx")
        for par in docstr.paragraphs:
            cppfile.write(par.text)
        os.remove(srcpath + os.path.sep + filename + ".docx")
        cppfile.close()

word.Quit()
