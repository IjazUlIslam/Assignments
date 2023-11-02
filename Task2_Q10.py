def perfect(number):
    sum_number = 0
    for i in range(1, number):
        if number % i == 0:
            sum_number += i
    if sum_number == number:
        print(f" {number} is perfect number ")
    else:
        print(f" {number} is not a perfect number ")

perfect(int(input("Enter your number : ")))