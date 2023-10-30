# A library charges a fine for every book returned late. For first5 days, the fine is 50 paise,
# for 6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book
# after 30days your membership will be cancelled. Write a program to accept the number
# of days the member is late to return the book and display the fine or the appropriate
# message.
late_returned_days = int(input("Enter late days of returning book : "))
if late_returned_days <= 5:
    print("you fined 50 paise")
elif late_returned_days >= 6 and late_returned_days <= 10:
    print("you fined 1 Rs")
elif late_returned_days > 10 and late_returned_days <= 30:
    print("You fined 5 Rs")
elif late_returned_days > 30:
    print("your membership will be cancelled")