"""
类：指对一系列具有相同特征和行为的事物的统称，是一个抽象的概念，不是真实存在的事物
· 特征既是属性
· 行为既是方法
定义类：
Python2中类分为：经典类和新式类
语法：
class 类名(要继承的类的类名)：
    code...
注意：类名要满足标识符命名规则，同时组训大驼峰命名习惯

对象：指用类创建出来的真是存在的事物
创建对象语法：
对象名 = 类名()

例如：类为洗衣机图纸，对象则可以说是根据图纸创建出来的洗衣机
"""


# 定义类
class Washer():
    # self --- 实例
    # 初始化类的属性
    def __init__(self):
        self.name = '洗衣机'

    def wash(self):
        print('洗衣服', self.name)
        return self


# 创建对象
haier = Washer()
haier.name = '海尔1'  # 为对象添加或修改属性
print(haier, haier.name)
print(haier.wash())  # 返回self的内存地址和实例的内存地址相同
