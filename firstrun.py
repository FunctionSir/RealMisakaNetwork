'''
Author: FunctionSir
Date: 2022-01-01 17:48:44
LastEditTime: 2022-09-05 22:02:09
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
DIRS = ["conf", "data", "lock", "temp", "data/sisters.d"]
DIRS_USAGE = ["配置", "数据", "锁", "临时", "link文件"]
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
    print("请阅读有关mnl文件与sisters.d的说明.")
    print("每个mnl文件都存放了一个妹妹的信息, 这些信息对于网络来说是很重要的.")
    print("只有知道了这些信息, 妹妹之间才可以相互沟通, 不然, 她们找不到彼此!")
    print("这种文件一般是自动生成的, 当然手动写也不是不行.")
    print("每个妹妹在完成首次运行向导后, 均会自动生成一个, 并放在firstrun.py所在的文件夹中.")
    print("当然, 也会在这个妹妹的data/sisters.d中创建一个, 但是, 内容与上面说的那份不一样, 不要混用!")
    print("其他妹妹是无法用127.0.0.1或者::1连接到这个妹妹的!")
    print("其文件名是: $序列号.mnl. 请不要删除这个, 这样日后使用方便.")
    print("您需要将生成的这个文件放到需要连接到此妹妹的妹妹节点的data/sisters.d中")
    print("之后, A便可以知道B存在. 也就可以通过序列号连接她了.")
    '''
    MNL FILE VERSION 0.1-alpha FORMAT
    4 Lines:
    $VER
    $HOW_TO_LINK
    $CMDINPORT
    $FILE_SHARE_PORT
    Example:
    0.1-alpha
    192.168.1.10
    12233
    16699
    '''

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
        ufio.write_lines("conf", "python.py", 1,
                         ("python = "+str(temp)).split(), 2)

    temp = ""
    temp = input("要使用的用以运行netcat的命令\n>>> ")
    if temp == "#" or temp == "":
        temp = StaticRes.DEAFULT_NETCAT_CONF_FILE_CONTENT
        print("使用默认值, 要写入的内容是:", temp)
        ufio.write_lines("conf", "netcat.py", 1, temp, 2)
    else:
        ufio.write_lines("conf", "netcat.py", 1,
                         ("netcat = "+str(temp)).split(), 2)

    temp = ""
    temp = input("要使用的用以运行Miniserve的命令\n>>> ")
    if temp == "#" or temp == "":
        temp = StaticRes.DEAFULT_MINISERVE_CONF_FILE_CONTENT
        print("使用默认值, 要写入的内容是:", temp)
        ufio.write_lines("conf", "miniserve.py", 1, temp, 2)
    else:
        ufio.write_lines("conf", "miniserve.py", 1,
                         ("miniserve = "+str(temp)).split(), 2)

    print("GNU Wget设置将使用默认值(一般不需要更改).")
    temp = StaticRes.DEAFULT_WGET_CONF_FILE_CONTENT
    print("使用默认值, 要写入的内容是:", temp)
    ufio.write_lines("conf", "wget.py", 1, temp, 2)

    print("GNU cURL设置将使用默认值(一般不需要更改, 除非您不使用默认的Miniserve作为HTTP(S)服务器).")
    temp = StaticRes.DEAFULT_CURL_CONF_FILE_CONTENT
    print("使用默认值, 要写入的内容是:", temp)
    ufio.write_lines("conf", "curl.py", 1, temp, 2)

    print("接下来设置妹妹(节点).")
    tempSisterSN = input(
        "输入妹妹的序列号, 如: 001, 注意: 001与1是不同的, 因为sisterSN是str类型的.\n注意:sisterSN需要有唯一性且sisterSN内" + Fore.RED+Style.BRIGHT + "不得带有半角分号" + Style.RESET_ALL + ", 否则程序将剔除之!\nsisterSN = ")
    if tempSisterSN.count(";") == 0:
        sisterSN = tempSisterSN
    else:
        sisterSN = tempSisterSN.replace(";", "")
        print("在sisterSN中检测到半角分号, 已将其剔除. 若您不满意这个操作, 请自行更改配置文件, 但即使那样, 半角分号也不应存在于sisterSN中, 否则后患无穷.")
    sisterName = input("输入妹妹的名字, 其为str类型的, 可以为空.\nsisterName = ")
    sisterCmdInPort = str(int(input(
        "输入妹妹的指令传入端口, 其为int类型的.\n注意: 您应保证此端口可被使用, 此向导并不检查端口的可用性!\nsisterCmdInPort = ")))
    sisterFileSharePort = str(int(input(
        "输入妹妹的文件共享(HTTP(S)服务器)端口, 其为int类型的.\n注意: 您应保证此端口可被使用, 此向导并不检查端口的可用性!\nsisterFileSharePort = ")))
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

    sisterIPOrDN = input("请输入用于连接到此妹妹的IP/域名.\n>>> ")
    if len(sisterIPOrDN) == 0:
        print(Fore.RED+Style.BRIGHT+"您输入了空值, 请过后自行修改"+sisterSN+".mnl!")
        sisterIPOrDN = "!!!PLEASE CHANGE THIS LINE TO A CORRECT VALUE!!!"
    print("创建mnl文件...")
    print("创建data/sisters.d/"+sisterSN+".mnl")
    cpsc.mkfile("data/sisters.d", sisterSN+".mnl")
    ufio.write_lines("data/sisters.d", sisterSN+".mnl",
                     1, ["0.1-alpha", "localhost", sisterCmdInPort, sisterFileSharePort], 2)
    print("创建"+sisterSN+".mnl")
    cpsc.mkfile("", sisterSN+".mnl")
    ufio.write_lines("", sisterSN+".mnl",
                     1, [StaticRes.MNL_VER, sisterIPOrDN, sisterCmdInPort, sisterFileSharePort], 2)

    print(Fore.GREEN + "此向导已经接近尾声了, 对了, 正式运行前请您仔细检查相关配置文件是否合乎心意.")
    print("创建就绪锁文件lock/ready.lck")
    cpsc.mkfile("lock", "ready.lck")
    print(Fore.GREEN + "首次运行向导已结束,您可以运行start.py来启动此妹妹(节点)了.")
    input("按下Enter继续...")
else:
    print(Fore.GREEN + "操作已取消, 没有应用任何修改.")
    input("按下Enter继续...")
