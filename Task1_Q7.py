# If a five-digit number is input through the keyboard, write a program to calculate the sum
# of its digits. (Hint: Use the modulus operator „%‟ to split the digits)

number = int(input("enter your digit number : " ))
sum_of_digits = 0
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10
print("Sum of digit = ", sum_of_digits)
