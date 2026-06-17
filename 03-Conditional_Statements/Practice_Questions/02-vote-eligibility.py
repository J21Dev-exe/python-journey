# Question 2:
''' 
Take age as input and check whether the person is eligible to vote.
'''

#===================================
# Solution:
print('2.')

# Print Eligible or Not Eligible to vote
age = int(input('Enter age: '))

if (age >= 18):                        # if condition - adult
    print('Eligible to Vote!')
else:                                       # else condition - minor
    print('Not Eligible to Vote!')

#===================================