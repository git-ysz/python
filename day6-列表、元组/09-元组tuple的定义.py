# 多个数据的元组
t1 = (10, 20, 30)
# 单个数据的元组
t2 = (10,)
print(type(t1), type(t2))  # tuple

# 单个数据如果不加逗号","会影响数据本身的类型
t3 = (1)
t4 = ('aaa')
t5 = (['aaa', 'bbb', 'ccc'])
print(type(t3), type(t4), type(t5))  # int,str,list
