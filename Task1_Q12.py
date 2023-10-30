# Write a program that reads in two integers and determines and prints whether the first is a
# multiple of the second. [Hint: Use the remainder operator.

num1 = int(input("enter num1 : "))
num2 = int(input("enter num2 : "))
if num1 % num2 == 0:
    print("first number is the multiple of second number")
else:
    print("first number is not multiple of second number")