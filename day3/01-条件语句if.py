"""
if 条件:
    条件成立执行代码
    .....
"""
if True:
    print('条件成立执行的代码1')
    print('条件成立执行的代码2')
if False:
    print('条件成立执行的代码3')
    print('条件成立执行的代码4')
# 注意：在下方没有加缩进的代码与if的成立与否无关
print('这个代码执行么？')

# 判断是否可以在网吧上网
name = '小明'
age = input('请问您的年龄为:')

print(type(age))

# 注意input接收到的是str类型，不能和int类型的18相比较
if int(age) >= 18:
    print(f'{name}已经成年，可以上网')
