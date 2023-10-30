# 16. Write a program to check whether a triangle is valid or not, when the three angles of the
# triangle are entered through the keyboard. A triangle is valid if the sum of all the three
# angles is equal to 180 degrees.
angle1 = int(input("Enter angle 1 : "))
angle2 = int(input("Enter angle 2 : "))
angle3 = int(input("Enter angle 3 : "))
triangle = angle1 + angle2 + angle3
print(f"Sum of all angles is : {triangle}")
if triangle == 180:
    print("triangle is valid ")
else:
    print("triangle is not valid ")