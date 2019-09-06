# 需求1、创建一个0-10的列表
i = 0
list1 = []

# while循环实现方法
while i < 10:
    list1.append(i)
    i += 1
print(list1)

# for 循环实现方法
list2 = []
for i in range(0, 10):
    list2.append(i)
print(list2)

# -------------------------------推导式实现方法
list3 = [i for i in range(0, 10)]
list4 = [i for i in range(0, 10) if i % 2 == 0]  # [i for i in range(0, 10, 2)]
list5 = [i if i != 2 else f'这是值:{i}的位置' for i in range(0, 10) if i % 2 == 0]
print(list3, list4, list5)

