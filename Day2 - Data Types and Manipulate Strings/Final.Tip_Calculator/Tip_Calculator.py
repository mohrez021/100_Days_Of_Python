print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
people_number = int(input("How many people to split the bill? "))

bill_with_tip = bill + (bill * tip)

bill_per_person = ("{:.2f}".format(bill_with_tip / people_number))

print(f"Each person should pay: ${bill_per_person}")
