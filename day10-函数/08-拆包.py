# 元组拆包
def return_num():
    return 100, 200


num1, num2 = return_num()
print(num1, num2)


# 字典拆包
def return_dict():
    return {
        'name': 'Tom',
        'age': 25
    }


a, b = return_dict().items()
print(a, b)
