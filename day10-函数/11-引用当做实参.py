def test1(a):
    print(a, id(a))

    a += a

    print(a, id(a))


b = 100
test1(b)  # int,不可变类型计算后储存的地址不同 -- 计算后开辟了两块空间去储存
print(b)  # 没有发生变化


def test2(list1):
    print(list1, id(list1))

    list1.append(100)

    print(list1, id(list1))


listA = [10, 20]
test2(listA)  # list,可变类型更改后储存地址没有发生变化 -- 只占用一个“地址”储存
print(listA)  # 可变数据类型原数据发生了变化
