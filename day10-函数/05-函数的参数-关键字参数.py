# 2、关键字参数 键=值 的方式传参
# **kw 代表多余的传入的参数，类型为字典


def user_info(name, age, gender, **kw):
    print(f'您的姓名是{name}，年龄为{age}，性别为{gender}')
    print(kw)


dict1 = {
    'age': 21,
    'name': 'Yao',
    'gender': '男'
}
list1 = ['小明', 25, '男']
user_info('Tom', age=18, gender='男')
user_info('Rose', gender='女', age=20)
user_info(**dict1)
user_info(*list1)

# 注意：位置参数必须在关键字参数前面
