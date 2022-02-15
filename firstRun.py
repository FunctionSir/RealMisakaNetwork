'''
Author: FunctionSir
Date: 2022-01-01 17:48:44
LastEditTime: 2022-02-15 11:06:49
LastEditors: FunctionSir
Description: 首次运行向导
FilePath: /RealMisakaNetwork/firstRun.py
'''

import os
import colorama
import cpsc
import ufio
import staticRes
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print(Fore.GREEN+"欢迎来到第一次运行向导!")
print(Fore.CYAN+"您可以输入R来")
print(Fore.RED+Style.BRIGHT+"警告:若之前存在配置等,将可能会被清除!")
if input("[要继续,请输入「EXEC」（区分大小写）]>") == "EXEC":
    print("第1阶段:创建必要的文件夹.")
    print("配置文件夹conf:")
    cpsc.mkdir("", "conf")
    print("DONE")
    print("数据文件夹data:")
    cpsc.mkdir("", "data")
    print("DONE")
    print("锁文件夹lock:")
    cpsc.mkdir("", "lock")
    print("DONE")
    print("临时文件夹temp:")
    cpsc.mkdir("", "temp")
    print("DONE")
    print("第2阶段:创建必要的配置文件.")
    print("Python配置python.conf.py:")
    cpsc.mkfile("conf", "python.conf.py")
    print("DONE")
    print("Miniserve配置miniserve.conf.py:")
    cpsc.mkfile("conf", "miniserve.conf.py")
    print("DONE")
    print("Wget配置wget.conf.py:")
    cpsc.mkfile("conf", "wget.conf.py")
    print("DONE")
    print("Curl配置curl.conf.py:")
    cpsc.mkfile("conf", "curl.conf.py")
    print("DONE")
    print("妹妹设置sister.conf.py:")
    cpsc.mkfile("conf", "sister.conf.py")
    print("DONE")
    print("第3阶段:写入设置("+Fore.RED+Style.BRIGHT+"注意原有设置会丢失"+Style.RESET_ALL+").")
    print("小贴士:直接回车或仅输入\"#\"则会使用默认值.")
    temp = ""
    temp = input("要使用的用以运行Python3的命令:")
    if temp == "#" or temp == "":
        temp = staticRes.deafultPythonConfFileContent
        print("使用默认值,要写入的内容是:", temp)
        ufio.write_lines("conf", "python.conf.py", 1, temp, 2)
    else:
        ufio.write_lines("conf", "python.conf.py", 1, ("python = "+str(temp)).split(
            staticRes.strNGA+staticRes.strNGA+staticRes.strNGA), 2)

else:
    print(Fore.GREEN + "操作已取消")
