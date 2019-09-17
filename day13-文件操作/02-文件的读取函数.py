
# 1、文件对象.read(num)
"""
num表示要从文件中读取的数据的长度（字节），如果没有传入num,表示读取文件中所有的数据
"""
f1 = open('02-test.txt', 'r')
# print(f1.read())
print(f1.read(10))  # 文件内容如果换行，程序底层是需要\n才能完成换行，所以\n（换行）占一个字节
f1.close()

# 2、文件对象.readlines()
"""
按照行的方式去读取文件所有内容，返回列表，列表的每一项为内容的一行
"""
f2 = open('02-test.txt', 'r')
print(f2.readlines())  # 返回结果中换行的会有\n（换行）字符
f2.close()

# 3、文件对象.readline()
"""
一次性读取一行内容，多次调用，读取多行
"""
f3 = open('02-test.txt', 'r')
print(f3.readline() + '-end')
print(f3.readline() + '-end')
print(f3.readline() + '-end')
print(f3.readline() + '-end')  # 始终会读取，读不到内容则返回空字符
f3.close()
