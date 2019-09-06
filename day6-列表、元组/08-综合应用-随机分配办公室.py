"""
需求：
1、有8位老师
2、有三个办公室
3、将八位老师随机分配到三个办公室
4、验证结果
"""
import random

# 1. 准备数据
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
offices = [[], [], []]

# 2.分配老师到办公室 -- 取每个老师放到offices中
for name in teachers:
    num = random.randint(0, 2)
    offices[num].append(name)
print(offices)

