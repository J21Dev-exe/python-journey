# Question 3:
''' 
Input:

chrome
edge
firefox

Print:

Opening Chrome...
Opening Edge...
Opening Firefox...
'''

#===================================
# Solution:
print('3.')

# Print Stop Ready Go
browser = input('Enter Browser you want to surf: ')

match browser:
    case 'Chrome':                  # Chrome
        print('Opening Chrome...')
    case 'Edge':                    # Edge
        print('Opening Edge...')
    case 'Firefox':                 # Firefox
        print('Opening Firefox...')
    case _:                         # Invalid
        print('Invalid browser!')

#===================================