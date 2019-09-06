def user_info(*args, **kwargs):
    print(args)  # 包裹位置参数 -- 不确定参数个数的写法 -- 返回元组
    print(kwargs)  # 包裹关键字参数 -- 不确定参数个数的写法 -- 返回字典


user_info('123', '245', test1=1, test2=2)

list1 = [1, 2, *[3, 4]]
dict1 = {'test1': 3, 'test2': 4}
user_info(*list1, **dict1)
