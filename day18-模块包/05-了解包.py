"""
包将有联系的模块组织在一起，即放到同一个文件夹下，并且在这个文件夹创建一个名字为__init__.py文件，那么这个文件夹就称之为“包”。
制作包：
    new => python package => 输入包名 => ok => 新建功能模块（有联系的模块）
    注意：新建包后，包内部会自动创建__init__.py文件，这个文件控制着包的导入行为

体验包：
    1、新建包_my_package
    2、新建包内模块：my_module1 和 my_module2 并书写代码
    3、导入包：
        3.1、方法一：
            import 包名.模块名
        3.2、方法二：
            注意：必须要在__init__.py文件中添加__all__ = [] ，控制允许导入的模块列表
            from 包名 import *
"""

# 方法一
# import _my_package.my_module1
# import _my_package.my_module2 as module2
# _my_package.my_module1.info_print1()
# module2.info_print2()

# 方法二
from _my_package import *
my_module1.info_print1()
my_module2.info_print2()

