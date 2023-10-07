bill = 0
print("Welcome to Python Pizza Deliveries")
size = str.upper(input("What size pizza do you want? (S,M,L) "))
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Please select between S, M, or L")

add_pepperoni = str.upper(input("Do you want pepperoni? (Y/N)"))
extra_cheese = str.upper(input("Do you want extra cheese? (Y/N)"))

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
