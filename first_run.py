'''
The Project-RealMisakaNetwork
Version: alpha-1
License: AGPL
File Description:
初次运行向导。
'''
import os
import random
import time
import hashlib

#密码靠以下四个生成，均可随意改动。
set_a = ['a','b','c','d','e','f','g','q','w','r','e','o','s']
set_b = ['#','%','&','+','*','/','l','t','m','z','.','h','i']
set_c = ['0','1','2','3','4','5','6','7','8','9','=','{','}']
set_d = ['i','really','love','misaka','mikoto','!','---byfs']

def new_conf():
    ready_info = "RealMisakaNetwork Ready Lock, DONOT Delete! VER=ALPHA-1"
    print('[I]将会生成配置文件夹及内部文件。御坂御坂如此说到。')
    os.mkdir('conf')
    os.mknod('conf/port')
    port = open('conf/port','w')
    port.write('666')
    port.close()
    os.mknod('conf/passwd')
    os.mknod('conf/allow_host')
    os.mknod('conf/this')
    print('[I]将会生成临时文件夹。御坂御坂如此说到。')
    os.mkdir('temp')
    print('[I]以下是文件说明。御坂御坂如此说到。')
    print('[I]port决定端口，默认为666。')
    print('[I]')
    print('[I]this三行，内有这个妹妹的信息，行1：编号，行2：名字，行3：身份SHA256号（不要更改它）。')
    num = input('编号>')
    name = input('名字>')
    random.seed(time.time())
    sha256 = hashlib.sha256() #当然，可以改为MD5/SHA512等HASHLIB支持的算法。下面代码凑字数～～～
    tmp = (
    str(random.random())+str(random.random())+
    str(random.random())+str(random.random())+
    str(random.random())+str(random.random())+
    str(random.random())+str(random.random())+
    str(random.random())+str(random.random())+
    str(random.random())+str(random.random())+
    str(random.random())+str(random.random())+
    str(random.random())+str(random.random())
    )
    sha256.update(tmp.encode())
    ident = sha256.hexdigest()
    this = open('conf/this','w')
    this.writelines([num+'\n',name+'\n',ident+'\n'])
    this.close()
    print('[I]passwd文件可以用一个简单的密码防止未授权连接（目前并不可靠，明文传输）。')
    passwd = 'pc' #密码生成部分可以更改。
    for i in range(2):
        random.seed(time.time())
        passwd = passwd + random.choice(set_a) + random.choice(set_b)
        random.seed(time.time())
        passwd = passwd + random.choice(set_c) + random.choice(set_d)
    pwd = open('conf/passwd','w')
    pwd.write(passwd)
    pwd.close()
    print('[I]密码被设定为[',passwd,']')
    print('[I]allow_host中存放允许建立连接的主机的IP。注意：在存在allow_all.lck时，只要passwd正确即可连接。')
    print('[I]以上文件均位于“conf”文件夹中。')
    print('[I]将会属于这个妹妹的连接文件：',num+'.link','，可以把它复制到各个属于这个网络的妹妹的link文件夹内，方便连接。')
    os.mknod(num+'.link')
    #CODE HERE!#
    os.mknod('ready.lck')
    ready = open('ready.lck','w')
    ready.write(ready_info)
    ready.close()
    print('恭喜你，看似成功完成了！御坂御坂欢快的说到。')

def already_ready():
    print('已有ready,lck！不允许再次运行此向导！御坂御坂如此说到。')
    exit('ERR::EXISTS::READY_LCK')
print('[I]欢迎来到初次运行向导！御坂御坂如此表示欢迎。')

if (os.path.isfile('ready.lck') == False):
    new_conf()
else:
    already_ready()