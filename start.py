'''
The Project-RealMisakaNetwork
Version: alpha-1
License: AGPL
File Description:
启动Python脚本，启动器。
'''
import os

def no_ready_lck():
    print('[E]糟糕！缺失就绪锁，您可能没有运行第一次运行向导，运行吗？御坂御坂如此问道。')
    print('[I]不运行请输入“-”，然后会退出，或输入任何字符然后继续。御坂御坂如此等待您的输入。')
    print('[I]Tip: 如果确定配置无误，你可以退出后手动创建ready.lck。')
    choice = input('TOUMA>')
    if (choice != '-' ):
        os.system('python first_run.py')
    else:
        print('肥肠抱歉，遇到严重错误：无法找到就绪锁。御坂御坂抱歉的说到。')
        exit('ERR::MISS::READY_LCK')

def rock_it():
    print('[I]看起来一切就绪，即将启动！御坂御坂如此回报到。')
    print('[I]Start [Sister]')
    os.system('python sister.py')

if (os.path.isfile('ready.lck') == False):
    no_ready_lck()
else:
    rock_it()
