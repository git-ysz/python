"""
再Python中文件和文件夹的操作需要借助os模块里面的相关功能，具体步骤如下
1、导入os模块
2、使用os模块相关功能
"""
import os

f = open('06-rename.txt', 'w')  # 为了测试，先创建一个文件
f.close()

# 1、rename(目标文件，新文件名):重命名
os.rename('06-rename.txt', '06-rename[new].txt')

# 2、remove(目标文件)
# os.remove('06-rename[new].txt')

# 3、os.mkdir(文件夹名字) -- 创建文件夹(当前存在则报错)
# 4、os.rmdir(文件夹名字) -- 删除文件夹

# 5、os.getcwd() -- 获取当前文件目录路径
# 6、os.chdir(目录) -- 改变默认目录
# 7、os.listdir(文件夹名字) -- 获取某个文件夹下所有文件，返回一个列表，默认当前文件所在文件夹
