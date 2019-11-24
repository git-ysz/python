from StudentManagerSystem.student import *


class StudentManager(object):
    """
    管理系统
    """
    def __init__(self):
        # 储存数据所用的列表
        self.student_list = []

    def __str__(self):
        return '学员管理系统'

    # 程序入口函数，启动程序后执行的函数
    def run(self):
        # 1.加载学员信息
        self.load_student()

        while True:
            # 2.显示功能菜单
            self.show_menu()

            # 3.用户输入功能序号
            menu_num = int(input('请输入功能序号：'))

            # 4.根据用户输入的功能序号执行不同的功能
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 修改学员信息
                self.modify_student()
            elif menu_num == 4:
                # 查询学员信息
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
            elif menu_num == 7:
                # 退出系统 -- 退出循环
                print('--退出系统--')
                break

    """系统功能函数"""

    def load_student(self):
        pass

    @staticmethod
    def show_menu():
        """
        显示功能菜单 -- 打印序号的功能对应关系 -- 静态方法
        """
        print('请选择如下功能')
        print('1：添加学员')
        print('2：删除学员')
        print('3：修改学员信息')
        print('4：查询学员信息')
        print('5：显示所有学员信息')
        print('6：保存学员信息')
        print('7：退出系统')

    def add_student(self):
        print('--添加学员信息--')
        # 1.用户输入姓名、性别、手机号
        name, gender, tel = input('请输入学员姓名：'), input('请输入学员性别：'), input('请输入学员联系方式：')
        # 2.创建学员对象 -- 学员类在student文件内，导入该模块，创建学员类
        student = Student(name, gender, tel)
        print(student)
        # 3.将该学员添加到学员列表
        self.student_list.append(student)

    def del_student(self):
        print('--删除学员信息--')
        # 1.用户输入目标学员姓名
        del_name = input('请输入要删除的学员的姓名：')
        # 2.遍历学员列表，如果用户输入的学员存在则删除学员对象，否则提示学员不存在
        for i in self.student_list:
            if i.name == del_name:
                # 删除该学员
                self.student_list.remove(i)
                print('删除成功！')
                break
        else:
            print('该学员不存在。')
        print(self.student_list)

    def modify_student(self):
        print('--修改学员信息--')

    def search_student(self):
        print('--查询学员信息--')

    def show_student(self):
        print('--显示所有学员信息--')

    def save_student(self):
        print('--保存学员信息--')
