# Question 11:
'''
Using input(), create this:
-------------------
Student Information
-------------------

Name    : Jeevan
Age     : 20
College : BJB
'''

#===================================
# Solution:
print('11.')

name = input("Enter your name: ")
age = int(input('Enter your age: '))
college = input('Enter your college: ')

print('-' * 20)
print('Student Information')
print('-' * 20)

print(f'{'Name':<7}: {name}')
print(f'{'Age':<7}: {age}')
print(f'{'College':<7}: {college}')