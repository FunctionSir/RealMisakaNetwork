'''
Author: FunctionSir
Date: 2022-01-01 17:48:44
LastEditTime: 2022-01-01 22:09:45
LastEditors: FunctionSir
Description: 首次运行向导
FilePath: /RealMisakaNetwork/firstRun.py
'''

import os
import colorama
import cpsc
import ufio
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print(Fore.GREEN+"欢迎来到第一次运行向导！")
print(Style.BRIGHT+Fore.RED+"警告：若之前存在配置等，将可能会被清除！")
if input("[要继续，请输入「EXEC」（区分大小写）]") == "EXEC":
    print("第一阶段：创建必要的文件夹。")
    print("配置文件夹conf：")
    cpsc.mkdir("", "conf")
    print("DONE")
    print("数据文件夹data：")
    cpsc.mkdir("", "data")
    print("DONE")
    print("锁文件夹lock：")
    cpsc.mkdir("", "lock")
    print("DONE")
    print("临时文件夹temp：")
    cpsc.mkdir("", "temp")
    print("DONE")
    print("第一阶段：创建必要的配置文件。")
    print("Python配置python.conf：")
    cpsc.mkfile("conf", "python.conf")
    print("DONE")
    print("Miniserve配置miniserve.conf：")
    cpsc.mkfile("conf", "miniserve.conf")
    print("DONE")
    print("Wget配置wget.conf：")
    cpsc.mkfile("conf", "wget.conf")
    print("DONE")
    print("Curl配置curl.conf：")
    cpsc.mkfile("conf", "curl.conf")
    print("DONE")
    print("妹妹基本设置basic.conf")
    cpsc.mkfile("conf", "basic.conf")
    print("DONE")
else:
    print(Fore.GREEN + "操作已取消")
