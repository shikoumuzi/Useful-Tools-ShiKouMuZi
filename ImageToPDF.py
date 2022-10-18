from PIL import Image
import os


def combine2Pdf(folderpath, pdffilepath):
    files = os.listdir(folderpath)
    imagefiles = []
    sources = []
    for file in files:
        imagefiles.append(folderpath + os.path.sep + file)
    imagefiles.sort()
    output = Image.open(imagefiles[0])
    imagefiles.pop(0)
    for file in imagefiles:
        imagefile = Image.open(file)
        sources.append(imagefile)
    output.save(pdffilepath, "pdf", save_all=True, append_images=sources)


floder = input("请输入需要批量制作成pdf的图片文件路径： ")
pdf = input("请输入需要导出的路径： ")
combine2Pdf(floder, pdf)
