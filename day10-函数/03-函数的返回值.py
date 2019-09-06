def return_num():
    return 1
    return 2


result = return_num()
print(result)  # 只返回第一个return的值


def return_num2():
    return 1, 2  # return (1, 2)


result2 = return_num2()
print(result2, type(result2))
