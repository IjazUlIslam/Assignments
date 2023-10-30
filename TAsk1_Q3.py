# Write a program that takes the marks obtained by a student in five different subjects as
# input through the keyboard, then find out the total marks and percentage marks obtained
# by the student in each subject. Assume that the maximum marks that can be obtained by a
# student in each subject is 100.
maths = float(input("Enter marks of Maths : "))
while maths > 100:
    print("You entered your marks greater than 100 you need to enter marks less than 100")
    maths = float(input("enter marks of maths less than 100 : "))
java = float(input("Enter marks of java : "))
while java > 100:
    print("You entered your marks greater than 100 you need to enter marks less than 100")
    java = float(input("enter marks of java less than 100 : "))
python = int(input("Enter marks of python : "))
while python > 100:
    print("You entered your marks greater than 100 you need to enter marks less than 100")
    python = float(input("enter marks of python less than 100 : "))
oop = int(input("Enter marks of oop : "))
while oop > 100:
    print("You entered your marks greater than 100 you need to enter marks less than 100")
    oop = float(input("enter marks of oop less than 100 : "))
operating_system = int(input("Enter marks of Operating System : "))
while operating_system > 100:
    print("You entered your marks greater than 100 you need to enter marks less than 100")
    operating_system = float(input("enter marks of operating system less than 100 : "))

total_marks = maths + java + python + oop + operating_system
print("Total Marks of Student : ", total_marks)

per_in_maths = (maths/100) * 100
print("percentage in Maths : ",per_in_maths,"%")
per_in_java = (java/100) * 100
print("percentage in Java : ",per_in_java,"%")
per_in_python = (python/100) * 100
print("percentage in python : ",per_in_python,"%")
per_in_oop = (oop/100) * 100
print("percentage in oop : ",per_in_oop,"%")
per_in_operating_system = (operating_system/100) * 100
print("percentage in Operating System : ",per_in_operating_system,"%")
