# If the three sides of a triangle are entered through the keyboard, write a program to check
# whether the triangle is isosceles, equilateral, scalene or right-angled triangle.
angel1 = int(input("Enter angle 1 : "))
angel2 = int(input("Enter angle 2 : "))
angel3 = int(input("Enter angle 3 : "))
if angel1 == angel2 and angel1 != angel3 or (angel1 == angel3 and angel2 != angel3 ) or (angel2 == angel3 and angel1 != angel2) :
    print("This is isosceles Triangle")
elif angel1 == angel2 == angel3:
    print("This is equilateral Triangle")
elif angel1 != angel2 != angel3:
    print("This is Scalene Triangle")
elif angel1 + angel2 + angel3 == 180 and (angel1 == 90 or angel2 == 90 or angel3 == 90):
    print("This right-angled ")
