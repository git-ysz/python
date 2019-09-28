"""
需求：将小于房子剩余面积的家具摆放到房子中
步骤分析：
需求设计两个事物：房子 和 家具，故被案例设计两个类，房子类 和 家具类
家具占地面积要小于房屋剩余面积才能放进屋子里
定义类：
一、房子类：
    实例属性：
        房子的地理位置
        房子总面积
        房子剩余面积
        房子内家具列表
    实例方法
        容纳家具
    显示房屋信息（__str__）
二、家具类：
    实例属性
        家具名称
        家具占地面积
"""


class Furniture:
    """家具类属性的初始化：名字，占地面积"""

    def __init__(self, name='', area=''):
        self.name, self.area = name, area

    def __str__(self):
        return f'该家具是{self.name}，占地面积为：{self.area}'


class House:
    """家具类属性初始化"""
    def __init__(self, address, area):
        self.address, self.area, self.free_area, self.furniture = address, area, area, []

    def __str__(self):
        return f'房屋的地理位置为：{self.address}，占地面积：{self.area}平米，剩余占地面积：{self.free_area}平米，房内家具有：{"、".join(self.furniture)}。'

    def add_furniture(self, item):
        """容纳家具函数，item:目标家具的对象"""
        if item.area <= self.free_area:
            """判断搬进家具的占地面积是否小于房子的剩余面积"""
            self.furniture.append(item.name)
            self.free_area -= item.area  # 更新房屋剩余占地面积
        else:
            print('该家具太大啦~装不进去了~~~')


# 家具实例化
bad = Furniture('双人床', 6)
sofa = Furniture('沙发', 10)
# 房屋实例化
home = House('上海市宝山区杨行镇宝启公寓', 145)
print(home)
home.add_furniture(bad)
print(home)
home.add_furniture(sofa)
print(home)
