"""
作用：用来移动文件指针
语法：
文件对象.seek(偏移量，起始位置)
起始位置：0 -- 文件开头；1 -- 当前位置；2 -- 文件结尾
目标：
    1、r 模式改变文件指针位置：改变读取数据开始位置或把文件指针放置结尾（无法读取到数据）
    2、a 模式改变文件指针位置，做到可以读取出数据

"""

f1 = open('04-test.txt', 'r+', encoding='utf-8')
print(f1.read())
f1.seek(6, 0)  # 中文占3个字节
print(f1.read())
f1.close()

f2 = open('04-test.txt', 'a+', encoding='utf-8')
print(f2.read())  # 读取不到数据，因为目前指针在文件内容结尾
f2.seek(0, 0)  # 简写 ==> f2.seek(0) 指针放到开头位置，不偏移
print(f2.read())
f2.close()

