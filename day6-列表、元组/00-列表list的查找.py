name_list = ['tom', 'lily', 'rose']

print(name_list[0])

# 1、index() 使用方法同字符串 -- 查询出现下标
print(name_list.index('lily'))
# print(name_list.index('lilys'))  # 报错

# 2、count() 使用方法同字符串 -- 查询出现次数
print(name_list.count('tom'))
print(name_list.count('toms'))

# 3、len() 获取列表长度 -- 公共方法
print(len(name_list))

# 4、in 判断某个数据存在于列表 -- 公共方法
print('tom' in name_list)
print('toms' in name_list)

# 5、not in 判断某个数据不存在于列表 -- 公共方法
print('tom' not in name_list)
print('toms' not in name_list)
