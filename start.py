'''
Author: FunctionSir
Date: 2022-01-01 15:08:40
LastEditTime: 2022-02-15 19:37:40
LastEditors: FunctionSir
Description: 启动器
FilePath: /RealMisakaNetwork/start.py
'''

import os
import colorama
import cpsc
import ufio
import staticRes
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
unitName = "启动器"
print(Fore.MAGENTA + staticRes.ASCIIMisaka)
print(Fore.GREEN + staticRes.ASCIINetwork)
print("The " + staticRes.projectName+" Project - " + unitName)
print("版本：" + staticRes.ver+" 版本代号：" + staticRes.verCodename)
if not os.path.isfile(ufio.path_proc("lock/ready.lck", False)):
    print(Style.BRIGHT+Fore.RED+"未找到\"" +
          ufio.path_proc("lock/ready.lck", False) + "\"，无法继续。")
    print(Fore.CYAN+"若为第一次运行，请运行第一次运行向导firstRun.py。")
    print(Fore.CYAN+"若确定只是此文件缺失，请手动创建之。")
else:
    pass
# 未完待续
