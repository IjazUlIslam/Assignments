# Two numbers (base and exponent) are entered through the keyboard. Write a program to
# find the value of base raised to the power of exponent.

base_number = int(input("Enter your base number : "))
exponent_number = int(input("Enter your Exponent number : "))

result = base_number ** exponent_number
print(f"base raised to the power of exponent : {base_number} ^ {exponent_number} = {result}")
