"""
故事演变：
徒弟掌握了师父和培训的技术后，自己钻研出了自己的独门配方
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


# 徒弟类 - 继承师傅类
class Prentice(Master, School):
    """注意：当一个类有多个父类的时候，默认使用第一个父类的同名属性和方法"""
    def __init__(self):
        self.kongfu = '独创煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子 -- 自己')


tudi = Prentice()
tudi.make_cake()
"""拓展属性"""
print(tudi.__doc__)  # 类的文档 --- 类名下首行三引号注释的内容
print(tudi.__dict__)  # 实例的属性，值的键值对
print(Prentice.__mro__)  # 获取当前类所继承的父类集合，按照继承先后排序
