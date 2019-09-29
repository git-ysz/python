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


# 徒弟类 - 继承师傅类 《第一种方法》
class Prentice(Master, School):
    """注意：当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法"""
    def __init__(self):
        self.kongfu = '独创煎饼果子配方'

    def make_cake(self):
        # 注意：如果先调用了父类的属性和方法，父类属性就会覆盖子类属性
        # 故在方法一中，在调用自己类的方法时需要初始化自身类的属性
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子 -- 自己')

    # 注意：调用父类方法，但是为保证调用到的也是父类的属性，必须在调用方法钱调用父类的初始化
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


tudi = Prentice()
tudi.make_cake()
tudi.make_master_cake()
tudi.make_school_cake()
tudi.make_cake()
