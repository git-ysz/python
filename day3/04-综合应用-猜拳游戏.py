"""
需求：猜拳
参与者：1、玩家（手动出拳） 2、电脑（随机出拳）
判断输赢：
1、玩家获胜 2、平局 3、电脑获胜
"""

import random

# 1、玩家出拳
player = int(input('请出拳（0 => 石头；1 => 剪刀；2 => 布）：'))

# 2、电脑出拳 -- 暂时固定1
"""
随机数
1、导入模块
2、使用这个模块中的功能
"""
computer = random.randint(0, 2)
print(computer)

# 3、判断输赢
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print('玩家赢了')
elif player == computer:
    print('平局')
else:
    print('电脑赢了')
