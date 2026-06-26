members = int(input("Enter Number of Family Members: "))
litres_per_person = float(input("Enter Average Litres Per Person: "))

daily_consumption = members * litres_per_person
weekly_consumption = daily_consumption * 7
monthly_consumption = daily_consumption * 30

print("--- Water Consumption Tracker ---")
print("Total Daily Consumption:", daily_consumption, "litres")
print("Weekly Consumption:", weekly_consumption, "litres")
print("Monthly Consumption (30 days):", monthly_consumption, "litres")
print("-----------------")