name_list = ['Tom', 'Lily', 'Rose']

# 需求：注册邮箱，用户输入一个账户名，判断这个账户名是否存在，如果存在，提示用户，否则提示可以注册

"""
1、用户输入账号
2、判断if...else...
"""
name = input('请输入您的邮箱账号名：')
if name in name_list:
    print(f'您输入的名字为{name}，该用户名已经存在')
else:
    print('可以注册')
