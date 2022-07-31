'''
Author: FunctionSir
Date: 2021-09-21 09:35:07
LastEditTime: 2022-07-29 15:13:37
LastEditors: FunctionSir
Description: CrossPlatformSystemCommands，自动判断操作系统的系统并执行指令
FilePath: /RealMisakaNetwork/cpsc.py
'''

import os
import platform
import ufio


def is_win():
    r = False
    winSymbol = "Windows"
    if os.path.isfile("iswindows.lck"):
        r = True
    elif os.path.isfile("notwindows.lck"):
        r = False
    else:
        if platform.system() == winSymbol:
            r = True
        else:
            r = False
    return r


def clear():
    r = -32768
    winCmd = "cls"
    POSIXCmd = "clear"
    if is_win():
        r = os.system(winCmd)
    else:
        r = os.system(POSIXCmd)
    return r


def mkfile(path, name):
    r = -32768
    path = ufio.path_proc(path, True)
    winCmd = "copy nul " + path + name
    POSIXCmd = "touch " + path + name
    if is_win():
        r = os.system(winCmd)
    else:
        r = os.system(POSIXCmd)
    return r


def mkdir(path, name):
    r = -32768
    path = ufio.path_proc(path, True)
    winCmd = "mkdir " + path + name
    POSIXCmd = "mkdir " + path + name
    if is_win():
        r = os.system(winCmd)
    else:
        r = os.system(POSIXCmd)
    return r


def rmfile(path, name):
    r = -32768
    path = ufio.path_proc(path, True)
    winCmd = "del " + path + name
    POSIXCmd = "rm " + path + name
    if is_win():
        r = os.system(winCmd)
    else:
        r = os.system(POSIXCmd)
    return r


def ping(dest):
    r = -32768
    winCmd = "ping " + dest
    POSIXCmd = "ping -c 4 " + dest
    if is_win():
        r = os.system(winCmd)
    else:
        r = os.system(POSIXCmd)
    return r


def more(path, name):
    r = -32768
    path = ufio.path_proc(path, True)
    winCmd = "more " + path + name
    POSIXCmd = "more " + path + name
    if is_win():
        r = os.system(winCmd)
    else:
        r = os.system(POSIXCmd)
    return r
