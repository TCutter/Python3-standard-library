# Python3-standard-library

* [1. 核心模块](#1)
    * [1.1 介绍](#1.1)
    * [1.2 builtins 模块](#1.2)
    * [1.3 exceptions 模块](#1.3)
    * [1.4 os 模块](#1.4)

参考：

* [python2](https://blog.csdn.net/liujinwei2005/article/details/76725422#t1)
* [python3](https://blog.csdn.net/manimanihome/article/details/53043431)


# <span id = '1'>1. 核心模块</span>
## <span id = '1.1'>1.1 介绍</span>
本章描述了一些基本的标准库模块. 任何大型 Python 程序都有可能直接或间接地使用到这类模块的大部分.

### 1.1.1 内建函数和异常
定义内建函数（如 len、int、range...）的  *_ _ builtin _ _* （Python3中叫 *builtins*）模块;以及定义所有内建异常的 *exceptions* 模块。

Python 在启动时导入这两个模块, 使任何程序都能够使用它们.

### 1.1.2 操作系统接口模块
Python 有许多使用了 POSIX 标准 API 和标准 C 语言库的模块. 它们为底层操作系统提供了平台独立的接口.

比如：

* 提供文件和进程处理功能的 *os* 模块；
* 提供平台独立的文件名处理(分拆目录名, 文件名, 后缀等)的 *os.path* 模块;
* 以及时间日期处理相关的 *time/datetime* 模块

### 1.1.3. 类型支持模块
标准库里有许多用于支持内建类型操作的库. *string* 模块实现了常用的字符串处理. *math* 模块提供了数学计算操作和常量(pi, e都属于这类常量), *cmath* 模块为复数提供了和 *math* 一样的功能.

### 1.1.4. 正则表达式
*re* 模块为 Python 提供了正则表达式支持. 正则表达式是用于匹配字符串或特定子字符串的有特定语法的字符串模式.

### 1.1.5. 语言支持模块
sys 模块可以让你访问解释器相关参数,比如模块搜索路径,解释器版本号等. operator 模块提供了和内建操作符作用相同的函数.copy 模块允许你复制对象, Python 2.0 新加入的 gc 模块提供了对垃圾收集的相关控制功能.

## <span id = '1.2'>1.2 builtins 模块</span>

这个模块包含 Python 中使用的内建函数，一般情况下不用手动导入。

这个模块一般情况下不用显示引用，只有当自定义的函数或者变量与内建函数或变量重名，而且仍然需要该内建类型时需要显示指明。

<font color=#0099ff size=3 >Example1 : myPrint.py</font>
```
import builtins # 此时需要手动导入

def print(message):
    new_mes = message.center(len(message)+10,'*')
    builtins.print(new_mes)
```
## <span id = '1.3'>1.3 exceptions 模块</span>
不需要手动导入

基础类（BaseException）：Exception，ArithmeticError，BufferError，LookupError

自定义的异常类必须继承自BaseException(或者它的任意一个合适的子类），而且只有继承自BaseException的对象才可以被抛出

<font color=#0099ff size=3 >Example2 : 自定义异常</font>
```
class HTTPError(Exception):
    def __init__(self, url,errcode,errmessage):
        error = "<HTTPError for {0} ：{1}  {2}>".format(url,errcode,errmessage)
        Exception.__init__(self,error)

try:
    err = HTTPError('www.baidu.com','404','Not Found!')
    raise(err)
except HTTPError as ex:
    print(ex)     
```

输出：
```
<HTTPError for www.baidu.com ：404  Not Found!>
```

## <span id = '1.4'>1.4 os 模块</span>
### 1.4.1. 处理文件
内建的 *open* 和 *file*(Python3已弃用) 函数提供创建、打开、编辑功能，而 *os* 模块提供了重命名和删除文件所需的函数.

<font color=#0099ff size=3 >Example3 : 使用 *os* 模块重命名和删除文件</font>
```
import os
import myPrint

def rename(file, new_name):
    if os.path.exists(file):
        filename = os.path.splitext(file)
        new_file = new_name + filename[1]
        os.rename(file,new_file)
    else:
        myPrint.print('rename : 文件不存在！')
  
# 删除文件
def remove(file):
    if os.path.exists(file):
        os.remove(file)
    else:
        myPrint.print('remove : 文件不存在！')

remove('sample.tmp')
rename('sample.txt','index')
```

### 1.4.2 处理目录

<font color=#0099ff size=3 >Example4 : 使用 *os.listdir()* 函数列出给定目录下的所有目录和文件名</font>
```
import os
from myPrint import print

for name in os.listdir():   # 参数为空时默认使用当前目录
    print(name)
```
