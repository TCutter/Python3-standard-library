# Python3-standard-library

* [1. 核心模块](#1)
    * [1.1 介绍](#1.1)
    * [1.2 builtins 模块](#1.2)
    * [1.3 exceptions 模块](#1.3)
    * [1.4 os 模块](#1.4)
    * [1.5 os.path 模块](#1.5)
    * [1.6 re 模块](#1.6)

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

<font color=#0099ff size=3 >Example 1-1 : myPrint.py</font>
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

<font color=#0099ff size=3 >Example 1-2 : 自定义异常</font>
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

<font color=#0099ff size=3 >Example 1-3 : 使用 *os* 模块重命名和删除文件</font>
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
目录结构如下：

![文件结构](/images/file_hierachy.PNG)

<font color=#0099ff size=3 >Example 1-4 : 使用 *os.listdir()* 函数列出给定目录下的所有目录和文件名</font>
```
import os
from myPrint import print

for name in os.listdir():   # 参数为空时默认使用当前目录
    print(name)
```

输出：
```
*****.git*****
*****.vscode*****
*****images*****
*****index.py*****
*****myPrint.py*****
*****README.md*****
*****test*****
*****__pycache__*****
```

<font color=#0099ff size=3 >Example 1-5 : 使用 *os.getcwd()* 和 *os.chdir()* 分别获取和改变当前工作目录</font>
```
import os

path = os.getcwd()
print('1',path)

# go down 
os.chdir('test')
path = os.getcwd()
print('2',path)

# go back
os.chdir(os.pardir) # 获取当前工作目录的上层目录
path = os.getcwd()
print('3',path)
```

输出：
```
1 C:\Users\xiao.guo\Desktop\Demo\GitHub\Python3-standard-library
2 C:\Users\xiao.guo\Desktop\Demo\GitHub\Python3-standard-library\test
3 C:\Users\xiao.guo\Desktop\Demo\GitHub\Python3-standard-library
```


<font color=#0099ff size=3 >Example 1-6 : 使用 *os.mkdir()* 和 *os.rmdir()* 分别创建和删除 *单* 个目录级 </font>
```
import os

if os.path.exists('test2'):
    os.rmdir('test2')   # 只能删除空目录，若要删除非空目录，则使用shutil.rmtree
else:
    os.mkdir('test2')
```

<font color=#0099ff size=3 >Example 1-7 : 使用 *os.makedirs()* 和 *os.removedirs()* 分别创建和删除 *多* 个目录级 </font>
```
import os

if os.path.exists('test2'):
    os.removedirs('test2/test3')   # 同样只能删除空目录。从‘test3’目录开始删除，然后往父级目录查找，直达父级目录不为空时停止
else:
    os.makedirs('test2/test3')
```

### 1.4.3 处理文件属性

<font color=#0099ff size=3 >Example 1-8 : 使用 *os.stat()*  获取文件属性</font>

函数的返回值如下：
![stat](/images/return_stat.PNG)

As of Python 3.3, *os.fstat(fp)* is equivalent to *os.stat(path)*

```
import os
import time

filename = 'images/return_stat.PNG'

def dump(func,filename):
    path = "{!s}({!r})".format(func,filename)
    print("path = ",path)

    st = eval(path)
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
    print("{0}: {1}".format(func,filename))

    print("- size: {} bytes".format(size))
    print("- owner: {0} {1}".format(uid,gid))
    print("- created: ",time.ctime(ctime))
    print("- last accessed: ",time.ctime(atime))
    print("- last modified: ",time.ctime(mtime))
    print("- mode:", oct(mode)) # 转成8进制
    print("- inode/dev: {0}/{1}\n".format(ino,dev))

dump('os.stat',filename)

with open(filename,'rb') as fp:
    dump('os.fstat',fp.fileno())
    
```

输出：
```
path =  os.stat('images/return_stat.PNG')
os.stat: images/return_stat.PNG
- size: 27822 bytes
- owner: 0 0
- created:  Sun Apr  8 16:38:01 2018
- last accessed:  Sun Apr  8 16:38:01 2018
- last modified:  Sun Apr  8 16:38:01 2018
- mode: 0o100666
- inode/dev: 94012642221422957/2359390063

path =  os.fstat(3)
os.fstat: 3
- size: 27822 bytes
- owner: 0 0
- created:  Sun Apr  8 16:38:01 2018
- last accessed:  Sun Apr  8 16:38:01 2018
- last modified:  Sun Apr  8 16:38:01 2018
- mode: 0o100666
- inode/dev: 94012642221422957/2359390063
```

<font color=#0099ff size=3 >Example 1-9 : 使用 os 模块修改文件的权限和时间戳</font>
```
import os
import stat, time

infile = "images/in.png"

st_original = os.stat(infile)
print("original", "=>")
print("mode", oct(stat.S_IMODE(st_original[stat.ST_MODE])))
print("stat mode",st_original[stat.ST_MODE])
print ("atime", time.ctime(st_original[stat.ST_ATIME]))
print ("mtime", time.ctime(st_original[stat.ST_MTIME]))
print()
# copy mode and timestamp
os.chmod(infile, stat.S_IMODE(st_original[stat.ST_MODE]))
os.utime(infile, (time.time(),time.time()))

st_copy= os.stat(infile)
print ("copy", "=>")
print("mode", oct(stat.S_IMODE(st_copy[stat.ST_MODE])))
print("stat mode",st_copy[stat.ST_MODE])
print ("atime", time.ctime(st_copy[stat.ST_ATIME]))
print ("mtime", time.ctime(st_copy[stat.ST_MTIME]))
```

输出：
```
original =>
mode 0o666
stat mode 33206
atime Mon Apr  9 14:55:46 2018
mtime Mon Apr  9 14:55:46 2018

copy =>
mode 0o666
stat mode 33206
atime Mon Apr  9 14:57:25 2018
mtime Mon Apr  9 14:57:25 2018
```

### 1.4.4 处理进程 --- 各种操作系统接口

以后都会用 *subprocess* 模块代替

<font color=#0099ff size=3 >Example 1-10: 使用 os.system(command)执行操作系统命令</font>
```
# system() 函数在当前进程下执行一个新命令, 并等待它完成
import os

print("name :",os.name)
if os.name == "nt":
    command = "dir"
else:
    command = "ls -l"

os.system(command)
```

<font color=#0099ff size=3 >Example 1-11: 使用 os.exec* 函数使用新进程替换当前进程(或者说是"转到进程").</font>
```
import os

program = 'python'
arg = 'myPrint.py'

os.execvp(program,(program,arg)) # one of exec*
print('456')    # 不会被执行
```

<font color=#0099ff size=3 >Example 1-12: 使用 os.spawnv()调用其他程序 (Windows和Unix通用)</font>

```
# Windows下无 os.fork()

import os

if os.name in ("nt", "dos"):
    exefile = ".exe"
else:
    exefile = ""

def spawn(program, *args):
    try:
        # possible 2.0 shortcut!
        return os.spawnvp(program, (program,) + args)
    except AttributeError as e:
        print("AttributeError :",e)
    try:
        spawnv = os.spawnv
    except AttributeError:

        # assume it's unix
        pid = os.fork()
        if not pid:
            os.execvp(program, (program,) + args)
        return os.wait()[0]
    else:
        # got spawnv but no spawnp: go look for an executable
        for path in str.split(os.environ["PATH"], os.pathsep):
            file = os.path.join(path, program) + exefile
            try:
                return spawnv(os.P_WAIT, file, (file,) + args)
            except os.error as e:
                print("os.error :",e)
        raise IOError("cannot find executable")

#
# try it out!

spawn("python", "myPrint.py")

print("goodbye")
```

输出：
```
AttributeError : module 'os' has no attribute 'spawnvp'
os.error : [Errno 2] No such file or directory
*****123*****
goodbye
```

## <span id = '1.5'>1.5 os.path 模块</span>
### 1.5.1 处理文件名

*os.path* 模块包含了许多与平台无关的处理长文件名的函数. 也就是说, 你不需要处理前后斜杠, 冒号等.

<font color=#0099ff size=3 >Example 1-13: 使用 *os.path* 模块处理文件名</font>
```
import os.path as path
import os

filename = r"\images\in.png"

split = path.split(filename)    #返回tuple
splitext = path.splitext(filename)  #返回tuple
dirname = path.dirname(filename)
basename = path.basename(filename)

print("split =>",split)
print("splitext =>",splitext)
print("dirname =>",dirname)
print("basename =>",basename)
print("join =>",path.join(dirname,basename))    # windows中使用 \，Linux中使用 /

print(path.exists(os.getcwd() + path.join(dirname,basename)))
```

输出：
```
split => ('\\images', 'in.png')
splitext => ('\\images\\in', '.png')
dirname => \images
basename => in.png
join => \images\in.png
True
```

<font color=#0099ff size=3 >Example 1-14: 使用 *os.path* 模块检查文件名的特征</font>
```
import os

FILES = (
    os.curdir,
    "/",
    "file",
    "/file",
    "images",
    "images/in.png",
    "../images/in.png",
    "/images/in.png"
    )

for file in FILES:
    print(file, "=>",end = '  ')
    if os.path.exists(file):
        print("EXISTS",end = '  ')
    if os.path.isabs(file):
        print("ISABS",end = '   ')  # 是否为绝对路径
    if os.path.isdir(file):
        print("ISDIR",end = '   ')
    if os.path.isfile(file):
        print("ISFILE",end = '  ')
    if os.path.islink(file):
        print("ISLINK",end = '  ')
    print()
```

输出：
```
. =>  EXISTS  ISDIR
/ =>  EXISTS  ISABS   ISDIR
file =>
/file =>  ISABS
images =>  EXISTS  ISDIR
images/in.png =>  EXISTS  ISFILE
../images/in.png =>
/images/in.png =>  ISABS
```

## <span id = '1.6'>1.6 re 模块</span>