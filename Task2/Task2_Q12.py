random_list = [12, 23, 4, 5, 76, 9, 8, 32, 15, 6]
random_list.sort()
n = len(random_list)
# To find mean
sum_elements = 0
for i in random_list:
    sum_elements += i
mean = sum_elements / n
print(f"Mean of {random_list} is : {mean}")
# To find Median 
if n % 2 == 1:
    median = random_list[n // 2]
else:
    middle1 = random_list[n // 2 - 1 ]
    middle2 = random_list[n // 2]
    median = (middle1 + middle2) / 2
print(f"Median of {random_list} is : {median}")



