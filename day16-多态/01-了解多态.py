"""
多态：多态指的是一类事物有多种形态（一个抽象类有多个子类，因而多态的概念依赖于继承）
定义：多态是一种使用对象的方式，子类重写父类的方法，调用不同子类对象的相同方法，可以产生不同的执行结果
好处：调用灵活，有了多态，更容易编写出通用的代码，做出通用的编程，以适应需求的不断变化！
实现步骤：
    1、定义父类，并且提供公共方法
    2、定义子类，并且重写父类方法
    3、传递子类对象给调用者，可以见到不同子类执行效果的不同
体验：
需求：犬类
    1、警犬
    2、缉毒犬
    。。。
"""


class Dog(object):
    def work(self):
        print('旺旺~')


class ArmyDog(Dog):
    def work(self):
        print('警犬')


class DrugDog(Dog):
    def work(self):
        print('缉毒犬')


class Person(object):
    def work_with_dog(self, dog):  # 传入不同的对象，执行不同的代码，即不同的work函数
        dog.work()


ad = ArmyDog()
dd = DrugDog()

man = Person()
man.work_with_dog(ad)
man.work_with_dog(dd)
