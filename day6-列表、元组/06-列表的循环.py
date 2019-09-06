name_list = ['Tom', 'Lily', 'Rose']

i = 0
while i < len(name_list):
    print(name_list[i], end='\n' if (i == len(name_list) - 1) else ',')
    i += 1

for j in name_list:
    print(j, end='\n' if (name_list.index(j) == len(name_list) - 1) else ',')
