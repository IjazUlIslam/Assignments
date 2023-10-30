# Given the length and breadth of a rectangle, write a program to find whether the area of
# the rectangle is greater than its perimeter. For example, the area of the rectangle with
# length = 5 and breadth = 4 is greater than its perimeter

length = float(input("enter length of Rectangle : "))
breadth = float(input("enter breadth of Rectangle : "))
area = length * breadth
perimeter = (length + breadth) * 2
if area > perimeter:
    print("area of rectangle is greater than perimeter")
else:
    print("Perimeter of rectangle is greater than area ")