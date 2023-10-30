# Q1. Write a program that asks the user to enter two numbers, obtains them from the user and
# prints their sum, product, difference, quotient and remainder.

num1 = int(input("enter num1 : "))
num2 = int(input("enter num2 : "))
sums = num1 + num2
print(num1, "+", num2, "=", sums)
mult = num1 * num2
print(num1, "*", num2, "=", mult)
sub = num2 - num1
print(num2, "-", num1, "=", sub)
div = num1 / num2
print(num1, "/", num2, "=", div)
rem = num1 % num2
print(num1, "%", num2, "=", rem)
