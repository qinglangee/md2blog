# -*- coding: utf-8 -*-

def add(a,b):
    return a+b


    
# 组合 csv 字符串， 有引号的时行转义
def appendCsv(old, newStr):
    if(old == None):
        old = ""
    if(len(newStr)) < 1:
        return old + ","
    newStr = newStr.replace("\"", "\"\"")
    return old + ",\"" + newStr + "\""


# 列表内容写入文件。覆盖
def writeList(filename, list, toString=None):
    content = getListContent(list, toString)
    writeFile(filename, content)

# 列表内容转换为字符串
def getListContent(list, toString=None):
    content = ""
    for item in list:
        content = content + (toString(item) if toString != None else str(item)) + "\n"
    return content
# 列表内容写入文件。 追加 
def appendList(filename, list, toString=None):
    content = getListContent(list, toString)
    appendFile(filename, content)

# 写入文件内容。覆盖
def writeFile(filename, content):
    file_object = open(filename, 'w')
    file_object.write(content)
    file_object.close()

# 追加文件内容
def appendFile(filename, content):
    file_object = open(filename, 'a')
    file_object.write(content)
    file_object.close()

# 读取文件内容
def readFile(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content
# 读取文件内容,以行分割,存储到一个列表, 可以设置只读前 max 行
def readLines(filename, max=0):
    lines = [];
    f = open(filename, "r")
    if (max > 0):
        index = 1;  
        for line in f:  
            lines.append(line);
            index = index + 1
            if(index > max):
                break
    else:
        for line in f:  
            lines.append(line);
        
    f.close()  
    return lines;

def nouse():
    return 0