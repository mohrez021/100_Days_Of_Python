# for counting string len("str")
# slice srtring :   "string"[start:end:step]
# print("Hello"[::-1])

# integer and float and boolean
# print(123_456_7890045644)
# print(3.141_59)
# print(True, False)

# convert types - type conversion (type casting)
# a = 123
# print(type(a))
# print(type(float(a)))
# print(type(str(a)))
# print(70 + float("100.5"))
# print("70" + str(100))

# print(len(str(123_456_7)))

# output of len function is integer
# num_char = len(input("What is your name? "))
# print(type(num_char))
# num_char = str(num_char)
# print(type(num_char))
# print("your name has " + num_char + " characters.")

'''
mathematical operations: + - / * % ** 
+=  /=  *=  -=

priority: PEMDAS=>
    Parentheses     ()
    Exponents       **
    Multiplication *  Division /    => left to right
    Addition +   Subtraction-       => left to right
'''
# print(3 * 3 + 3 / 3 - 3) # => (((3*3) + (3/3)) - 3) = 7
# print(3 * (3 + 3) / 3 - 3)  # => (((3 * (3 + 3)) / 3) - 3) = 3
# num = 8 // 4
# num += 8  #=> num = num + 8
# print(num)

'''
Number Manipulation and F Strings in Python
round()
/ => result is float
// => result is integer (ignore all numbers after decimal point.)
f"{var1} string {var2} string string {varn}"
'''
# print(8/3)  # => 2.6666666666666665
# print(int(8/3))  # => 2
# print(round(8/3))  # => 3
# print(round(8 / 3, 2))  # => 2.67
# print(8 // 3)  # => 2
