"""
测试目标
1、访问模式对文件的影响
2、访问模式对write()的影响
3、访问模式是否可以省略，如果可以省略，默认情况是什么
"""

# r（只读）
# f1 = open('test1.txt', 'r')  # 该模式（只读）下，没有查找到该文件会报错
f1 = open('00-test.txt', 'r')
# f1.write('aa')  # 对只读模式调用write会报错
f1.close()

# w（只写）
f2 = open('00-test1.txt', 'w')  # 该模式（只写）下，没有查找到文件会新创建一个文件
f2.write('aaa')
f2.write('bbb')  # 该模式调用write写入会覆盖原有内容
f2.close()

# a（追加）
f3 = open('00-test2.txt', 'a')  # 该模式（追加）下，没有查找到文件会新创建一个文件
f3.write('abc')
f3.write('xyz')  # 该模式调用write写入会在原有内容的基础上追加内容
f3.close()

# 访问模式是否可以省略？？
# f4 = open('00-test3.txt')  # 省略访问模式下，没有查找到该文件会报错
f4 = open('00-test.txt')  # 省略访问模式下，默认的访问模式为r（只读）
f4.close()
