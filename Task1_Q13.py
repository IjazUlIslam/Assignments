# 13. Write a program that asks the user to enter two integers, obtains the numbers from the
# user, then prints the larger number followed by the words “is larger.” If the numbers are
# equal, print the message “These numbers are equal.” Use only the single-selection form
# of the if statement you learned in this chapter.

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
if num1 > num2 :
    print(f"{num1} is larger than {num2}")
elif num1 < num2:
    print(f"{num2} is larger than {num1}")
elif num1 == num2:
    print("These numbers are equal")