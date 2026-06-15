# 1. What is Programming and Python?

## What is Programming?
Programming is a way for us to tell computers what to do. Computer is a very dumb machine and it only does what we tell it to do. Hence we learn programming and tell computers to do what we are very slow at- i.e., computation. If i ask you to calculate 5+6, you will immediately say 11. How about 23453453 x 56456?

You will start searching for a calculator or jump to a new tab to calculate the same. 

## What is Python?
- Python is a dynamically typed, general purpose programming language that supports an object-oriented programming approach as well as a functional programming approach.
- Pyhton is an intepreted and a high-level programming language.
- it was created by Guido Van Rossum in 1989.

## Features of Python?

- Python is simple and easy to understand.
- It is Intepreted and platform-independent which makes debugging very easy.
- Python is an open-source programming language.
- Python provides very big library support. Some of the popular libraries include NumPy, Tensorflow, Selenium, OpenCV, etc.
- It is possible to integrate other programming languages within python.

## What is Python used for?

- Python is used in Data Visualization to create plots and graphical representations.
- Python helps in Data Analytics to analyze and understand raw data for insights and trends.
- It is used in AI and Machine Learning to simulate human behavior and to learn from past data without hard coding.
- It is used to create web applications.
- It can be used to handle databases.
- It is used in business and accounting to perform complex mathematical operations along with quantitative and qualitative analysis.


# 2. Modules and pip in Python!

Module is like a code library which can be used to borrow the code written by somebody else in our python program. There are two types of modules in python:

1. Built-in Modules - These modules are ready to import and use and ships with the python interpreter, there is no need to install such modules explicitely.
2. External Modules - These modules are imported from a third party file or can be installed using a package manager like pip or conda. Since this code is written by someone else, we can install different versions of a same module with time.

## The pip command
It can be used as a package manage `pip` to install a python module. Let's install a module called pandas using the following command

**Install Pandas**

```bash
pip install pandas
```

## Using a module in Python(Usage)
We use the import syntax to import a module in python. Here is an example code:

```bash
import pandas

# Read and work with a file named 'words.csv'
pandas.read_csv('words.csv')
```

# 3. First Program
We can write statement and show the output in the terminal using print(), this can be done with the help of syntax:

```bash
print("Hello! World")
```

# 4. Comments, Escape sequence & Print in Python

## Python Comments
A comment is a part of the coding file that the programmer does not want to execute, rather the programmer uses it to either expalin a block of code or to avoid the execution of a specific part of code while testing.

### Single-Line Comments:
To write a comment just add a '#' at the start of the line.

**Example 1**
```bash
# This is a 'Single-Line Comment'
print("This is a print statement.")
```
**Output**
```
This is a print statement.
```
---
**Example 2**
```bash
print("Hello World !!") #Printing Hello World
```
**Output**
```
Hello World !!
```
---
**Example 3**
```bash
print("Python Program")
#print("Python Program")
```
**Output**
```
Python Program
```
---

### Multi-Line Comments:
To write multi-line comments you can use '#' at starting of each line or you can use he multiline string, i.e. " **'''** "
**Example 1: The use of "#"**
```bash
# It will execute a block of code if a specified conditionn is true.
# If the condition is false then it will execute another block of code.
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
```
**Output**
```
p is greater than 5.
```
---
**Example 2: The use of multi-line string**
```bash
'''This is an if-else statement.
It will execute a block of code if a specified conditionn is true.
If the condition is false then it will execute another block of code.'''
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
```
**Output**
```
p is greater than 5.
```
---

## Escape Sequence Characters
To insert characters that cannot be directly used in a string, we use an escape sequence character.

An escape sequence character is backslash `\` followed by the character you want to insert.

An example of a string that cannot be directly used in a string is a double quote inside a string that is surrounded by souble quotes
```bash
print("This doesn't "execute")
print("This will \"execute")
```

## More on Print Statement
The syntax of a print statement looks something like this:
```bash
print(objects(s), sep=separator, end=end, file=file, flush=flush)
```

### Other Parameters of Print Statements

1. objects(s): Any object, and as many as you like. Will be converted to string before printed.
2. sep=separator: Specify how to separate the objects, if there is more than one. Default is ''.
3. end=end: Specify what to print at the end. Default is '\n'(line feed).
4. file: An object with a write method. Default is sys.stdout

Parameters 2 to 4 are optional.

# 5. Variables and Data Types in Python

## What is a variable?
Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt, etc. Creating a variable is like creating a placeholder in memory and assigning it some value. In Python, it's as easy as writing:

**Example**
```bash
a = 1
b = True
c = "Harry"
d = None
```

These are four variables of different data types.

## What is a Data Type?
Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
In Python, we can print the type of any operator using type functions:

**Example**
```bash
a = 1
print(type(a))
b = "1"
print(type(b))
```

By default, Python provides the following built-in data types:

## 1. Numeric data: int, float, complex
- int: 3, 0, -8
- float: 7.980, -9.0, 0.000001
- complex: 6 + 2i

## 2. Text data: str
- str: "Hello World!", "Python Programming."

## 3. Boolean Data
- Boolean: True / False

## 4. Sequenced data: list, tuple
**list**: A list is an ordered collection of data with elements separated by a comma `,` and enclosed within square brackets `[]`. Lists are mutable and can modified after creation.

**Example:**
```bash
list1 = [8, 2.3, [-4, 5], ["apple", "Banana"]]
print(list1)
```
**Output:**
```bash
[8, 2.3, [-4, 5], ["apple", "Banana"]]
```

**tuple**: A tuple is an ordered collection of data with elements separated by a comma `,` and enclosed within parentheses `()`. Tuple are immutable and cannot be modified after creation.

**Example:**
```bash
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)
```
**Output:**
```bash
(("parrot", "sparrow"), ("Lion", "Tiger"))
```

## 5. Mapped data: dict
**dict**: A dictionary is an unordered collection of data containing a `key:value` pair. The `key:value` pairs are enclosed within curly brackets.

**Example:**
```bash
dict1 = {"name": "Sakshi", "age": 20, "canVote": True}
print(dict1)
```
**Output:**
```bash
{"name": "Sakshi", "age": 20, "canVote": True}
```

# 6. Operators
Python has different types of operators for different operations. To create a calculator we require arithmetic operators.

| **Operator** | **Operator Name** | **Example** |
|:-------|:------:|-------:|
| + | Addition | 15 + 7 |
| - | Subtraction | 15 - 7 |
| * | Multiplication | 15 * 7 |
| / | Division | 15 / 7 |
| % | Exponential | 15 ** 7 |
| % | Modulus | 15 % 7 |
| // | Floor Division | 15 // 7 |

**Example:**
```bash
dict1 = {"name": "Sakshi", "age": 20, "canVote": True}
print(dict1)
```
**Output:**
```bash
{"name": "Sakshi", "age": 20, "canVote": True}
```

# 7. Typecasting in Python
The conversion of one data type into the other data type is known as type casting in python or type coversion in python.

Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), tuple(), set(), list(), dict(), etc. for the type casting in Python.

## Types of Typecasting
1. Explicit Conversion
2. Implicit Conversion

### *Explicit Typecasting:*
The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirements, is known as explicit type conversion.

It can be achieved with the help of Python's built-in type conversion funcions such as int(), float(), hex(), oct(), str(), etc.

**Example: Explicit**
```bash
string = "15"
number = 7
string_number = int(string) # Throws error if the string is not a valid integer
sum = number + string_number
print("The sum of both the number is: ", sum)
```
**Output:**
```bash
The sum of both the number is: 22
```

### *Implicit Typecasting:*
Data types in Python do not have the same level, i.e. ordering of data types is not the same in Python. Some of the data types have higher-order, and some have lower order. While performing any operations on variables with different data types in Python, one of the variable's data type will be changes to the higher data type. According to the level, one data type is converted into other by the Python interpreter itself(automatically). This is called, implicit typecasting in Python.

Python converts a smaller data type to a higher data type to previous data loss.

**Example: Implicit**
```bash
# Python automatically converts a to int
a = 7
print(type(a))

# Python automatically converts b to float
b = 3.0
print(type(b))

# Pyhton automatically converts c to float as it is a float addition 
c = a + b
print(c)
print(type(c))
```
**Output:**
```bash
<class 'int'>
<class 'float'>
10
<class 'float'>
```

# 8. Taking User Input in Python
In Python, we can take user input directly by using `input()` function. This input function gives a return value as string/character hence we khave to pass that into a variable.

**Syntax:**
```bash
variable = input()
```
---
**Example:**
```bash
variable = int(input())
variable = float(input())
```
We can also display a text using input funtion. This will make input() function take user input and display a message as well

**Example:**
```bash
a = input("Enter the name: ")
print(a)
```
```
**Output:**
```bash
The sum of both the number is: 22
```