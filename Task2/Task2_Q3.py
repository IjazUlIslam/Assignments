def take_number_user(number):
    sum_of_digits = 0
    actual_number = number
    while number > 0:
        digit = number % 10
        cube_of_digit = digit**3
        sum_of_digits += cube_of_digit
        number //= 10
    if sum_of_digits == actual_number:
        print(f"{actual_number} is Armstrong")
    else:
        print(f"{actual_number} is not Armstrong")
    print(sum_of_digits)
take_number_user(int(input("Enter a number : ")))