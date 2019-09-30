"""
在Python中，可以为实例属性和方法设置私有权限，即设置某个实例属性或实例方法不继承给子类
故事演变：
    师傅把技术传给自己的徒弟的同时，不想把自己的钱（2个亿）继承给他的徒弟
这个时候就要为 “钱” 这个实例属性设置私有权限

私有属性的方法：
在属性名和方法名前面加上两个下划线 "__属性、方法名"
"""


class Master(object):
    def __init__(self):
        self.kongfu = '古法配方'
        self.__money = '2个亿'

    def make_cake(self):
        print(f'{self.kongfu}-师傅')

    def __self_fn(self):
        print(f'{self.__money}--私有方法')

    def get_money(self):
        # 获取私有属性
        return self.__money

    def set_money(self, money):
        # 修改私有属性
        self.__money = money


class Prentice(Master):
    pass


tudi = Prentice()
tudi.make_cake()
print(tudi.kongfu)
print(tudi.__dict__)
print(tudi.__dir__())
# tudi.__self_fn()  # 报错
# print(tudi.__money)  # 报错
print(tudi.get_money())
tudi.set_money('500亿')
print(tudi.get_money())
tudi._Master__money = '800亿'  # 不建议这种方式修改
print(tudi.get_money())
