"""
需求：用户输入当前目录下任意文件名，程序完成对该文件的备份功能（备份文件名为xx[备份].后缀，例如：test[备份].txt）
步骤：
    1、接收用户输入的文件名
    2、规划备份文件名
    3、备份文件写入数据(数据和源文件一样)

"""

# 1、输入
old_name = input('请输入您要备份的文件名：')

index = old_name.rfind('.')
if index > 0:
    # 2、规划备份文件名
    # 2.1、提取目标文件后缀
    hz_name = old_name[index:]
else:
    print('请输入正确的文件名')

# 2.2、组织备份的文件，xx[备份]后缀
file_new_name = f'{old_name[:index]}[备份]' + hz_name
print(file_new_name)

# 3、备份文件写入数据（数据和源文件一样）
# 3.1、打开原文件，备份文件
old_file = open(old_name, 'rb')
new_file = open(file_new_name, 'wb')
# 3.2、源文件读取，备份文件写入
# new_file.write(old_file.read())
# 如果不确定目标文件大小，循环读取写入，当读取出来的数据没有了，终止循环
while True:
    con = old_file.read(3)  # 每次读取写入1024字节
    if len(con) == 0:
        print('文件读取完成，备份完成！')
        break
    print(f'写入数据：{con}')
    new_file.write(con)
# 3.3、关闭文件
old_file.close()
new_file.close()
