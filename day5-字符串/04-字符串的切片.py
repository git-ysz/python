str1 = 'abcdefg'
print(str1)
# 拿到c,下拨得到的是下标为某个数字的数据
print(str1[2])
"""
语法
序列[开始下标:结束下标:步长]
1、下标可以为负数 -- -1代表倒数一个下标，-2代表倒数第二 ......
2、得到的数据包括开始下标的数据，不包括结束下标的数据
3、开始下标默认为0，结束下标默认为最后一个，步长默认为1
4、步长为-1时，顺序为倒序，即开始下标向左选取到结束下标
"""
# 拿到abc
print(str1[0:3])
print(str1[0:3:1])

# 拿到ac
print(str1[0:3:2])

# 倒序排列
print(str1[::-1])
print(str1[-3::-1])

num = '012345678'
print(num[8:5:-1])
