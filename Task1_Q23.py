positive_counts = 0
negative_counts = 0
zero_counts = 0
while True:
    try:
        number = float(input("Enter a number (or '0' to stop) : "))
        if number == 0:
            break
        elif number > 0:
            positive_counts += 1
        elif number < 0:
            negative_counts += 1
        else:
            zero_counts += 1
    except ValueError:
        print("Invalid number. please enter a valid number or '0' to stop")

print(f"Count of positive number : {positive_counts}")
print(f"Count of negative number : {negative_counts}")
print(f"Count of zero number : {zero_counts}")