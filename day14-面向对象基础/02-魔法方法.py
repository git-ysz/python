"""
在python中，__xx__()的函数叫做魔法方法，指的是具有特殊功能的函数
1、__init__(self[, *args]) ==> 初始化对象,在创建对象时，默认被调用
2、__str__(self[, *args])
    当使用print输出对象的时候，默认打印对象的内存地址。
    如果定义了该方法，那么就会打印从这个方法中return的数据
......

"""


# 定义类
class Washer():
    # self --- 实例
    # 初始化类的属性
    def __init__(self, name='洗衣机'):
        self.name = name

    def __str__(self):
        return '这是洗衣机的类'

    def wash(self):
        print('洗衣服', f'该产品是{self.name}')
        return self


haier = Washer('海尔')
print(haier)
print(haier.name)
haier.wash()
