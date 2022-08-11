'''
Author: FunctionSir
Date: 2022-03-05 17:38:02
LastEditTime: 2022-08-11 23:47:27
LastEditors: FunctionSir
Description: 妹妹(即节点)
FilePath: /RealMisakaNetwork/sister.py
'''
import os
import _thread
import colorama
import cpsc
import ufio
import StaticRes
from switchtools.switchcase import Switch, Case
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
if os.path.isfile(ufio.path_proc("lock/ready.lck", False)):
    print(Fore.BLUE+"导入配置文件...")
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
else:
    print(Style.BRIGHT+Fore.RED+"未找到\"" +
          ufio.path_proc("lock/ready.lck", False) + "\", 无法继续.")
    print(Fore.CYAN+"若为第一次运行, 请运行首次运行向导firstrun.py.")
    print(Fore.CYAN+"若确定只是此文件缺失, 请手动创建之.")
    print(Fore.RED+Style.BRIGHT+"由于发生某些错误将退出.")
    exit()

print(Fore.BLUE + "初始化全局变量...")
exitFlag = False  # 控制妹妹是否执行退出, 默认为False
cmdToDoList = []  # 待执行命令列表, 默认为空.
cmdToTxList = []  # 待发送命令列表, 默认为空.
print(Fore.GREEN + "定义且赋值了必要的全局变量.")


def cmd_rx():
    global CMD_IN_PROT
    global cmdToDoList
    cycleCount = 0
    while True:
        print("\n[CR] Start CmdRxCycle " + str(cycleCount)+" .")
        temp = (os.popen(NC + " " + "-l -w  8 -p" +
                " " + str(CMD_IN_PROT)).readlines())
        print("\n[CR] Received " + str(temp) + " in this cycle.")
        for i in temp:
            cmdToDoList.append(i.rstrip("\n"))
        print("\n[CR] Command(s) received was added to the CmdToDoList.")
        print("\n[CR] Now cmdToDoList = "+str(cmdToDoList)+" .")
        print("\n[CR] End CmdRxCycle " + str(cycleCount)+" .")
        cycleCount = cycleCount + 1


def cmd_default():
    global cmdToDoList
    if cmdToDoList[0] == "default":
        print("\n[CMD::DEFAULT] 收到 \"default\" 忽略并从cmdToDoList中移除.")
    else:
        print("\n[CMD::DEFAULT] 收到 \""+cmdToDoList[0] +
              "\" 然而这并不是一个有效命令, 忽略并从cmdToDoList中移除.")
    pass
    del cmdToDoList[0]


def cmd_exit():
    global exitFlag
    global cmdToDoList
    print("\n[CMD::EXIT] 收到退出命令, 将exitFlag设置为True.")
    exitFlag = True
    del cmdToDoList[0]


def cmd_sys():
    global cmdToDoList
    if len(cmdToDoList) >= 2:
        if cmdToDoList[0] != "^C":
            print("\n[CMD::SYS] 将要执行系统命令 \"" + cmdToDoList[1] + "\".")
            os.system(cmdToDoList[1])
            print("\n[CMD::SYS] 系统指令 \"" + cmdToDoList[1] + "\" 执行结束.")
        else:
            print("\n[CMD::SYS] ^C! 取消!")
        del cmdToDoList[1]
        del cmdToDoList[0]
    else:
        print(
            "\n[CMD::SYS] 语法错误或接收错误: 正确的sys命令有且只有两行, 第一行是sys, 第二行为需要执行的系统指令. 若第二行为字符串 \"^C\", 则取消.")
        print("\n[CMD::SYS] 等待新的字符串进入...")
        del cmdToDoList[0]
        while(1):
            if len(cmdToDoList) >= 1:
                if cmdToDoList[0] != "^C":
                    print("\n[CMD::SYS] 将要执行系统命令 \"" + cmdToDoList[0] + "\".")
                    os.system(cmdToDoList[0])
                    print("\n[CMD::SYS] 系统指令 \"" + cmdToDoList[0] + "\" 执行结束.")
                    del cmdToDoList[0]
                    break
                else:
                    print("\n[CMD::SYS] ^C! 取消!")
                    del cmdToDoList[0]
                    break


def cmd_py():
    global cmdToDoList
    if len(cmdToDoList) >= 2:
        print("\n[CMD::PY] 将要执行Python 3语句 \"" + cmdToDoList[1] + "\".")
        exec(cmdToDoList[1])
        print("\n[CMD::PY] Python 3语句 \"" + cmdToDoList[1] + "\" 执行结束.")
        del cmdToDoList[1]
        del cmdToDoList[0]
    else:
        print("\n[CMD::PY] 语法错误或接收错误: 正确的py命令有且只有两行, 第一行是py, 第二行为需要执行的Python 3语句.")
        del cmdToDoList[0]


def cmd_run():
    global cmdToDoList
    while True:
        if len(cmdToDoList) >= 1:
            Switch(cmdToDoList[0], [
                Case("exit", lambda:cmd_exit()),
                Case("sys", lambda: cmd_sys()),
                Case("py", lambda: cmd_py()),
                Case("default", lambda: cmd_default())
            ])


def cmd_tx():
    pass


def file_rx():
    pass


def file_tx():
    pass


try:
    _thread.start_new_thread(cmd_rx, ())
    _thread.start_new_thread(cmd_run, ())
    _thread.start_new_thread(cmd_tx, ())
    _thread.start_new_thread(file_rx, ())
    _thread.start_new_thread(file_tx, ())
except:
    temp = input(Fore.RED + Style.BRIGHT + "错误: 无法正常启动某个线程! 退出.")
    exit()
while True:
    if exitFlag == True:
        print("[MAIN] exitFlag 被设置为 \"True\", sister.py将退出!")
        exit()
