"""
if 条件:
    条件成立执行代码
    .....
else:
    if条件不成立执行的代码
    .....
"""
name = '小明'
age = int(input('请输入您的年龄：'))

if age >= 18:
    print(f'{name}已成年，可以上网')
else:
    print(f'{name}不成年，不能上网')
