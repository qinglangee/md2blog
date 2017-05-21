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
        all_files.append(file)
    else:
        print "not blog file:", name
    
# 根据 file ,创建一个html文件,放到path中    
def create_html(templet, file, dest_path):
    content = C.readFile(file["path"]);
    temp = templet.replace("${content}", content);
    C.writeFile(os.path.join(dest_path, file["name"] + ".html"), temp);

# 创建首页
def create_index(files):
    content = C.readFile("index_templet.html")
    links = ""
    for file in files:
        links = links + "<a href='blog/"+file["parent"] + "/" + file["year"] + "/" + file["name"] + ".html"+"'>" + file["name"] + "</a><br>"
    content = content.replace("${links}", links)
    C.writeFile(os.path.join(G.dest_path, "index.html"), content)

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
    create_html(templet, file, path)
    # print file["name"]
    index = index+1

create_index(all_files[-10:])
copy_static_resources()
print "index is", index

# shutil.copytree("/home/zhch/temp/d3/static/", "/home/zhch/temp/d3/abc")


