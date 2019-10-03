"""
类属性：
    类属性就是类对象所拥有的属性，它被该类的所有实例对象所共有
    类属性可以使用类对象或实例对象访问
优点：
    记录某项数据始终保持一致时，则定义类属性
    实例属性要求每个对象为其单独开辟一份内存空间来记录数据，而类属性为全类所共有，仅占用一份内存，更加节省内存空间
修改类属性：
    只能通过类对象修改，不能通过实例对象修改，如果通过实例对象修改类属性，表示的是创建了一个同名实例属性，并不是类属性的修改

实例属性：
    描述事物的特征
"""


class Dog(object):
    tooth = 10  # 设置类属性


xiao_ming = Dog()
xiao_hong = Dog()
print(Dog.tooth)
print(xiao_hong.tooth)
print(xiao_ming.tooth)
Dog.tooth = 11  # 通过类对象修改类属性
print(xiao_hong.tooth)
print(xiao_ming.tooth)
xiao_hong.tooth = 20  # 通过实例对象修改类属性
print(xiao_hong.tooth)  # 20
print(xiao_ming.tooth)  # 11
