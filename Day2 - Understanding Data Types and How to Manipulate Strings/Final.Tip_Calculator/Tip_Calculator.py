print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
# number / 100 => give us percentage
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
people_number = int(input("How many people to split the bill? "))
bill_with_tip = bill + (bill * tip)

# round doesnt show last zero. ex: round(10.6000, 2) => 10.6  - but we want float output with 2 decimal points like 10.60
# so we use "{:.2f}".format(10.600000)
bill_per_person = ("{:.2f}".format(bill_with_tip / people_number))

print(f"Each person should pay: ${bill_per_person}")
