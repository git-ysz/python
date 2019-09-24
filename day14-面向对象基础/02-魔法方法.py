"""
在python中，__xx__()的函数叫做魔法方法，指的是具有特殊功能的函数
1、__init__(self[, *args]) ==> 初始化对象,在创建对象时，默认被调用
2、__str__(self[, *args])
    当使用print输出对象的时候，默认打印对象的内存地址。
    如果定义了该方法，那么就会打印从这个方法中return的数据
......

"""


# 定义类
class Washer:
    # self --- 实例
    # __init__,初始化类的属性-实例被初始化的时候自动被调用
    def __init__(self, name='洗衣机'):
        self.name = name

    # __str__,实例被初始化的时候自动被调用 - 返回的是该实例对象的指向
    def __str__(self):
        return '这是洗衣机的类'

    # __del__,实例被删除/销毁的时候自动被调用，程序结束属于被销毁
    def __del__(self):
        print(f'{self}，被删除了')

    def wash(self):
        print('洗衣服', f'该产品是{self.name}')
        return self


haier = Washer('海尔')
print(haier)
print(haier.name)
haier.wash()
