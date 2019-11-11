"""
如果一个模块文件中有__all__变量，当使用from xxx import * 导入时，只能导入这个列表内的元素

"""

from _test_module import *

test(1, 2)
testA(4, 2)
# testB(2, 2)  # NameError: name 'testB' is not defined
