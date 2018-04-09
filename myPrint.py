import builtins # 此时需要手动导入

def print(message):
    new_mes = message.center(len(message)+10,'*')
    builtins.print(new_mes)
