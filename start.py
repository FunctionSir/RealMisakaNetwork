'''
Author: FunctionSir
Date: 2022-01-01 15:08:40
LastEditTime: 2022-08-03 23:35:01
LastEditors: FunctionSir
Description: 启动器
FilePath: /RealMisakaNetwork/start.py
'''

import os
import colorama
import cpsc
import ufio
import StaticRes
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
UNIT_NAME = "启动器"
print(Fore.MAGENTA + StaticRes.ASCII_MISAKA)
print(Fore.GREEN + StaticRes.ASCII_NETWORK)
print("The " + StaticRes.PROJECT_NAME+" Project - " + UNIT_NAME)
print("版本：" + StaticRes.VER + " 版本代号：" + StaticRes.VER_CODENAME)
if not os.path.isfile(ufio.path_proc("lock/ready.lck", False)):
    print(Style.BRIGHT+Fore.RED+"未找到\"" +
          ufio.path_proc("lock/ready.lck", False) + "\"，无法继续。")
    print(Fore.CYAN+"若为第一次运行，请运行第一次运行向导firstrun.py。")
    print(Fore.CYAN+"若确定只是此文件缺失，请手动创建之。")
else:
    print(Fore.CYAN+"读取配置文件...")
    from conf import python
    PYTHON_CMD = python.python
    print(Fore.GREEN+"启动sister.py...")
    os.system(PYTHON_CMD + " " + "sister.py")
    input("按下Enter继续...")
