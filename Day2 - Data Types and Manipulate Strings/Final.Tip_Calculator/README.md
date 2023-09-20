## Instructions
* You give total cost. 
* and tip that you should pay.
* and number of people 

I tell you how much each person should pay.

Input:
```
Welcome to the tip calculator.
What was the total bill? $124.56
What percentage tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7
```

Output:
```commandline
Each person should pay: $19.93
```

## Hint
1. number / 100 => give us percentage
2. round() doesnt show last zero. ex: round(10.6000, 2) => 10.6  - but we want float output with 2 decimal points like 10.60
so we use `"{:.2f}".format(10.600000)`