"""
Write a program that switches the values stored in the variables a and b.
Warning.
Your program should work for different inputs. e.g. any value of a and b.
Example Input
a: 3
b: 5
Example Output
a: 5
b: 3
"""
a = input("a:")
b = input("b:")

c = a
a = b
b = c

print(f"a:{a}\nb:{b}")
