'''
Author: FunctionSir
Date: 2022-01-01 17:48:44
LastEditTime: 2022-08-04 22:06:55
LastEditors: FunctionSir
Description: 首次运行向导
FilePath: /RealMisakaNetwork/firstrun.py
'''

import os
import colorama
import cpsc
import ufio
import StaticRes
from colorama import Fore, Back, Style


colorama.init(autoreset=True)


UNIT_NAME = "第一次运行向导"  # 你可以自由更改这个组件的显示名称而不用更改文件名, 这样可以避免很多麻烦.
DIRS = ["conf", "data", "lock", "temp"]
DIRS_USAGE = ["配置", "数据", "锁", "临时"]
CONF_FILES = ["python.py", "netcat.py", "miniserve.py",
              "wget.py", "curl.py", "sister.py"]
CONF_USAGE = ["Python", "NetCat", "Miniserve", "Wget", "cURL", "妹妹(节点)"]


def gen_dir(dirName, usage):
    print("创建", usage, "文件夹", dirName)
    cpsc.mkdir("", dirName)


def gen_conf_file(fileName, usage):
    print("创建", usage, "配置文件", fileName)
    cpsc.mkfile("conf", fileName)


print(Fore.GREEN+"欢迎来到", UNIT_NAME)
print(Fore.RED+Style.BRIGHT+"警告:若之前存在配置等,将可能会被清除!")
if input("[要继续,请输入「EXEC」(区分大小写)]\n>>> ") == "EXEC":

    print("第1阶段:创建必要的文件夹.")
    i, j = 0, 0
    for i in DIRS:
        gen_dir(i, DIRS_USAGE[j])
        j = j + 1

    print("第2阶段:创建必要的配置文件.")
    i, j = 0, 0
    for i in CONF_FILES:
        gen_conf_file(i, CONF_USAGE[j])
        j = j + 1

    i, j = 0, 0

    print("第3阶段:写入设置("+Fore.RED+Style.BRIGHT+"注意原有设置会丢失"+Style.RESET_ALL+").")
    print("小贴士:直接回车或仅输入\"#\"则会使用默认值.\n"+Fore.GREEN +
          "注意: 若要写入默认值, 则将写入的内容将以list形式展示, 请不要惊慌.")

    '''
    来自ufio.py:
    对函数"ufio.write_lines(path, name, overWrite, strList, addEnds)"的部分说明：
    当addEnds=0时，不对strList做任何处理，
    当addEnds=1时，将会对strList中的每个字符串末尾加入\n，
    当addEnds=其他值时，将会自动按照末尾为\n则不加，非\n则加\n的策略对strList中的每个字符串做处理。
    '''

    temp = ""
    temp = input("要使用的用以运行Python 3的命令\n>>> ")
    if temp == "#" or temp == "":
        temp = StaticRes.DEAFULT_PYTHON_CONF_FILE_CONTENT
        print("使用默认值, 要写入的内容是:", temp)
        ufio.write_lines("conf", "python.py", 1, temp, 2)
    else:
        ufio.write_lines("conf", "python.py", 1, ("python = "+str(temp)).split(
            StaticRes.STR_NGA+StaticRes.STR_NGA+StaticRes.STR_NGA), 2)

    temp = ""
    temp = input("要使用的用以运行netcat的命令\n>>> ")
    if temp == "#" or temp == "":
        temp = StaticRes.DEAFULT_NETCAT_CONF_FILE_CONTENT
        print("使用默认值, 要写入的内容是:", temp)
        ufio.write_lines("conf", "netcat.py", 1, temp, 2)
    else:
        ufio.write_lines("conf", "netcat.py", 1, ("netcat = "+str(temp)).split(
            StaticRes.STR_NGA+StaticRes.STR_NGA+StaticRes.STR_NGA), 2)

    temp = ""
    temp = input("要使用的用以运行Miniserve的命令\n>>> ")
    if temp == "#" or temp == "":
        temp = StaticRes.DEAFULT_MINISERVE_CONF_FILE_CONTENT
        print("使用默认值, 要写入的内容是:", temp)
        ufio.write_lines("conf", "miniserve.py", 1, temp, 2)
    else:
        ufio.write_lines("conf", "miniserve.py", 1, ("miniserve = "+str(temp)).split(
            StaticRes.STR_NGA+StaticRes.STR_NGA+StaticRes.STR_NGA), 2)

    print("GNU Wget设置将使用默认值(一般不需要更改).")
    temp = StaticRes.DEAFULT_WGET_CONF_FILE_CONTENT
    print("使用默认值, 要写入的内容是:", temp)
    ufio.write_lines("conf", "wget.py", 1, temp, 2)

    print("GNU cURL设置将使用默认值(一般不需要更改, 除非您不使用默认的Miniserve作为HTTP(S)服务器).")
    temp = StaticRes.DEAFULT_CURL_CONF_FILE_CONTENT
    print("使用默认值, 要写入的内容是:", temp)
    ufio.write_lines("conf", "curl.py", 1, temp, 2)

    print("接下来设置妹妹(节点).")
    sisterSN = input(
        "输入妹妹的序列号, 如: 001, 注意: 001与1是不同的, 因为sisterSN是str类型的.\n注意:sisterSN需要有唯一性.\nsisterSN = ")
    sisterName = input("输入妹妹的名字, 其为str类型的, 可以为空.\nsisterName = ")
    sisterCmdInPort = str(int(input(
        "输入妹妹的指令传入端口, 其为int类型的.\n注意: 您应保证此端口可被使用, 此向导并不检查端口的可用性!\nsisterCmdInPort = ")))
    sisterFileSharePort = str(int(input(
        "输入妹妹的文件共享(HTTP服务器)端口, 其为int类型的.\n注意: 您应保证此端口可被使用, 此向导并不检查端口的可用性!\nsisterFileSharePort = ")))
    finalSisterConfContent = ["sisterSN = \"" + sisterSN + "\"",
                              "sisterName = \"" + sisterName + "\"",
                              "sisterCmdInPort = " + sisterCmdInPort,
                              "sisterFileSharePort = " + sisterFileSharePort]
    ufio.write_lines("conf", "sister.py", 1, finalSisterConfContent, 2)

    temp = input(
        Fore.GREEN + "配置已完成.\n"+Style.RESET_ALL+"要审阅配置文件, 输入Y/y(在每个文件审阅结束后请按q退出).\n>>> ")
    if temp == "Y" or temp == "y":
        for i in CONF_FILES:
            input("按下回车来审阅"+ufio.path_proc("conf/"+i, False)+"...")
            cpsc.more("conf", i)
            print("已审阅conf/"+i)

    print(Fore.GREEN + "此向导已经接近尾声了, 对了, 正式运行前请您仔细检查相关配置文件是否合乎心意.")
    print("创建就绪锁文件lock/ready.lck")
    cpsc.mkfile("lock", "ready.lck")
    print(Fore.GREEN + "首次运行向导已结束,您可以运行start.py来启动此妹妹(节点)了.")
    input("按下Enter继续...")
else:
    print(Fore.GREEN + "操作已取消, 没有应用任何修改.")
    input("按下Enter继续...")
