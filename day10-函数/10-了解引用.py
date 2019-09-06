# 1、整形 int -- 不可变类型
a = 1
b = a
print(a, b)
print(id(a), id(b), id(a) == id(b))

a = 2
print(b)  # b ==> 1，说明int为不可变类型
print(id(a), id(b), id(a) == id(b))


# 2、列表 list -- 不可变类型
list1 = [10, 20]
list2 = list1
print(list1, list2)
print(id(list1), id(list2), id(list1) == id(list2))

list1.append(30)
print(list2)  # b ==> [10, 20, 30]，list为可变类型
print(id(list1), id(list2), id(list1) == id(list2))
