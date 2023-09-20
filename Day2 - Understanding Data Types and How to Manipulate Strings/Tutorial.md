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
* round()
  * به سمت بالا رند میکنه 
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