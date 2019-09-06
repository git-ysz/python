# 1、位置参数 -- 传参个数和顺序必须一致
def user_info(name, age, gender):
    print(f'您的姓名是{name}，年龄为{age}，性别为{gender}')


user_info('Tom', 18, '男')
# user_info('Tom', 18)  # 报错

