'''
Author: FunctionSir
Date: 2022-01-01 18:09:52
LastEditTime: 2022-02-12 20:52:19
LastEditors: FunctionSir
Description: 版本信息等静态资源
FilePath: /RealMisakaNetwork/staticRes.py
Note: 此文件仅充当资源库
'''
'''
一些软件信息
'''
projectName = "RealMisakaNetwork"  # 项目名称
ver = "0.1"  # 版本
verCodename = "MisakaMikoto"  # 版本代号（在这个项目里，会使用《某科学的超电磁炮（S/T）》中的人物来作为这个）
'''
ASCII艺术，由toilet生成
'''
ASCIIMisaka = "m    m   \"                  #            \n##  ## mmm     mmm    mmm   #   m   mmm  \n# ## #   #    #   \"  \"   #  # m\"   \"   # \n# \"\" #   #     \"\"\"m  m\"\"\"#  #\"#    m\"\"\"# \n#    # mm#mm  \"mmm\"  \"mm\"#  #  \"m  \"mm\"#"
ASCIINetwork = "mm   m          m                         #     \n#\"m  #  mmm   mm#mm m     m  mmm    m mm  #   m \n# #m # #\"  #    #   \"m m m\" #\" \"#   #\"  \" # m\"  \n#  # # #\"\"\"\"    #    #m#m#  #   #   #     #\"#   \n#   ## \"#mm\"    \"mm   # #   \"#m#\"   #     #  \"m"
'''
永不会出现的字符串(用以str->单元素list时的参数)
不要让她很简单，不然可能会出现莫名其妙的BUG
'''
strNGA = "\n\n\n(・∀・)this String is Never Gonna to Appear(・∀・)\n木原家族的价格是114514镑114514便士\n辊斤拷烫烫烫屯屯屯\nTel: +114514-114514-114514\nosifhowerhffheiuhewr983ry238957y348567345isphdh9843yurhdksdfjoieja3493540454sjfoie\n(°Д°)(◕‿◕✿)☺\n\n\n"
'''
默认配置文件内容部分
'''
deafultPythonConfFileContent = ["python = \"python\" \n"]
deafultWgetlConfFileContent = ["wgetDownload = \"wget -c\" \n"]
deafultCurlConfFileContent = ["curlDownload = \"curl -C -O\" \n", "\'\'\'\n$URL$：miniserve生成的“\\”页面的URL，末尾有反斜杠。\n$PATH$:将文件上传到的目录。\n\'\'\'\n",
                              "curlUpload = \"curl -F \"path=@$FILE$\" $URL$upload\\?path\\=$PATH$\" #对miniserve的上传可见此处参考的miniserve的READNE.md\n"]
deafultMiniserveConfFileContent = []
