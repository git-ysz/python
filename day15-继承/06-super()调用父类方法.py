"""
故事演变：
很多顾客都希望既能够吃到古法又能吃到学校技术的煎饼果子
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


# 徒弟类 - 继承师傅类 《第二种方法》
class Prentice(Master, School):
    def __init__(self):
        self.kongfu = '独创煎饼果子配方'


tudi = Prentice()
tudi.make_cake()
