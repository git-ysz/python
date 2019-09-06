# 1、定义全局变量
glo_num = 0


def test1():
    global glo_num
    # 修改全局变量
    glo_num = 100


def test2():
    print(glo_num)


print(glo_num)
# 2、调用test1函数，修改全局变量
test1()
# 3、调用test2函数，打印全局变量
test2()
