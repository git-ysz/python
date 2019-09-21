"""
需求：批量修改文件名，既可添加指定字符串，又能删除指定字符串。
步骤：
1、设置添加删除字符串的标识
2、获取指定目录的所有文件
3、将原有文件名添加、删除指定字符串，构造新名字
4、os.rename(),重命名
"""
import os

flag = 2  # 判断flag等于1时为添加，等于2时为删除指定字符串
# 找到所有文件：获取aa文件夹内的目录列表 -- listdir
# 改变默认目录为aa
os.chdir('./aa')
file_list = os.listdir()
print(file_list)

for i in file_list:
    if flag == 1:
        new_name = 'python-' + i
    elif flag == 2:
        num = len('python-') if i.find('python-') == 0 else 0
        new_name = i[num:]
    print(new_name)
    os.rename(i, new_name if new_name else i)
