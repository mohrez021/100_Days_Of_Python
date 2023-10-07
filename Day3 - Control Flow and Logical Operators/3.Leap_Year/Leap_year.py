year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            result = "Leap year!"
        else:
            result = "Not Leap year"
    else:
        result = "Leap year!"
else:
    result = "Not Leap year!"

print(result)
