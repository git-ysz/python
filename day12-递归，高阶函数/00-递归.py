"""
递归特点
1、函数自调用
2、必须有出口
"""


# 应用：3以内数字累加和 3 + 2 + 1

def sum_numbers(n):
    if n == 1:
        # 必须存在出口，否则报错
        return 1
    return n + sum_numbers(n - 1)


print(sum_numbers(3))
