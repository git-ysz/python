name_list = ['Tom', 'Lily', 'Rose']

# 1、.append(数据) -- 追加到后面
name_list.append('Yao')
print(name_list)

# 2、.extend(序列) -- 追加到后面
name_list.extend(['Song', 'XiaoMing'])
print(name_list)
name_list.extend('sanmao')
print(name_list)

# .insert(下标,数据) --- 添加数据到下标的位置
name_list.insert(1, 'daxiong')
print(name_list)
