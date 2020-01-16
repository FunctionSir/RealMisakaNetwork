'''
The Project-RealMisakaNetwork
Version: alpha-1
License: AGPL
File Description:
初次运行向导。
'''
import os

def new_conf():
    print('[I]将会生成配置文件夹及内部文件。御坂御坂如此说到。')
    os.mkdir('conf')
    os.mknod('conf/port')
    port = open('conf/port','w')
    port.write('666')
    port.close()
    os.mknod('conf/passwd')
    os.mknod('conf/ban_order')
    os.mknod('conf/allow_host')
    print('[I]将会生成临时文件夹。御坂御坂如此说到。')
    os.mkdir('temp')
    print('[I]以下是文件说明。御坂御坂如此说到。')
    print('[I]port决定端口，默认为666。')
    print('[I]passwd文件可以用一个简单的密码防止未授权连接（目前并不可靠，明文传输）。')
    print('[I]ban_order中，凡是接收到的任务中含有里面的指令，将无条件拒绝接受。需要手工启用（通过创建ubo.lck在conf中）')
    print('[I]allow_host中存放允许建立连接的主机的IP。')
    print('[I]以上文件均位于“conf”文件夹中。')
    os.mknod('ready.lck')
    ready = open('ready.lck','w')
    ready.write("RealMisakaNetwork Ready Lock, DONOT Delete! VER=ALPHA-1")
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