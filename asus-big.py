#!/usr/bin/python
import os

def search(root, target):
    items = os.listdir(root)
    for item in items:
        path = os.path.join(root, item)
        if os.path.isdir(path):
            search(path, target)
        if target in path.split('/')[-1]:
            os.system("convert " + path + " " + path + ".gif")
            os.system("convert -strip -quality 75% " + path + ".gif " + path + ".gif")
            os.system("rm " + path)
            os.system("mv " + path + ".gif " + path)
            
search("fmk/rootfs/www/images/", ".png")


