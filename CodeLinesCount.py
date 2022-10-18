import os

suffixname = [".cpp", ".h", ".py", ".js", ".c", ".sh", ".java", ".asm", ".css", ".html", ".sql"]

filedict = \
    {"cpp": [],
     "h": [],
     "c": [],
     "py": [],
     "sh": [],
     "js": [],
     "java": [],
     "asm": [],
     "css": [],
     "html": [],
     "sql": []}

errorlist = []


def addfile(suffix, path, num):
    filedict[suffix[1:]].append([path, num])


def adderror(path, exception: Exception):
    errorlist.append(path + "\t" + exception.__str__())


def filelinescount(file_path: str, encoding=True):
    file = None
    if encoding is None:
        file = open(file_path, "r")
    else:
        file = open(file_path, "r", encoding="gb18030", errors="ignore")

    lines = file.readlines()
    ret = 0
    for line in lines:
        if line.split():
            ret += 1
    file.close()
    del lines
    return ret



def filecount(start_path: str):
    files = os.listdir(start_path)
    ret = 0
    ret_temp = 0
    for file in files:
        file_path = os.path.join(start_path + os.path.sep, file)
        if os.path.isfile(file_path):
            suffix = os.path.splitext(file)[-1]
            if suffix in suffixname:
                try:
                    ret_temp = filelinescount(file_path)
                    ret += ret_temp
                    addfile(suffix, file_path, ret_temp)
                except :
                    try:
                        ret_temp = filelinescount(file_path, False)
                        ret += ret_temp
                        addfile(suffix, file_path, ret_temp)
                    except Exception as E_result:
                        adderror(file_path, E_result)
                    continue
        elif os.path.isdir(file_path):
            print(file_path)
            ret += filecount(file_path)
    if ret != 0:
        print(start_path + "is count finished")
    del files
    return ret


start_path = []
print("请输入路径")
while True:
    temp_input = input()
    if temp_input == '0':
        break
    start_path.append(temp_input)

result = 0
for object in start_path:
    result += filecount(object)

print("\nCode lines is " + str(result))

writedfile = open("../record.txt", "w+")
for key in filedict:
    writedfile.write("\n" + key + "\n")
    for path in filedict[key]:
        writedfile.write(path[0] + "\t" + str(path[1]) + "\n")
    writedfile.write("\n")

errorfile = open("../error.txt", "w+")
for error in errorlist:
    errorfile.write(error + "\n")

