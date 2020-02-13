'''
The Project-RealMisakaNetwork
Version: alpha-1
License: AGPL
File Description:
Sister的。
'''
def read_conf():
    say = '御坂如此汇报道。'
    f = open('conf/port','r')
    port = int(f.read())
    f.close()
    print('端口设置为',port,say)
    f = open('conf/passwd','r')
    passwd = f.read()
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