laptop_price = float(input("Enter Laptop Price: "))
down_payment = float(input("Enter Down Payment: "))
months = int(input("Enter EMI Duration (Months): "))

remaining_amount = laptop_price - down_payment
monthly_emi = remaining_amount / months

print("--- EMI Statement ---")
print("Laptop Price:", laptop_price)
print("Down Payment:", down_payment)
print("Remaining Amount:", remaining_amount)
print("Monthly EMI:", round(monthly_emi, 2))
print("---------------------")