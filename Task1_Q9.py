# Q9. A company insures its drivers in the following cases:
# − If the driver is married.
# − If the driver is unmarried, male & above 30 years of age.
# − If the driver is unmarried, female & above 25 years of age.
# In all other cases, the driver is not insured. If the marital status, sex and age of the driver
# are the inputs, write a program to determine whether the driver is to be insured or not.
martial_status = input("Enter you martial status (married / unmarried) : ")
age = int(input("Enter you age : "))
sex = input("Enter driver sex (male / female) :")
if martial_status == "married":
    print("insured")
elif martial_status == "unmarried" and sex == "male" and age > 30:
    print("insured")
elif martial_status == "unmarried" and sex == "female" and age > 25:
    print("insured")
else:
    print("not insured")