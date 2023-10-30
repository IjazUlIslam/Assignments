# 10. Write a program that take year as an input from user. Determine whether year is leap year
# or not.
year = int(input("enter your year : "))
if year % 4 == 0 and year % 100 != 0 or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")