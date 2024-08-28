height = float(input("Enter your height in meters: "))  # Type conversion to float is a must
weight = float(input("Enter your weight in kilograms: "))
BMI = weight / (height ** 2)  # BMI count formula

print("Your BMI count is", BMI)
