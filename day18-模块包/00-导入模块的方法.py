"""
模块：
    Python模块（module），是一个python文件，以.py结尾，包含了python对象定义和python语句。
    模块能定义函数，类和变量，模块里面也能包含可执行的代码
"""

import math  # 导入指定模块
# from math import sqrt  # 导入指定模块内的指定功能
from math import *  # 导入指定模块内的所有功能

print(math.sqrt(9))  # 开平方 -- 3.0
print(sqrt(9))  # 开平方 -- 3.0 导入指定模块内的所有功能
print(pi, e)  # 3.141592653589793... 导入指定模块内的所有功能
