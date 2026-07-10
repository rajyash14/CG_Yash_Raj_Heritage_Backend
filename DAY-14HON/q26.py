player_name = input("Enter Player Name: ")
runs = int(input("Enter Runs Scored: "))
balls = int(input("Enter Balls Faced: "))

strike_rate = (runs * 100) / balls

print("Player Name:", player_name)
print("Strike Rate:", round(strike_rate, 2))