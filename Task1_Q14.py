# 14. Write a program that inputs three different integers from the keyboard (i.e num1, num2,
# num3), then prints the sum, the average, the product, the smallest and the largest of these
# numbers. The screen dialogue should appear as follows:
# Enter three different integers: 13 27 14
# Sum is 54
# Average is 18
# Product is 4914
# Smallest is 13
# Largest is 27

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
num3 = int(input("Enter num3 : "))
sums = num1 + num2 + num3
print(f"Enter Three different integers : {num1} {num2} {num3}")
print("Sum is ", sums)
average = (num1 + num2 + num3) / 3
print("Average is ", average)
product = num1 * num2 * num3
print("Product is ", product)

smallest = largest = num1
if num2 < smallest:
    smallest = num2
elif num2 > largest:
    largest = num2
if num3 < smallest:
    smallest = num3
elif num3 > largest:
    largest = num3
print(f"Smallest is {smallest}")
print(f"Largest is {largest}")