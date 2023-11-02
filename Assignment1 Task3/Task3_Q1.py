# 1. Implement a function that meets the specification below. Use a try-except block.
# def sumDigits(s):
# """Assumes s is a string
# Returns the sum of the decimal digits in s
# For example, if s is 'a2b3c' it returns 5"""


def sumDigits(s):
    integers = "0123456789"
    sum_digits = 0
    for i in s:
        if i in integers:
            sum_digits += int(i)
    return sum_digits

input_string = sumDigits(input("Enter a string with decimal numbers : "))
print(input_string)