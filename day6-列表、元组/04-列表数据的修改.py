name_list = ['Tom', 'Lily', 'Rose']

# 1、修改指定下标的数据
name_list[0] = 'TOM'
print(name_list)

list1 = [4, 4, 1, 8, 10, 29, 3, 7]
# 逆序 reverse()
list1.reverse()
print(list1)

# 3、排序 sort(key=None, reverse=False) -- 默认升序
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
