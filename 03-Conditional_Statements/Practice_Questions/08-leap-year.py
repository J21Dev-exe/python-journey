# Question 8:
''' 
Take a year and determine whether it is a leap year.
'''

#===================================
# Solution:
print('8.')

# Print whether Leap year or not
year = int(input('Enter a Year: '))

if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):      # if condition - leap year
    print(f"{year} is a leap year")
else:                                                                   # else condition - not a leap year
    print(f"{year} isn't a leap year")

#===================================