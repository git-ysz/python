#!/usr/bin/env python3 
# 为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# -*- coding: utf-8 -*-
# 告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码

sum = 0
for x in range(101):
    sum = sum + x
print(sum) # 5050

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("hekko,%s" % name)