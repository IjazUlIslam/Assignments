# Q4. Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a
# program to convert this temperature into Centigrade degrees.

temp_in_fahrenheit = float(input("Enter temprature of city in Fahrenheit : "))
convert_to_centigrade = (temp_in_fahrenheit - 32) * 5/9
print("Centigrade = ", convert_to_centigrade)