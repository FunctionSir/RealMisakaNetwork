'''
Author: FunctionSir
Date: 2021-09-21 19:06:36
LastEditTime: 2022-01-01 17:41:04
LastEditors: FunctionSir
Description: UniversalFilesIO 通用文件IO
FilePath: /RealMisakaNetwork/ufio.py
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


def new(path, name, overWritten):
    if overWritten and os.path.isfile(path_proc(path, True)+name):
        cpsc.rmfile(path, name)
    r = cpsc.mkfile(path, name)
    return r


def read_lines(path, name, lineEnds):
    r = -32768
    file = path_proc(path, True)+name
    if not os.path.isfile(file):
        return r
    else:
        temp = open(file)
        r = temp.read().splitlines(lineEnds)
    return r
