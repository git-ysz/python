"""
lambda的参数形式和函数的参数形式相同
"""

# 1.无参数
fn1 = lambda: 200

# 2.默认参数
fn2 = lambda a, b, c=100: a + b + c

# 3.可变参数（不定数参数） *args
# 可变参数允许你传入0个或任意个参数
# 这些可变参数在函数调用时自动组装为一个tuple。
fn3 = lambda *args: args 

# 4.关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数
# 这些关键字参数在函数内部自动组装为一个dict
fn4 = lambda **kw: kw
# print(fn4(name='tom', age=16))

# 5.命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
fn5 = lambda *, name, age: f'name:{name},age:{age}'
# print(fn5(name='tom', age=16))
