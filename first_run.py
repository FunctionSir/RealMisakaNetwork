'''
The RealMisakaNetwork Project
许可证：AGPL-3.0
文  件：first_run.py
说  明：首次运行向导。
编  码：UTF-8
'''
#!/usr/bin/python3
#coding=utf-8
import os
print('MisakaNetwork 首次运行向导')
print('版本：1.0.0, MisakaMikoto')
print('是RealMisakaNetwork Project的一部分，使用AGPL-3.0协议')
print('这个向导将会引领你完成第一次运行所需要的设置。御坂御坂如此回报到。')
print('这台设备将成为0号（FileIndex），1号（FileSHA256），2～20000（Common），还是20001（Root）？御坂如此问道。')
print('#0=I,#1=S,#2~20000=C,#20001=R，御坂御坂如此补充道。')
inp = input('MISAKA#20001>')
t = inp #t：Type。
if (t == 'I'):
    print('您把这台设备的类型设置为了FileIndex，我会带你到另一个.py文件进行设置。')
    os.system('python sister_index/config.py')
