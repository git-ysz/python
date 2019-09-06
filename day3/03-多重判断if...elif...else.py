"""
语法：
if 条件1:
    条件1成立执行的代码
elif 条件2:
    条件2成立执行的代码
elif 条件3:
    条件3成立执行的代码
...........
else:
    以上条件都不成立执行的代码
"""

age = int(input('请输入您的年龄：'))
print(f'您的年龄是{age}，', end='')
if age < 18:
    print('童工')
# elif可以简写为elif age <= 60:
elif (age >= 18) and (age <= 60):
    print('合法工作年龄')
else:
    print('退休年龄')
