# Write your code below this line 👇
def prime_checker(number):
    result = ""
    if number == 1 or number == 2:
        print("It's a prime number.")

    for divider in range(2, number):
        if number % divider == 0:
            result = "It's not a prime number."
            break
    if result == "":
        result = "It's a prime number."
    
    print(result)


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: ")) 
prime_checker(number=n)