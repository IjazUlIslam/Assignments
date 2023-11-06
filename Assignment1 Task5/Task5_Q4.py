# 4. Write a Python program to remove duplicates from a list
my_list = [2, 4, 3, 4, 2, 7, 4, 2]
new_list =[]
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)