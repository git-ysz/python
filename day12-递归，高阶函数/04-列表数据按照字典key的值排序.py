students = [
    {'name': 'Tom', 'age': 20},
    {'name': 'Rose', 'age': 19},
    {'name': 'Jack', 'age': 22}
]

students.sort(key=lambda x: x['age'])
print(students)

students.sort(key=lambda x: x['age'], reverse=True)
print(students)
