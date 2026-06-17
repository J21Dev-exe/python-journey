# Conditional Statements
Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate `True or False`. If the expression evaluates to `False`, then the program execution follows a different path than it would have if the expression had evaluated to `True`.

Based on this, the conditional statements are further classified into following types:
- if statement
- if-else statement
- if-else-elif statement
- nested if-else-elif statement

## if Statement
It evaluates `True`, when the condition is met.

**Example:**
```bash
jersey = 'India'
if (jersey == 'India'):         # if statement
    print('Indian Jersey')
```
**Output:**
```bash
Indian Jersey
```

## if-else Statement

### if the expression evaluates True:
Executes the block of code inside if statement. After execution return to the code out of the if-else block.

### if the expression evaluates False:
Executes the block of code inside else statement. After execution return to the code out of the if-else block.


**Example:**
```bash
applePrice = 210
budget = 200
if (applePrice <= budget):                          # if statement 
    print('Alexa, add 1 kg Apples to the cart.')
else:                                               # else statement
    print('Alexa, do not add Apples to the cart.')
```
**Output:**
```bash
Alexa, do not add Apples to the cart.
```

## if-else-elif Statement
Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement.

Execute the block of code inside the if statement if the initial expression evaluates to `True`. After execution, return to the code of the if-else-elif block.

Execute the block of code inside the first elif statement if the expression inside it evaluates `True`. After execution, return to the code of the if-else-elif block.

Execute the block of code inside the second elif statement if the expression inside it evaluates `True`. After execution, return to the code of the if-else-elif block.
.
.
.
Execute the block of code inside the nth elif statement if the expression inside it evaluates `True`. After execution, return to the code of the if-else-elif block.

Execute the block of code inside the else statement if none of the expression evaluates to `True`. After execution, return to the code of the if-else-elif block.

**Example:**
```bash
num = 0
if (num < 0):                           # if statement
    print("Number is negative.")
elif (num == 0):                        # elif statement
    print("Number is Zero.")
else:                                   # else statement
    print("Number is positive.")
```
**Output:**
```bash
Number is Zero.
```

## nested if-else-elif Statement
We can use if, if-else, elif atatementss inside other `if` statement as well.

**Example:**
```bash
num = 10

if (num < 0):                                   # if statement
    print("Number is negative.")
elif (num > 0):                                 # nested if-else-elif statement
    if (num <= 10):
        print("Number is between 1-10.")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20.")
    else:
        print("Number is greater than 20.")
else:                                           # else statement
    print("Number is Zero.")
```
**Output:**
```bash
Number is between 11-20.
```