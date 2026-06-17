# Question 7:
''' 
Check whether a number is divisible by given number.
'''

#===================================
# Solution:
print('7.')

# Print whether divisible or not
value = int(input('Enter a number: '))
number = int(input('Number to check divisibility: '))

if (value % number == 0):                           # if condition - is divisible
    print(f'{value} is divisible by {number}')
else:                                               # else condition - isn't divisible
    print(f'{value} is not divisible by {number}')

#===================================