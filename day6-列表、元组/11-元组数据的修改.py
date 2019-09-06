"""
元组数据不支持修改，只支持查找
"""

t1 = ('aa', 'bb', 'cc', 'dd')
# 出错：'tuple' object does not support item assignment
# t1[0] = 'aaa'

# 特例 -- 元组内部的可更改数据类型不会因为元组的特性而不可变
t2 = ('aa', ['bb', 'cc', 'dd'])
t2[1][0] = 'bbb'  # 更改成功
print(t2)
