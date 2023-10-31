# 31. Write a program that displays the following checkerboard pattern:
# * * * * * * *
# * * * * * * * *
#  * * * * * * * *
# * * * * * * * *
#  * * * * * * * *
# * * * * * * * *
#  * * * * * * * *
# * * * * * * * *
# Your program must use only three output statements, one of each of the following forms:
# print "* "
# print " "

number_of_rows = int(input("Enter number of rows : "))
number_of_columns = int(input("Enter number of columns : "))
for i in range(number_of_rows):
    for j in range(number_of_columns):
        if (i + j) % 2 == 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()