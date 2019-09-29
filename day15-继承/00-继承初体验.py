"""
python 面向对象的继承指的是多个类之间的所属关系，即子类默认继承父类的所有属性和方法
具体如下：
"""


# 父类
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)


# 子类
class B(A):
    pass


res = B()
# 子类调用父类的info_print方法
res.info_print()  # 1
