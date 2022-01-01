'''
Author: FunctionSir
Date: 2022-01-01 15:08:40
LastEditTime: 2022-01-01 17:00:42
LastEditors: FunctionSir
Description: 启动器
FilePath: /RealMisakaNetwork/start.py
'''
import os
import cpsc
import ufio
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

if not os.path.isfile(ufio.path_proc("lock/ready.lck", False)):
    print(Style.BRIGHT+Fore.RED+"未找到\"" +
          ufio.path_proc("lock/ready.lck", False)+"\"，无法继续。")
    print(Fore.CYAN+"若为第一次运行，请运行第一次运行向导firstRun.py。")
    print(Fore.CYAN+"若确定只是此文件缺失，请手动创建之。")
