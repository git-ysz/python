"""测试的模块"""


def test(a, b):
    print(a + b)


# 只在当前文件中调用该函数，其他导入的文件内不符合该条件，则不执行test函数的调用
if __name__ == '__main__':
    test(1, 1)
