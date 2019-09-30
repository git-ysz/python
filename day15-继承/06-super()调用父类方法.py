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
class School(Master):
    def __init__(self):
        self.kongfu = '学校煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子 -- 学校')
        # 调用基(父)类的同名属性和方法
        super().__init__()
        super().make_cake()


# 徒弟类 - 继承师傅类 《第二种方法》
class Prentice(School):
    def __init__(self):
        self.kongfu = '独创煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子 -- 自创')

    def make_old_cake(self):
        # 调用基(父)类的同名属性和方法
        super().__init__()
        super().make_cake()


tudi = Prentice()
print(Prentice.__mro__)
# 注意：使用super可以自动查找父类。调用顺序遵循__mro__类属性的顺序。比较适合单继承使用
tudi.make_old_cake()
