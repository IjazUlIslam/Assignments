def Celsius(temprature_in_fahrenheit):
    celsius = (temprature_in_fahrenheit - 32) * 5 /9
    return celsius

def Fahrenheit(temprature_in_celsius):
    fahrenheit = (temprature_in_celsius * 9 /5 ) + 32
    return fahrenheit

print(Celsius(float(input("Enter temprature in Fahrenheit : "))), "'C")
print(Fahrenheit(float(input("Enter temprature in Celsius : "))), "'F")
