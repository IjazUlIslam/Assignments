# Write a program that reads in the radius of a circle and prints the circle‟s diameter,
# circumference and area. Use the constant value 3.14159 for pi. Perform each of these
# calculations inside the print statement(s) and use the conversion format specifier %f.
radius = float(input("Enter radius of circle : "))
diameter = radius * 2
circumference = 3.14159 * (radius)**2
print(f" Diameter of circle is : {diameter}")
print((f" circumference of circle is : {circumference}"))