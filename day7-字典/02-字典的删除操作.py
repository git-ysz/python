dict1 = {
    'name': 'Tom',
    'age': 20,
    'gender': '男'
}
print(dict1)
# 1. del 删除指定的键值对
del dict1['name']
# del dict1['names']  # 没有的键值对删除时会报错
print(dict1)

# 2. clear() 清空
dict1.clear()
print(dict1)  # {}
