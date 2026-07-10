name = input("Enter Name: ")
weight = float(input("Enter Weight (kg): "))
height = float(input("Enter Height (meters): "))

bmi = weight / (height ** 2)

print("Name:", name)
print("BMI:", round(bmi, 2))