# 体验
dict1 = {i: i**2 for i in range(1, 6)}
print(dict1)

# 需求：合并以下列表为字典
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, '男']

dict2 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict2)

# 需求：提取字典中的目标数据 -->数量大于200
counts = {
    'MBP': 268,
    'HP': 125,
    'DELL': 201,
    'Lenovo': 199
}
count1 = {key: value for key, value in counts.items() if value > 200}
print(count1)
