# Question 2:
''' 
Input color:

Red
Yellow
Green

Print:

Stop
Ready
Go
'''

#===================================
# Solution:
print('2.')

# Print Stop Ready Go
color = input('Enter the color: ')

match color:
    case 'red':                 # Stop
        print('Stop')
    case 'yellow':              # Ready
        print('Ready')
    case 'green':               # Go
        print('Go')
    case _:                     # Consonant
        print('Invalid Color!')

#===================================