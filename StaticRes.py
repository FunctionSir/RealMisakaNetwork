'''
Author: FunctionSir
Date: 2022-01-01 18:09:52
LastEditTime: 2022-09-05 22:01:09
LastEditors: FunctionSir
Description: 版本信息等静态资源
Note: 此文件仅充当资源库
FilePath: /RealMisakaNetwork/StaticRes.py
'''

'''
一些软件信息
'''
PROJECT_NAME = "RealMisakaNetwork"  # 项目名称
VER = "0.1"  # 版本
VER_CODENAME = "MisakaMikoto"  # 版本代号（在这个项目里, 会使用《某科学的超电磁炮（S/T）》中的人物来作为这个）
MNL_VER = "0.1-alpha"  # 指定使用的mnl版本

'''
ASCII艺术, 由toilet生成
'''
ASCII_MISAKA = "m    m   \"                  #            \n##  ## mmm     mmm    mmm   #   m   mmm  \n# ## #   #    #   \"  \"   #  # m\"   \"   # \n# \"\" #   #     \"\"\"m  m\"\"\"#  #\"#    m\"\"\"# \n#    # mm#mm  \"mmm\"  \"mm\"#  #  \"m  \"mm\"#"
ASCII_NETWORK = "mm   m          m                         #     \n#\"m  #  mmm   mm#mm m     m  mmm    m mm  #   m \n# #m # #\"  #    #   \"m m m\" #\" \"#   #\"  \" # m\"  \n#  # # #\"\"\"\"    #    #m#m#  #   #   #     #\"#   \n#   ## \"#mm\"    \"mm   # #   \"#m#\"   #     #  \"m"

'''
永不会出现的字符串
预留
'''
STR_NGA = "\n\n\n(・∀・)this String is NeVER Gonna to Appear(・∀・)\n木原家族的价格是114514镑114514便士\n辊斤拷烫烫烫屯屯屯\nTel: +114514-114514-114514\nosifhowerhffheiuhewr983ry238957y348567345isphdh9843yurhdksdfjoieja3493540454sjfoie\n(°Д°)(◕‿◕✿)☺\n\n\n"

'''
默认配置文件内容部分
'''
DEAFULT_PYTHON_CONF_FILE_CONTENT = ["python = \"python3\"\n"]
DEAFULT_NETCAT_CONF_FILE_CONTENT = ["netcat = \"nc\"\n"]
DEAFULT_WGET_CONF_FILE_CONTENT = ["wgetDownload = \"wget -c\"\n"]
DEAFULT_CURL_CONF_FILE_CONTENT = ["curlDownload = \"curl -C -O\"\n", "\'\'\'\n$URL$: miniserve生成的“\\”页面的URL, 末尾有反斜杠.\n$PATH$:将文件上传到的目录.\n\'\'\'\n",
                                  "curlUpload = \"curl -F path=@$FILE$ $URL$upload\\?path\\=$PATH$\" #对miniserve的上传可见此处参考的miniserve的READNE.md\n"]
DEAFULT_MINISERVE_CONF_FILE_CONTENT = ["miniserve = \"miniserve\"\n"]
