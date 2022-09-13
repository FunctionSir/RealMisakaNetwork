<!--
 * @Author: FunctionSir
 * @Date: 2022-01-01 14:57:51
 * @LastEditTime: 2022-09-02 17:57:51
 * @LastEditors: FunctionSir
 * @Description: README file
 * @FilePath: /RealMisakaNetwork/README.md
-->

# RealMisakaNetwork “御坂网络”的简单实现

***注意：持续施工中…***  
***尚未完成第一个版本，目前无法使用。***  

## 项目进度

目前还未实现v0.1-alpha的全部功能.  
但是, 您已经可以部署节点并使用netcat与现有节点交互了.  
目前可用命令较少.  

## 需要配置的内容

在您开始使用（启动start.py）前，请确保运行过firstRun.py，这是第一次运行向导。  
此向导将会为您准备好基本的东西.  
注意：本程序需求Python 3，至于Python 2, 现在及将来均不会支持.  
若您还在使用Python 2, 非常建议您切换到Python 3.  

## Commands

### 简要说明

RealMisakaNetwork的节点之间使用一组统一的命令来让各自的对方做出动作. 各节点的命令都是同一套. 就像是所有人身体所用的密码子都是同一套.  
有的命令有参数, 一定在紧跟命令的第二行.  
如果参数有多个, 那么需要用半角分号分隔.  
命令的执行往往伴随着相关信息的输出.  
详细的命令用法等, 可以参照下文, 以及sister.py的源代码, 在源码中, 命令的实现函数都是c_开头的. 如c_exit.  
default比较特殊, 它可以是命令, 专管占位或者是耗时间, 也可以是在输入非命令时的默认操作.

### 命令及用途

**!exit**: 退出  
**!sys**: 执行系统命令. 使用例:  

```rmncmd
!sys  
poweroff  
```

**!py**: 执行Python语句. 使用例:

```rmncmd
!py  
print("Hello, World!")  
```

**!r**: 读取一个文件到fileContentBuffer. 使用例:  

```rmncmd
!r
/etc; hosts; 0  
```

说明: 把/etc处的hosts读入fileContentBuffer, 不包括每行尾的换行符.  

**!default**: 除了把它自己移出cmdToDoList之外, 什么也不做.  
