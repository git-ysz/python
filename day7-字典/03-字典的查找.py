dict1 = {
    'name': 'Tom',
    'age': 20,
    'gender': '男'
}

# 查找1. -- 字典序列[key]
print(dict1['name'])
# print(dict1['names'])  # 不存在的kye会报错

# 查找2. -- 字典序列.get(key, 默认值)
print(dict1.get('name'))
print(dict1.get('name', 'Yao'))  # name有值，所以不会取默认值
print(dict1.get('name_a', 'Yao'))  # name_a没有值，所以取默认值
print(dict1.get('names_b'))  # names_b没有值，没有默认值，取None

# 查找3. -- 字典序列keys() -- 获取的是可迭代的对象（所以键的集合）
# dict_keys(['name', 'age', 'gender'])
print(dict1.keys())
print(type(dict1.keys()))

# 查找4. -- values() -- 获取的是可迭代的对象（所有值的集合）
# dict_values(['Tom', 20, '男'])
print(dict1.values())
print(type(dict1.values()))

# 查找5. -- items() -- 获取的是可迭代的对象（所有键值对的集合）
# dict_items([('name', 'Tom'), ('age', 20), ('gender', '男')])
print(dict1.items())
print(type(dict1.items()))
