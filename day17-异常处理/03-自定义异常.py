"""
需求：密码长度不足，则报异常（用户输入密码，如果输入长度不足三位，则报错，即抛出自定义异常，并捕获该异常）

关键字：raise -- 用于抛出自定义异常错误
"""


# 自定义的异常类，继承Exception
class ShortInputError(Exception):

    def __init__(self, length, min_len=3):
        self.length = length
        self.min_len = min_len

    # 设置抛出异常的描述信息
    def __str__(self):
        return f'您输入的长度为{self.length}，不能少于{self.min_len}个字符'


def main():
    try:
        password = input('请输入密码：')
        if len(password) < 3:
            raise ShortInputError(len(password), 3)
    except ShortInputError as res:
        print(res)
    else:
        print(f'输入的密码为{password}')


main()
