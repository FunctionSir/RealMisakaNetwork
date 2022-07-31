'''
Author: FunctionSir
Date: 2021-09-21 19:06:36
LastEditTime: 2022-03-05 15:30:28
LastEditors: FunctionSir
Description: UniversalFilesIO 通用文件IO
FilePath: /RealMisakaNetwork/UFIO.py
'''

from math import isfinite
import os
import cpsc


def path_proc(path, slashAtEnd):
    if path != "":
        if cpsc.is_win():
            path = path.replace("/", "\\")
        else:
            path = path.replace("\\", "/")
        if slashAtEnd and path[-1] != "/" and path[-1] != "\\":
            if cpsc.is_win():
                path = path + "\\"
            else:
                path = path + "/"
    r = path
    return r


def new(path, name, overWrite):
    if overWrite and os.path.isfile(path_proc(path, True)+name):
        cpsc.rmfile(path, name)
    r = cpsc.mkfile(path, name)
    return r


def read_lines(path, name, keepEnds):
    r = -32768
    file = path_proc(path, True)+name
    if not os.path.isfile(file):
        return r
    else:
        temp = open(file)
        r = temp.read().splitlines(keepEnds)
    temp.close()
    return r


'''
对函数"write_lines(path, name, overWrite, strList, addEnds)"的部分说明：
当addEnds=0时，不对strList做任何处理，
当addEnds=1时，将会对strList中的每个字符串末尾加入\n，
当addEnds=其他值时，将会自动按照末尾为\n则不加，非\n则加\n的策略对strList中的每个字符串做处理。
'''


def write_lines(path, name, overWrite, strList, addEnds):
    r = -32768
    j = 0
    file = path_proc(path, True)+name
    if overWrite == True:
        temp = open(file, "w")
    else:
        temp = open(file, "a")
    if addEnds == 0:
        pass
    elif addEnds == 1:
        for i in strList:
            strList[j] = i + "\n"
            j = j+1
    else:
        for i in strList:
            if i[-1] != "\n":
                strList[j] = i + "\n"
            j = j+1
    temp.writelines(strList)
    temp.close()
    r = 0
    return r
