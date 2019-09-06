str1 = 'abcd'
list1 = [10, 20, 30, 40]
t1 = (10, 20, 30, 40)
dict1 = {'name': 'Tom', 'age': 20}
s1 = {'Tom', 'Lily'}

# in 和 not in
print('a' in str1, 'a' not in str1)
print(10 in list1, 10 not in list1)
print(10 in t1, 10 not in t1)

print('name' in dict1, 'name' not in dict1)
print('name' in dict1.keys(), 'Tom' in dict1.values())

print('Tom' in s1, 'Tom' not in s1)
