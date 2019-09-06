"""
判断是否以某个字符串开头或结尾
1、startswith(子串， 开始下标， 结束下标)
2、endswith(子串， 开始下标， 结束下标)
"""
str1 = 'hello world'

# 1、startswith
print(str1.startswith('hell'))
print(str1.startswith('ell'))

# 2、endswith
print(str1.endswith('rld'))
print(str1.endswith('rl'))

myStr = 'hello world and itcast and itheima and Python'

# 3、isalpha 判断所有下标都非空
print(myStr.isalpha())

# 4、isdigit 判断全是数字组成
print(myStr.isdigit())
print('1231234'.isdigit())

# 5、isalnum 都是数字或字母或组合
print('12345'.isalnum())
print('12a4 5'.isalnum())
print('12aaa5'.isalnum())

# 6、isspace 空白字符
print('   '.isspace())
print('  1 a '.isspace())
