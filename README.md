# 100 Days of python

I want to track my path on learning python. and share it with others. so you can use it if you see this helpful.

### for counting string 
`len("str")`
### slice string
`
"string"[start:end:step]
`

```
print("Hello"[::-1])
```
output: olleH

## integer and float and boolean
```
print(123_456_7890045644)
```
out: 1234567890045644

```
print(3.141_59)
```
3.14159

```
print(True, False)
```
True False

## convert types - type conversion (type casting)
```
a = 123
print(type(a))                #int
print(type(float(a)))         #float
print(type(str(a)))           #str
print(70 + float("100.5"))    #170.5
print("70" + str(100))        #70100
```
## len()
* is used for counting number of characters
* output of len function is integer
```
print(len(str(123_456_7)))
```
ex:
```
num_char = len(input("What is your name? "))
print(type(num_char))
num_char = str(num_char)
print(type(num_char))
print("your name has " + num_char + " characters.")
```

## mathematical operations: + - / * % **
+=  /=  *=  -=
```
num1 += num2      # num1 = num1 + num2
num1 /= num2      # num1 = num1 / num2
num1 *= num2      # num1 = num1 * num2
num1 -= num2      # num1 = num1 - num2
```

priority: PEMDAS
1.     Parentheses     ()
2.     Exponents       **
3.     Multiplication *  Division /    => left to right
4.     Addition +   Subtraction-       => left to right

ex:
```
print(3 * 3 + 3 / 3 - 3) # => (((3*3) + (3/3)) - 3) = 7
print(3 * (3 + 3) / 3 - 3)  # => (((3 * (3 + 3)) / 3) - 3) = 3
num = 8 // 4
num += 8    #=> num = num + 8
print(num)  #=> 10
```

### Number Manipulation and F Strings in Python
int() به سمت پایین گرد میکنه عدد اعشاری رو
* round()
  * به سمتی که نزدیک تره عدد رو گرد میکنه 
    * round(2.6666666)        # 3
    * round(2.6666666, 2)     # 2.67

* / => result is float
* // => result is integer (ignore all numbers after decimal point.)
* f"{var1} string {var2} string string {varn}"

ex:
```
print(8/3)              # => 2.6666666666666665
print(int(8/3))         # => 2
print(round(8/3))       # => 3
print(round(8 / 3, 2))  # => 2.67
print(8 // 3)           # => 2
```

# Control Flow with if _ else and Conditional Operators
```
if condition:
    do this
else
    do this
```

### nested if/else
```
if condition:
    if another_condition:
        do this
    else:
        do this
else:
    do this
```

### if/elif/else
```
if condition1:
    do A
elif condition2:
    do B
elif condition3:
    do C
else:
    do this
```

### multiple if
```
if condition1:
    do this
if condition2:
    do this
if condition3:
    do this
```

### multiple condition:
* Logical operators: and or not
    ```
    a = 15
    a < 20 and a > 10 => True
    a < 10 or a > 20 => False
    not a < 10 => True
    ```
```
if condition1 and condition2 and condition3:
  do this
elif condition4 or condition5:
  do this
elif not condition6:
  do this
else:
  do this
```

* Comparison operators: >   >=   <   <=   ==   !=

#### example1: rollercoaster ticket
```
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride;.")
```

#### example2: roller coaster ticket
```
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

cost = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))

    if age < 12:
        cost = 5

    elif age <= 18:
        cost = 7
    # age 45 - 55
    elif age >= 45 and age <= 55:
        cost = 0
    else:
        cost = 12

    photo = input("Do you want a photo or not?(yes,no) ")

    if photo == "yes":
        cost += 3

    print(f"Pleasy pay ${cost}.")
else:
    print("Sorry, you have to grow taller before you can ride;.")
```

#### example3: roller coaster ticket
```
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("How old are you? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride;.")
```
