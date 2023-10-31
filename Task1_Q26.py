# 26. Write a program to generate all combinations of 1, 2 and 3 using for loop

elements = [1, 2, 3]
store_elements = []
for first in elements:
    for second in elements:
        for third in elements:
            combination = [first, second, third]
            store_elements.append(combination)

for i in store_elements:
    print(i)