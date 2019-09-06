"""
定义用户信息全局变量 -- 字典组成的列表
每位学员信息如下：
1.姓名 2.学号 3.联系电话
"""
users = []


def info_print():
    """定义功能界面函数"""
    print('请选择功能：')
    print('1、添加学员')
    print('2、删除学员')
    print('3、修改学员')
    print('4、查询学员')
    print('5、显示所有学员')
    print('6、退出系统')
    print('-' * 20)


def add_user_info():
    """添加学员的函数"""
    # global users
    # 1.1 输入学员信息
    new_id = input('请输入学号：')
    new_name = input('请输入姓名：')
    new_phone = input('请输入联系方式：')
    # 1.2 检测用户输入的学号或姓名是否已存在
    for i in users:
        if new_name == i['name']:
            print('该学员已存在！请重新输入↓')
            add_user_info()
            return
    users.append({
        'id': new_id,
        'name': new_name,
        'phone': new_phone
    })
    print(f'学员{new_name}已添加，正在返回功能界面')
    print(users)


def del_user():
    """删除学员"""
    global users
    del_name = input('请输入要删除学员的姓名：')
    for i in users:
        if i['name'] == del_name:
            if input('请确认是否删除该学员？[y:是，n:否]') == 'y':
                print(f'学员{i["name"]}删除成功')
                users.remove(i)
                print(users)
            else:
                print('已取消删除')
            # 已经查找到信息，退出循环
            break
    else:
        # 循环正常结束执行的代码 -- 没有break
        print('该学员不存在，正在返回功能界面')


def modify_user():
    """修改学员手机号信息"""
    global users
    # 用户输入学员姓名
    modify_name = input('请输入需要修改的学员姓名：')
    for i in users:
        if i['name'] == modify_name:
            i['phone'] = input('请输入您需要修改的学员的新手机号码：')
            print('修改成功！，正在返回功能界面')
            print(users)
            break
    else:
        print('该学员不存在...')


def query_user():
    """查询某个学员"""
    query_name = input('请输入您需要查询的学员姓名：')
    for i in users:
        if query_name == i['name']:
            print(f'您查询的学员姓名{i["name"]}，学号{i["id"]}，联系方式{i["phone"]}')
            if input('请确定是否继续查询？[y:是，n:否]') == 'y':
                query_user()
            print('正在返回功能界面...')
            break
    else:
        print('您查询的学员不存在，正在返回功能界面...')


def query_all_user():
    """查询所有学员信息"""
    for i in users:
        print(f'姓名：{i["name"]}，学号：{i["id"]}，联系方式：{i["phone"]}。')
    print('已查询所有学员信息，正在返回功能界面...')


"""
无限循环，为了趋近真实情况
执行完功能后可以选择其他功能
只有用户输入6（退出系统后方可结束程序）
"""
while True:
    # 1、显示功能界面
    info_print()

    # 2、用户输入功能序号
    user_num = int(input('请输入功能序号：'))

    # 3、按照用户输入的功能序号，执行不同的功能（函数）
    if user_num == 1:
        # print('添加')
        add_user_info()
    elif user_num == 2:
        # print('删除')
        del_user()
    elif user_num == 3:
        # print('修改')
        modify_user()
    elif user_num == 4:
        # print('查询')
        query_user()
    elif user_num == 5:
        # print('查询所有')
        query_all_user()
    elif user_num == 6:
        if input('确定要退出系统？[y:是，n:否]') == 'y':
            print('正在退出系统...')
            break
        print('已取消退出系统，正在返回功能界面')
        continue
    else:
        print('您输入的序号有误，请重新输入：')
        continue
    # ...........

print('系统已退出。')
