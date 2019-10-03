"""
类方法的特点：
    需要用装饰器@classmethod来标识其为类方法，对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数
类方法使用场景
    当方法中需要使用类对象（如访问私有类属性等）时，定义类方法
    类方法一般和类属性配合使用

静态方法：
    需要通过装饰器@staticmethod来进行修饰，静态方法既不需要使用传递类对象也不需要传递实例对象（形参没有self，cls）
    静态方法也能够通过实例对象和类对象去访问
静态方法的使用场景：
    当方法中既不需要使用实例对象（如实例对象，实例属性），也不需要使用类对象（如类属性，类方法，创建实例等）时，定义静态方法
    取消不需要的参数传递，有利于减少不必要的内存占用和性能消耗
"""


class Dog(object):
    __tooth = 10  # 定义私有类属性

    @classmethod
    def get_tooth(cls):
        return cls.__tooth

    @staticmethod
    def info_print():
        print('这是一个“狗”类，用于创建“狗”的实例对象...')


wang_cai = Dog()
print(Dog.__dict__)
print(wang_cai.get_tooth())
Dog.info_print()
wang_cai.info_print()
