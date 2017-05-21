# -*- coding: utf-8 -*-
import config as G
import common_util as C
import zhlog as LOG
# import urllib2
# import urllib
# import sys
import os
import re
# import time
# import random
import traceback
import datetime
import shutil

all_files=[];

def gci (path):
    """this is a statement"""
    parents = os.listdir(path)
    for parent in parents:
        if(parent == ".git"):
            continue
        child = os.path.join(path,parent)
        #print(child)
        if os.path.isdir(child):
            gci(child)
        else:
            add_file(child)

def add_file(filepath):
    filename = os.path.basename(filepath)
    name, ext = os.path.splitext(filename)
    parent = os.path.basename(os.path.dirname(filepath))
    file={"name":name, "path":filepath, "parent":parent}
    dateReg = "(\d{4})-(\d{2})-(\d{2})"
    dateMatch=re.search(dateReg, name)
    if(dateMatch != None):
        file["year"] = dateMatch.groups()[0]
        file["month"] = dateMatch.groups()[1]
        file["day"] = dateMatch.groups()[2]
        f = open(file["path"], "r")  
        title = ""
        for line in f:
            if(line.startswith("#")):
                title = line[1:].strip()
                break;
        f.close()
        if(title == ""):
            file["title"] = name;
        else:
            file["title"] = title;
        all_files.append(file)
    else:
        print "not blog file:", name
    
# 根据 file ,创建一个html文件,放到path中    
def create_html(templet, file, dest_path, pre_file=None, next_file=None):
    temp = templet.replace("${content}", read_markdown(file["path"]));
    temp = temp.replace("${title}", file["title"]);
    if(pre_file != None):
        temp = temp.replace("${pre_link}", getLink(pre_file))
        temp = temp.replace("${pre_title}", pre_file["title"])
    else:
        temp = temp.replace("${pre_link}", "/")
        temp = temp.replace("${pre_title}", "首页")
        
    if(next_file != None):
        temp = temp.replace("${next_link}", getLink(next_file))
        temp = temp.replace("${next_title}", next_file["title"])
    else:
        temp = temp.replace("${next_link}", "/")
        temp = temp.replace("${next_title}", "首页")
    
    C.writeFile(os.path.join(dest_path, file["name"] + ".html"), temp);

# 组装文件对应的链接
def getLink(file):
    return "/blog/" + file["parent"] + "/" + file["year"] + "/" + file["name"] + ".html"
# 创建首页
def create_index(files):
    files.reverse();
    content = C.readFile("index_templet.html")
    links = ""
    for file in files:
        links = links + "<div>"
        links = links + "<a class='title' href='"+getLink(file)+"'>" + file["title"] + "</a><br>"
        links = links + "<div class='markdown_box'>"
        links = links + "<pre class='markdown_src'>"
        links = links + read_markdown(file["path"], 10)
        links = links + "</pre>"
        links = links + "</div>"
        links = links + "</div>"
    content = content.replace("${links}", links)
    C.writeFile(os.path.join(G.dest_path, "index.html"), content)
# 读取 markdown, 转义尖括号
def read_markdown(path, lines= 0):
    markdown = ""
    if(lines > 0):
        markdown = C.getListContent(C.readLines(path, lines))
    else:
        markdown = C.readFile(path);
    markdown = markdown.replace("<", "&lt;")
    markdown = markdown.replace(">", "&gt;")
    return markdown
# 静态文件 copy 到目标目录
def copy_static_resources():
    static_path = os.path.join(G.dest_path, "static")
    if(os.path.exists(static_path)):
        shutil.rmtree(static_path)
    shutil.copytree("static_resources", static_path)
    
# 入口
gci(G.src_path)
all_files.sort(lambda p1, p2:cmp(p1["name"], p2["name"]))
print len(all_files)
index = 0;
templet=C.readFile("page_template.html")
while index < len(all_files):
    file = all_files[index]
    path = os.path.join(G.dest_path, "blog")
    path = os.path.join(path, file["parent"])
    path = os.path.join(path, file["year"])
    if(not os.path.exists(path)):
        os.makedirs(path)
    
    pre_file = None if index == 0 else all_files[index - 1]
    next_file = None if index + 1 == len(all_files) else all_files[index + 1]
    create_html(templet, file, path, pre_file, next_file)
    # print file["name"]
    index = index+1

create_index(all_files[-10:])
copy_static_resources()
print "index is", index

# shutil.copytree("/home/zhch/temp/d3/static/", "/home/zhch/temp/d3/abc")


