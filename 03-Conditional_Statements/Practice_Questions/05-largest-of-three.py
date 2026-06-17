# Question 5:
''' 
Take three numbers and print the larger number.
'''

#===================================
# Solution:
print('5.')

# Print Largest of three numbers
number1 = int(input('Enter number1: '))
number2 = int(input('Enter number2: '))
number3 = int(input('Enter number3: '))

if ((number1 > number2) and (number1 > number3)):     # if condition - Num1 largest
    print(f'{number1}(number1) is largest')
elif ((number2 > number1) and (number2 > number3)):   # elif condition - Num2 largest
    print(f'{number2}(number2) is largest')
else:                                                 # else condition - Num3 largest
    print(f'{number3}(number3) is largest')

#===================================