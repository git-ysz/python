#!/usr/bin/env python3 
# 为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# -*- coding: utf-8 -*-
# 告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码

# print("123123")

# print("helloword!!!\n", "啊啊啊啊", "eeeeeee\n", "dasdasdsa")

# print("1024 * 768 = ", 1024 * 768)

# print(r'''dasdas
#  ewqedad \\\n''', 3 > 2)


# name = input('please enter your name: ')
# print('hello', name)

# num = input('please enter number')
# num = int(num)
# if num > 0:
#     print(num)
# else:
#     print(-num)
# print(ord('A'), ord('哈'), chr(65), '\u4e2d\u6587')

# print('hello, %s' % 'world', 
# '''
# %%运算符用来格式化字符串
# %%s表示用%s替换
# %%f表示用%s替换
# %%d表示用%s替换
# %%x表示用%s替换''' % ('字符串', '浮点数', '整数', '十六进制整数'))

s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print('%.1f%%' % r)
print('%.2f%%' % r)
print('%.3f%%' % round(r, 2), round((0.2 + 0.1), 2))
print('hello,{0},成绩提升了{1:.2f}%'.format('小明', r))

print('%.2f-%02d' % (3.225, 1.3))
print('%.2f' % 3.1415926)

sum = 0
for x in range(101):
  sum = sum + x
print(sum) # 5050

L = ['Bart', 'Lisa', 'Adam']
for name in L:
  print("hekko,%s" % name)