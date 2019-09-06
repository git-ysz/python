"""
1、书写input
    input()
2、观察特点
    2.1、遇到input，等待用户输入
    2.2、接收input存变量
    2.3、input接收到的数据类型都是字符串
input()函数会把输入的内容全部按照字符串去处理
"""

name = input('请输入你的名字：')
password = input('请输入你的密码：')

print(f'您输入多的名字是{name}，您输入的密码是{password}')
print(type(name), type(password))
