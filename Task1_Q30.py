# 30. Write a program that takes the side of a square from user and then prints that square out
# of asterisks. Your program should work for squares of all side sizes between 1 and 20.
# For example, if your program reads a size of 4, it should print
# ****
# ****
# ****
# ****
side_length = int(input("Enter side of Square : "))
for i in range(side_length):
    print("*" * side_length)