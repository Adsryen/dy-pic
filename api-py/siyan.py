# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:20:54 2021

@author: Anderson Ryen
"""

import os

#文件的绝对路径
file_path = "E:\GitHub Desktop\GitHub\dy-pic\siyan\\"
#CDN前缀
web_path = "https://cdn.jsdelivr.net/gh/"
#GITHUB账户名
user_path = "anderson-ryen"
#仓库名
warehouse_path = "dy-pic"
#仓库内文件夹
img_path = "siyan"
#合并path
api_path = os.path.join( web_path + user_path + "/" + warehouse_path + "/" + img_path + "/")


print("")
print("前缀预览: " + api_path)
print("")
print("=" *50)
print("siyan已完成")
print("地址预览：E:\GitHub Desktop\GitHub\dy-pic\\api-py\siyan.txt")
print("=" *50)
print("")

if __name__ == '__main__':
    filelist = os.listdir(file_path)
    with open(r"E:\GitHub Desktop\GitHub\dy-pic\api-py\siyan.txt",'w',encoding='utf-8') as f:
        for file in filelist:
            f.write(api_path+file+'\n')
