# Loops in Python
Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this, loops are further classified into following types:
- 1. For loop
- 2. While loop
- 3. Nested loop

## For Loop
The `for` loop can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

**Example: Iterting over a string**
```bash
name = 'Jeevan'
for i in name:
    print (i, end=', ')
```
**Output:**
```bash
J, e, e, v, a, n, 
```
---

**Example: Iterting over a list**
```bash
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print (color)
```
**Output:**
```bash
Red
Green
Blue
Yellow
```
---
**Example: Iterting over a tuples**
```bash
fruits = ("apple", "banana", "mango", "orange")
for fruit in fruits:
    print (fruit)
```
**Output:**
```bash
Red
Green
Blue
Yellow
```
---
**Example: Iterting over a set**
```bash
animals = {"dog", "lion", "snake", "cat"}
for animal in animals:
    print (animal)
```
**Output:**
```bash
snake
lion
dog
cat
```
---
**Example: Iterting over a dictionary**
```bash
student_scores = {
    'Jeevan' : 20,
    'Vivek' : 18,
    'Priyansu' : 25
}

for student, score in student_scores.items():
    print(f'{student}:{score}')
```
**Output:**
```bash
'Jeevan': 20,
'Vivek': 18,
'Priyansu': 25
```
---

### range()
What if we don't want to iterate over a sequence?
What if we want to use for loop for a specific number of time?

Here, we can use the range() function.

**Example**
```bash
for k in range(5):
    print(k)
```
**Output:**
```bash
0
1
2
3
4
```
Here, we can see that the loop starts from 0 by default and increments at each iteration.

But we can also, loop over a specific range.

**Example**
```bash
for k in range(4, 9):
    print(k)
```
**Output:**
```bash
4
5
6
7
8
```
`Note`: There are three parameters for the range():

**Syntax**
```bash
for x in range(exp1, exp2, exp3):
    print(x)
```

The third parameter is used when we need to print statement by jumping or skipping them.

**Example**
```bash
for k in range(4, 9, 2):
    print(k)
```
**Output:**
```bash
4
6
8
```

## While Loop
As the name suggests, while loops execute statements while the condition is `True`. As soon as the condition becomes `False`, the interpreter comes out of the while loop.

**Example**
```bash
count = 5
while (count > 0):
    print(count)
    count = count -1
```
**Output:**
```bash
5
4
3
2
1
```
Here, the count variable is set to 5 which decrements after each iteration. Depending upon the while loop condition, we need to either increment or decrement the counter variable(the variable count, in our case) or the loop will continue forever.

### Else with While Loop
We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.

**Example**
```bash
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('Counter is 0')
```
**Output:**
```bash
5
4
3
2
1
Counter is 0
```

## Do-While Loop in Python
do..while is a loop in which a set of instructions will execute at least once(irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.

### How to emulate do while loop in Python?
To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.

The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true.

**Example**
```bash
while True:
    number = int(input('Enter a positive number: '))
    print(number)
    if not number > 0:
        break
```
**Output:**
```bash
Enter a positive number: 1
1
Enter a positive number: 4
4
Enter a positive number: -1
-1
```

## Break Statement
The break statement enables a program to skip over a part of the code. A break statement terminatesthe very loop it lies within.

**Example**
```bash
for i in range(1, 101, 1):
    print(i, end = " ")
    if(i==50):
        break
    else:
        print("Mississippi")
print('Thank You')
```
**Output:**
```bash
1 Mississippi
2 Mississippi
3 Mississippi
4 Mississippi
5 Mississippi
.
.
.
50 Mississippi
```

## Continue Statement
The continue statement skips the rest of the loop statements and causes the next iteration to occur.

**Example**
```bash
for i in [2,3,4,6,8,0]:
    if (i % 2 != 0):
        continue
    print(i)
```
**Output:**
```bash
2
4
6
8
0
```