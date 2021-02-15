'''
The Project-RealMisakaNetwork
Version: alpha-1
License: AGPL
File Description:
Sister的。
'''
import os
import shutil
import mfio
import minf
say = '御坂如此汇报道。'

allow_all = False
port = 666
allow = ['*']

def read_conf():
    global allow_all
    global port
    global allow
    port = int(mfio.fileread('conf/port'))
    print('端口设置为',port,say)
    passwd = mfio.fileread('conf/passwd')
    if (os.path.isfile('conf/allow_all.lck') == False):
        allow_all = False
        f = open('conf/allow_host','r')
        allow = set(f.readlines())
        f.close()
    else:
        print('[I]存在ALLOW_ALL的锁。允许所有。')
        allow_all = True
    print('你允许',allow,'连接。'+say)

read_conf()