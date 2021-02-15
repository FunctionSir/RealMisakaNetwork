'''
The Project-RealMisakaNetwork
Version: alpha-1
License: AGPL
File Description:
File I/O Lib
'''
import os
import shutil

def candmdir(which): #Clean And Make Dir
    if os.path.isdir(which):
        print('[W]文件夹', which, '已存在，删除。')
        shutil.rmtree(which)
    os.mkdir(which)


def candmnod(which): #Clean And Make Nod
    if os.path.isfile(which):
        print('[W]文件', which, '已存在，删除。')
        os.remove(which)
    os.mknod(which)

def fileread(which):
    f = open(which,'r')
    r = f.read()
    f.close()
    return r

def filewrite(which,what):
    f = open(which,"w")
    f.writelines(what)
    f.close()