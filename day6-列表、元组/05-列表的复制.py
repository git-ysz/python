list1 = ['Tom', 'Lily', 'Rose']
list2 = list1.copy()
list1[0] = ''  # 原始数据做修改的时候，使用copy函数复制的list2不会更改
print(list1, list2)
