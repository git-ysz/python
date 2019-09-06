"""
非重点
"""
myStr = '    hello world and itcast and itheima and Python    '
print(myStr)
"""
处理英文字符大小写
"""
# 1、capitlize() 字符串首字母大写
print(myStr.capitalize())

# 2、title() 字符串中所有单词开头大写
print(myStr.title())

# 3、upper() 小写转大写
print(myStr.upper())

# 4、lower() 大写转小写
print(myStr.lower())
"""
处理空白字符
"""
# 5、lstrip() 删除字符左侧空白字符
print(myStr.lstrip())

# 6、rstrip() 删除字符右侧空白字符
print(myStr.rstrip())

# 7、strip() 删除字符左右空白字符
print(myStr.strip())
"""
处理字符对齐方式
"""
str1 = 'hello'
# 8、字符串序列.ljust(num:对齐最多长度，填充字符)
print(str1.ljust(10))
print(str1.ljust(10, '.'))

# 9、字符串序列.rjust(num:对齐最多长度，填充字符)
print(str1.rjust(10))
print(str1.rjust(10, '.'))

# 10、字符串序列.center(num:对齐最多长度，填充字符)
print(str1.center(11))
print(str1.center(11, '.'))
