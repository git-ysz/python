
# 文件对象.read(num)
"""
num表示要从文件中读取的数据的长度（字节），如果没有传入num,表示读取文件中所有的数据
"""
f1 = open('02-test.txt')
print(f1.read())
f1.close()
