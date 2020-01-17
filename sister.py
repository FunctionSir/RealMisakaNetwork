'''
The Project-RealMisakaNetwork
Version: alpha-1
License: AGPL
File Description:
Sister的。
'''
def read_conf():
    f = open('conf/port','r')
    port = int(f.read())
    f.close()
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

read_conf()