cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

difference = selling_price - cost_price

print("--- Profit & Loss Statement ---")
print("Cost Price:", cost_price)
print("Selling Price:", selling_price)

if difference > 0:
    print("Result: Profit")
    print("Profit Value:", difference)
elif difference < 0:
    print("Result: Loss")
    print("Loss Value:", abs(difference))
else:
    print("Result: No Profit, No Loss")
print("-------------------------------")