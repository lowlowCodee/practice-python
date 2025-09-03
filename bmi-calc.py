import math

print("BMI Calculator!")

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))


BMI = weight / (height ** 2)

if BMI >= 30:
    print("Obese")
elif BMI >= 25:
    print("Over Weight")
elif BMI >= 18.5:
    print("Normal Weight")
else:
    print("Underweight")
    
print("Your BMI is " + str(BMI))