'''
The RealMisakaNetWork Project
许可证：AGPL-3.0
文  件：misakanetwork.py
说  明：启动器。
编  码：UTF-8
'''
#!/usr/bin/python3
#coding=utf-8
import os
print('MisakaNetwork 启动器')
print('版本：1.0.0, MisakaMikoto')
print('本软件为自由软件，使用AGPL-3.0协议')
if (os.path.exists('fr.lck') == False):
    print('看似这是第一次运行呢！启动首次运行向导么（Y/N）？ 御坂御坂如此说到。')
    inp=input('MISAKA#20001>')
    if (inp == 'Y'):
        print('---------------------------------')
        os.system('python first_run.py')
    else:
        print('退出请输入任意内容然后ENTER。御坂御坂如此说道。')
        ex=input('MISAKA#20001>')
        exit('EXIT!御坂御坂如此说道。')
else:
    exit()
