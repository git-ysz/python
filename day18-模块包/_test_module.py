"""测试的模块"""

__all__ = [
    'test',
    'testA'
]


def test(a, b):
    print(f'test:{a + b}')


def testA(a, b):
    print(f'testA:{a - b}')


def testB(a, b):
    print(f'testB:{a * b}')


# 只在当前文件中调用该函数，其他导入的文件内不符合该条件，则不执行test函数的调用
if __name__ == '__main__':
    test(1, 1)
    testA(3, 1)
    testB(2, 2)
