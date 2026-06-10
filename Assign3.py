# 7. Calculate compound growth

print("--- Question 7 ---")
initial_value = 1000
growth_factor = 1.1
years = 5

# Using the exponent operator (**)
final_value = initial_value * (growth_factor ** years)
print(f"The final value after {years} years is: {final_value:.2f}\n")


# 8. Candies distribution

print("--- Question 8 ---")
total_candies = 567
students = 25

# Floor division (//) to get candies per student
candies_per_student = total_candies // students
# Modulo (%) to get the remainder
candies_left = total_candies % students

print(f"Each student gets: {candies_per_student} candies")
print(f"Candies left over: {candies_left} candies\n")


# Part B: Comparison Operators

# 9. Compare two numbers entered by the user

print("--- Question 9 ---")
# Using float() to allow decimal numbers as well
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"Comparison results for {num1} and {num2}:")
print(f"{num1} == {num2} : {num1 == num2}")
print(f"{num1} != {num2} : {num1 != num2}")
print(f"{num1} > {num2}  : {num1 > num2}")
print(f"{num1} < {num2}  : {num1 < num2}")
print(f"{num1} >= {num2} : {num1 >= num2}")
print(f"{num1} <= {num2} : {num1 <= num2}\n")


# 10. Check whether a person's age is 18 or above

print("--- Question 10 ---")
age = int(input("Enter the person's age: "))
if age >= 18:
    print("The person is 18 or above (Adult).\n")
else:
    print("The person is under 18 (Minor).\n")


# 11. Check if two strings entered by user are equal

print("--- Question 11 ---")
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if string1 == string2:
    print("The two strings are exactly equal.\n")
else:
    print("The two strings are not equal.\n")


# 12. Verify whether a number lies between 50 and 100

print("--- Question 12 ---")
check_num = float(input("Enter a number to check: "))

# In Python, you can chain comparison operators
if 50 <= check_num <= 100:
    print(f"Yes, {check_num} lies between 50 and 100 (inclusive).\n")
else:
    print(f"No, {check_num} is outside the range of 50 to 100.\n")