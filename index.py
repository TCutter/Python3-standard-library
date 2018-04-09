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