class Student(object):
    """
    学员角色类
    name：学员姓名; gender：学员性别; tel：学员联系方式
    """
    def __init__(self, name, gender, tel):
        self.name, self.gender, self.tel = name, gender, tel

    def __str__(self):
        return f'该学员姓名为：{self.name}，性别：{self.gender}，联系方式：{self.tel}'


if __name__ == '__main__':
    _XM = Student('小明', '男', 111)
    print(Student.__doc__)
    print(_XM)
