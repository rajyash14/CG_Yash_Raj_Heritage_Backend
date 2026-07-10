consumer_name = input("Enter Consumer Name: ")
units = float(input("Enter Units Consumed: "))

rate = 8
bill_amount = units * rate
gst = bill_amount * 0.18
final_amount = bill_amount + gst

print("--- Electricity Bill ---")
print("Consumer Name:", consumer_name)
print("Bill Amount: ₹" + str(bill_amount))
print("18% GST: ₹" + str(gst))
print("Final Amount: ₹" + str(final_amount))
print("--------------")