'''
The Project-RealMisakaNetwork
Version: alpha-1
License: AGPL
File Description:
Sister的。
'''
def fileread(which):
    f = open(which,'r')
    r = f.read()
    f.close()
    return r
def read_conf():
    say = '御坂如此汇报道。'
    port = int(fileread('conf/port'))
    print('端口设置为',port,say)
    passwd = fileread('conf/passwd')
    f.close()
    if (os.path.isfile('conf/allow_all.lck') == False):
        allow_all = False
        f = open('conf/allow_host','r')
        allow_host = set(f.readlines())
        f.close()
    else:
        allow_all = True
    f = open('conf/allow_host')
    allow = f.readlines()
    print('你允许',allow,'连接本妹妹。'+say)
read_conf()