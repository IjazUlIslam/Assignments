# Q5. The length & breadth of a rectangle are input through the keyboard. Write a program to
# calculate the area & perimeter of the rectangle.

length = float(input("enter length of Rectangle : "))
breadth = float(input("enter breadth of Rectangle : "))
area = length * breadth
perimeter = (length + breadth) * 2
print(f"Area of Rectangle is : {area}")
print(f"Perimeter of Rectangle is : {perimeter}")