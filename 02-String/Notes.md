# What are Strings?
In Python, anything that you enclose between single or double quotation marks is considered as a `string`. A string is essentially a sequence or array of textual data. Strings are used when working with unicode characters.

**Example:**
```bash
name = "Harry"
print("Hello, " + name)
```
**Output:**
```bash
Hello, Harry
```
*Note*: It doesn't matter whether you enclose your strings in single or double quotes, the output remains the same.

Sometimes, the user might need to put quotation marks in between the strings. Example, consider the sentence: *He said, "I want to eat an apple".*

How will you print this statement inn Python? : `He said, "I want to eat an apple".` We will definitely use single quotes for our convenience

```bash
print('He said, "I want to eat an apple".')
```

## Multiline Strings
If our string has multiple lines, we can create them like this:
```bash
a = '''
Lorem ipsum dolar sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''
print(a)
```

## Accessing Characters of a String
In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
Square brackets can be used to access elements of the string.
```bash
print(name[0])
print(name[1])
```

## Looping through the String
We can loop through strings using a for loop like this:
```bash
for character in name:
    print(character)
```
Above code prints all the characters in the string name one by one!

## String Slicing & Operations on String
### Length of a String

We can find the length of a string using len() function.
**Example:**
```bash
fruit = "Mango"
len1 = len(fruit)
print('Mango is a', len1, 'letter word.')
```
**Output:**
```bash
Mango is a 5 letter word
```

## String as an array
A string is essentially a sequence of characters also called an array. Thus, we can access the elements of this array.

**Example:**
```bash
pie = "ApplePie"
print(pie[:5])
print(pie[6]) #Returns character at specified index
```
**Output:**
```bash
pple
i
```
*Note*: This method of specifying the start and end index to specify a part of a string is called slicing.

**Slicing Example:**
```bash
pie = "ApplePie"
print(pie[:5])   # Slicing from start
print(pie[5:])   # Slicing till end
print(pie[2:6])  # Slicing in between
print(pie[-8:])  # Slicing using negative index
```
**Output:**
```bash
Apple
Pie
pleP
ApplePie
```

## Loop through a String
Strings are arrays and arrays are iterable. Thus we can loop through strings.

**Example:**
```bash
alphabets = 'ABCDE'
for i in alphabets:
    prinnt(i)
```
**Output:**
```bash
A
B
C
D
E
```

## String methods
Python provides a set of built-in methods that we can use to alter and modify the strings.

### upper():
The upper() method converts a string to upper case.

**Example:**
```bash
str1 = 'AbcDEfghIJ'
print(str1.upper())
```
**Output:**
```bash
ABCDEFGHIJ
```

### lower():
The lower() method converts a string to lower case.

**Example:**
```bash
str1 = 'AbcDEfghIJ'
print(str1.lower())
```
**Output:**
```bash
abcdefghij
```

### swapcase():
The swapcase() method changes the character casing of the string. Upper case are converted to lower case and vise-versa.

**Example:**
```bash
str1 = 'Python is a Interpreted Language'
print(str1.swapcase())
```
**Output:**
```bash
pYTHON IS A iNTERPRETED lANGUAGE
```

### strip():
The strip() method removes any white spaces before and after the string.

**Example:**
```bash
str2 = 'Silver Spoon '
print(str2.strip)
```
**Output:**
```bash
Silver Spoon
```

### rstrip():
The rstrip() removes any trailing characters.

**Example:**
```bash
str3 = 'Hello !!!'
print(str3.rstrip('!'))
```
**Output:**
```bash
Hello
```

### replace()
The replace() method replaces all occurances of a string with another string.

**Example:**
```bash
str2 = 'Silver Spoon'
print(str2.replace('Sp', 'M'))
```
**Output:**
```bash
Silver Moon
```

### split()
The split() method splits the given string at the specified instance and returns the separated strings as list items.

**Example:**
```bash
str2 = 'Silver Spoon'
print(str2.split(" ")) # Splits the string at the whitespaces " ".
```
**Output:**
```bash
['Silver', 'Spoon']
```

### capitalize()
The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

**Example:**
```bash
str1 = 'hello'
capStr1 = str1.capitalize()
print(capStr1)

str2 = 'hello WorlD'
capStr2 = str2.capitalize()
print(capStr2)
```
**Output:**
```bash
Hello
Hello world
```

### center()
The center() method aligns the string to the center as per the parameters given by the user.

**Example:**
```bash
str1 = 'Welcome to the console!!!'
print(str1.center(50))
```
**Output:**
```bash
                    Welcome to the console!!! 
```
We can also provide padding character. It will fill the rest of the fill characters provided by the user.

**Example:**
```bash
str1 = 'Welcome to the console!!!'
print(str1.center(50, '.'))
```
**Output:**
```bash
....................Welcome to the console!!!.................... 
```

### count()
The count() method returns the number of times the given value has occured within the given string.

**Example:**
```bash
str2 = 'Abracadabra'
countStr = str2.count('a')
print(countStr)
```
**Output:**
```bash
4
```

### endswith()
The endswith() method checks if the string ends with a given value. If yes, then return True, or else return False.

**Example:**
```bash
str1 = 'Welcome to the console !!!'
print(str1.endswith('!!!'))
```
**Output:**
```bash
True
```
We can even also check for a value in-between the string by providing start and end index positions.

**Example:**
```bash
str1 = 'Welcome to the console !!!'
print(str1.endswith('to', 4, 10))
```
**Output:**
```bash
True
```
### startswith()
The startswith() method checks if the string starts with a given value. If yes, then return True, or else return False.

**Example:**
```bash
str1 = 'Python is an interpreted language'
print(str1.startswith('Python'))
```
**Output:**
```bash
True
```

### find()
The find() method searches for the first occurance of the given value and returns the index where it is present. If the given value is absent from the string then return -1.

**Example:**
```bash
str1 = 'He's name is Dan. He is an honest man.'
print(str1.find('is'))
```
**Output:**
```bash
10
```
As we can see this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

**Example:**
```bash
str1 = 'He's name is Dan. He is an honest man.'
print(str1.find('Daniel'))
```
**Output:**
```bash
-1
```

### index()
The index() method searches for the first occurance of the given value and returns the index whereas it is present. If given value is absent from the string then raise an exception.

**Example:**
```bash
str1 = 'He's name is Dan. He is an honest man.'
print(str1.index('Dan'))
```
**Output:**
```bash
13
```
As we can see, this method is somewhat similar to the find() method. The major difference being that index() raise an exception if value is absent whereas find() does not.

**Example:**
```bash
str1 = 'He's name is Dan. He is an honest man.'
print(str1.find('Daniel'))
```
**Output:**
```bash
ValueError: substring not found
```

### isalnum()
The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other character or punctuations are present, then it returns False.

**Example:**
```bash
str1 = 'WelcomeToTheConsole'
print(str1.isalnum())
```
**Output:**
```bash
True
```

### isalpha()
The isalpha() method returns True only if the entire string only consists of A-Z, a-z. If any other character or punctuations or numbers(0-9) are present, then it returns False.

**Example:**
```bash
str1 = 'Welcome'
print(str1.isalpha())
```
**Output:**
```bash
True
```

### islower()
The islower() method returns True, if all the characters in the string are lower case, else it returns False.

**Example:**
```bash
str1 = 'hello world'
print(str1.islower())
```
**Output:**
```bash
True
```

### isupper()
The isupper() method returns True, if all the characters in the string are upper case, else it returns False.

**Example:**
```bash
str1 = 'WORLD HEALTH ORGANIZATION'
print(str1.isupper())
```
**Output:**
```bash
True
```

### isprintable()
The isprintable() method returns True, if all the values within the given strings are printable, otherwise False.

**Example:**
```bash
str1 = 'We wish you a Merry Christmas'
print(str1.isprintable())
```
**Output:**
```bash
True
```

### isspace()
The isspace() method returs True only and only if the string contains white spaces, else returns False.

**Example:**
```bash
str1 = '        '      # Using Spacebar
print(str1.isspace())
str2 = '        '      # Using Spacebar
print(str2.isspace())
```
**Output:**
```bash
True
True
```

### istitle()
The istitle() method returns True only if the first letter of each word of the string is capitalize, else it returns False.

**Example:**
```bash
str1 = 'World Health Organization'
print(str1.istitle())
str2 = 'To kill a Mocking bird'
print(str2.istitle())
```
**Output:**
```bash
True
False
```
### title()
The title() method capitalizes each letter of the word within the string.

**Example:**
```bash
str1 = 'His name is Dan. He is an honest man.'
print(str1.title())
```
**Output:**
```bash
His Name Is Dan. He Is An Honest Man.
```
