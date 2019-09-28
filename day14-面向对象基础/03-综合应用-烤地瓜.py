"""
需求：
1、被烤的时间和对应的地瓜状态
    0-3分钟：生的，没熟
    3-5分钟：半生不熟
    5-8分钟：熟了
    超过8分钟：烤糊了
2、添加的调料
    用户可以按照自己的意愿添加调料

步骤分析：
1、定义类 -- 地瓜
    一、属性：
        被烤的时间
        地瓜的状态
        添加的调料
    二、方法：
        被烤
            1.用户根据意愿设定每次烤地瓜的时间
            2.判断地瓜被烤的总时间是在哪个区间，修改地瓜的状态
        添加调料
            1.用户根据意愿添加调料
            2.将用户添加的调料储存
    三、显示对象信息

"""


class SweetPotato:

    def __init__(self, time=0, state='生的', condiments=[]):  # 1、添加属性
        self.cook_time = time  # 烤的时间
        self.cook_state = state  # 地瓜的状态
        self.condiments = condiments  # 添加的调料

    def __str__(self):  # 3、显示对象信息
        return f'地瓜目前总共烤了{self.cook_time}分钟，现在的状态是：{self.cook_state}，调料有：{self.condiments}'

    def __del__(self):
        print(f'地瓜烤完了 --> 地瓜总共烤了{self.cook_time}分钟，现在的状态是：{self.cook_state}，调料有：{self.condiments}')

    """↓↓↓2、添加方法↓↓↓"""
    def cooking(self, time):
        """烤地瓜的方法"""
        self.cook_time += time  # 时间累加 ==> 烤一会看一眼
        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_state = '熟了'
        elif self.cook_time >= 8:
            self.cook_state = '烤糊了'
        # print(f'地瓜已经烤了{self.cook_time}分钟，地瓜现在的状态是：{self.cook_state}。')

    def add_condiments(self, condiment):
        self.condiments.append(condiment)


sweet_potato = SweetPotato()
sweet_potato.cooking(2)
sweet_potato.add_condiments('辣椒面')
print(sweet_potato)
sweet_potato.cooking(1)
sweet_potato.cooking(1)
sweet_potato.cooking(1)
sweet_potato.add_condiments('蜂蜜水')
print(sweet_potato)
