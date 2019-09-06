name_list = ['Tom', 'Lily', 'Rose', 'Yao', 'Song', 'XiaoMing']

# 1、del 目标
# del name_list
# del(name_list)
# print(name_list)  # 'name_list' is not defined
del name_list[0]
print(name_list)

# 2、pop(下标:默认0) -- 删除指定下标的数据。返回值为被删除的数据
pop_data = name_list.pop(1)
print(pop_data)
print(name_list)

# 3、.remove(数据)
name_list.remove('Yao')
print(name_list)

# 4、.clear() -- 清空列表
name_list.clear()
print(name_list)
