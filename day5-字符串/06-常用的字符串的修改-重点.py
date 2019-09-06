"""
重点使用
1、字符串序列.replace(旧子串, 新子串[, 替换次数])：替换
    1.1、返回的字符串是替换后的数据
    1.2、不会修改原数据

2、字符串序列.split(分割字符, num:分割次数)：分割
    1.1、返回的数据为列表
    2.2、返回数据中不会存在分割字符
    2
3、字符或子串.join(列表)：合并列表为字符串
    3.1、返回数据为字符串

数据是否可以改变，划分为“可变类型” 和 “不可变类型”
“字符串”属于不可变数据类型！！！
"""
myStr = 'hello world and itcast and itheima and Python'

# 1、replace() 把‘and’替换成‘和’
newReplaceStr = myStr.replace('and', '和', 2)
print(myStr)
print(newReplaceStr)

# 2、split() -- 分割
list1 = myStr.split('and')
list2 = myStr.split('and', 2)
print(list1)
print(list2)

# 3、join() -- 合并列表里的字符串数据为一个大字符串
list3 = ['123', '456', 'qfas']
newJoinStr = '...'.join(list3)
print(newJoinStr)
