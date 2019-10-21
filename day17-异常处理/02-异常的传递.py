"""
需求：
1、尝试以只读方式打开test.txt文件，如果存在则读取文件内容，文件不存在则提示用户即可
2、读取内容要求：尝试循环读取内容，读取过程中如果检测到用户意外终止程序。则except捕获异常并提示用户

结论：嵌套写法的异常是从外层开始
"""
import time

try:
    # 尝试打开文件
    f = open('test.txt', 'r')
    try:
        while True:
            # 循环读取文件的每一行，读取不到内容是退出
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)  # 暂停三秒
            print(content)
    except:
        # 拖过在读取文件的过程中，产生了异常，那么就会捕获到
        # 模拟实现：命令行执行中按下ctrl+c
        print(f'读取数据意外终止了')
    finally:
        f.close()
except Exception as res:
    print(f'打开文件出现错误：{res}')
