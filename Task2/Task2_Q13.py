integer_list = [12, 23, 34, 45, 34, 12, 45, 54, 67, 87, 98, 78, 34, 65, 77, 99, 44, 23, 34, 67]
new_list = []
for i in integer_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)
