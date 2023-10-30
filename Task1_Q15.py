# Q15. (Body Mass Index Calculator) We introduced the body mass index (BMI) calculator in
# The formulas for calculating BMI are
# BMI = (weightInKilograms) / (heightInMeters * heightInMeters)
# Create a BMI calculator application that reads the user‟s weight in kilograms and height
# in meters, then calculates and displays the user‟s body mass index. Also, the application
# should display the following information from the Department of Health and Human
# Services/National Institutes of Health so the user can evaluate his/her BMI:
# BMI VALUES
# Underweight: less than 18.5
# Normal: between 18.5 and 24.9
# Overweight: between 25 and 29.9
# Obese: 30 or greater

weightInKilograms = int(input("enter your weight in Kg : "))
heightInMeters = int(input("enter your height in meters : "))
BMI = (weightInKilograms) / (heightInMeters * heightInMeters)
print(f"BMI value is : {BMI}")
if BMI < 18.5:
    print(f"Underweight : less than 18.5")
elif BMI > 18.5 and BMI < 24.9:
    print(f"Normal : Between 18.5 and 24.9")
elif BMI > 25 and BMI < 29.9:
    print(f"Overweight : between 25 and 29.9")
else:
    print(f"30 or greater")