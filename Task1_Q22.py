# Q22. Write a program that calculates and prints the sum of the even integers from 2 to 30
sum_number = 0
for number in range(30):
    if number % 2 == 0:
        sum_number += number
print("Sum of all even number upto 30 : ", sum_number)
