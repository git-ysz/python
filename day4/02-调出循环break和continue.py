"""
break：当某些条件成立，退出整个循环
continue：当某个条件成立，跳过本次循环，进行下一次循环
"""
# 吃苹果案例
i = 1
while i <= 5:
    # 条件：如果吃完第三个，打印吃饱了
    if i == 4:
        print('吃饱了，不吃了')
        break
    if i == 2:
        print(f'第{i}个苹果有虫子，吃下一个')
        i += 1
        # 如果使用continue，在执行continue之前，一定要修改计数器，否则进入死循环
        continue
    print(f'吃了第{i}个苹果')
    i += 1
print(i)
