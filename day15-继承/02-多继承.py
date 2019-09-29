"""
故事演变：
徒弟除了想学习师父的技术外还想学习其他的技术

即：多继承的意思就是一个类同时继承多个父类
"""


# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子 -- 师父')


# 学校类
class School(object):
    def __init__(self):
        self.kongfu = '学校煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子 -- 学校')

    def make_cake_for_school(self):
        print(f'运用{self.kongfu}制作煎饼果子 -- 学校')


# 徒弟类 - 继承师傅类
class Prentice(Master, School):
    """注意：当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法"""
    pass


# 徒弟实例化
tudi = Prentice()
print(tudi.kongfu)
tudi.make_cake()
tudi.make_cake_for_school()
