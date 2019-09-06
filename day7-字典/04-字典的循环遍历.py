dict1 = {
    'name': 'Tom',
    'age': 20,
    'gender': '男'
}
# 遍历keys
for key in dict1.keys():
    print(key)
# 遍历values
for val in dict1.values():
    print(val)

# 遍历键值对
for item in dict1.items():
    print(item, item[0], item[1])
# 键值对拆包
for key, value in dict1.items():
    print(f'{key}:{value}')
