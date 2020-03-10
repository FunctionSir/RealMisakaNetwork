'''
The Project-RealMisakaNetwork
Version: alpha-1
License: AGPL
File Description:
清理配置文件，link文件，temp等。
'''
import os
import shutil
print('CLEAN WARNING')
print('你将会丢失几乎一切配置文件等，小心操作！')
really = input('OK-DO-THAT=执行，其他=放弃 \n'+'TOUMA>')
if really == 'OK-DO-THAT':
    if os.path.isdir('conf'):
        shutil.rmtree('conf')
    if os.path.isdir('temp'):
        shutil.rmtree('temp')
    if os.path.isdir('__pycache__'):
        shutil.rmtree('__pycache__')
    files = os.listdir()
    for i in files:
        if i[-5:] == '.link' or i[-4:] == '.lck':
            os.remove(i)
    print('[I]操作完成。')
else:
    print('[I]请放心，没有东西被操作。')
