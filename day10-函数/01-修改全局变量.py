a = 100


def testA():
    print(a)


def testB():
    a = 200  # 这么赋值不会修改全局变量a
    print(a)


def testC():
    global a
    a = 200
    print(a)


testA()
testB()
testA()  # 全局变量a并没有发生改变 ==》 修改失败
testC()
testA()  # 全局变量a发生改变 ==》 修改成功

"""
总结：
如果想要在函数内部修改全局变量，需要用到global关键字
"""
