'''
Author: FunctionSir
Date: 2022-03-05 17:38:02
LastEditTime: 2022-08-04 22:40:34
LastEditors: FunctionSir
Description: 妹妹(即节点)
FilePath: /RealMisakaNetwork/sister.py
'''
import os
from pickle import FALSE
import colorama
import cpsc
import ufio
import StaticRes
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

UNIT_NAME = "Sister"  # 你可以自由更改这个组件的显示名称而不用更改文件名, 这样可以避免很多麻烦.

print("The RealMisakaNetwork Project - " + UNIT_NAME)
print("要(Y/y)清除先前输出么?")
temp = input(">>> ")
if temp == "Y" or temp == "y":
    cpsc.clear()
    print(Fore.MAGENTA + StaticRes.ASCII_MISAKA)
    print(Fore.GREEN + StaticRes.ASCII_NETWORK)
    print(Fore.CYAN + "版本: " + StaticRes.VER +
          " 版本代号: " + StaticRes.VER_CODENAME)
    print(Fore.BLUE + "这是一个自由软件, 使用AGPL v3许可证.")
    print("The RealMisakaNetwork Project - " + UNIT_NAME)
print(Fore.BLUE+"导入配置文件...")
if os.path.isfile(ufio.path_proc("lock/ready.lck", False)):
    print(Fore.CYAN+"from conf import python")
    from conf import python
    print(Fore.CYAN+"from conf import netcat")
    from conf import netcat
    print(Fore.CYAN+"from conf import miniserve")
    from conf import miniserve
    print(Fore.CYAN+"from conf import curl")
    from conf import curl
    print(Fore.CYAN+"from conf import wget")
    from conf import wget
    print(Fore.CYAN+"from conf import sister")
    from conf import sister
    print(Fore.GREEN + "配置文件导入已结束")
else:
    print(Style.BRIGHT+Fore.RED+"未找到\"" +
          ufio.path_proc("lock/ready.lck", False) + "\", 无法继续.")
    print(Fore.CYAN+"若为第一次运行, 请运行首次运行向导firstrun.py.")
    print(Fore.CYAN+"若确定只是此文件缺失, 请手动创建之.")
print(Fore.BLUE+"赋值配置常量(以变量形式)...")
PY = python.python
NC = netcat.netcat
MINISERVE = miniserve.miniserve
CURL_DL = curl.curlDownload
CURL_UL = curl.curlUpload
WGET_DL = wget.wgetDownload
SN = sister.sisterSN
NAME = sister.sisterName
CMD_IN_PROT = sister.sisterCmdInPort
FILE_SHARE_PORT = sister.sisterFileSharePort
print(Fore.GREEN + "配置常量(变量形式)已赋值.")
print(Fore.BLUE + "初始化全局变量...")
exitFlag = False  # 控制妹妹是否执行退出, 默认为False
cmdList = []  # 待执行指令列表, 默认为[]
print(Fore.GREEN + "定义且赋值了必要的全局变量.")
pass  # 未完待续
