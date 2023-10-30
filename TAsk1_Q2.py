#Q2. The distance between two cities (in km.) is input through the keyboard. Write a program
# to convert and print this distance in meters, feet, inches and centimeters.

distance = int(input("Enter distance between two cities in Km :"))

convert_to_meters = distance * 1000
print("Conversion to Meters : ", convert_to_meters, "meter")
convert_to_feet = distance * 3280.84
print("Conversion to feet : ", convert_to_feet, "feet")
convert_to_inches = distance * 39370.1
print("Conversion to Inches : ", convert_to_inches, "inches")
convert_to_centimeters = distance * 100000
print("Conversion to Centimeters : ", convert_to_centimeters, "cent")
