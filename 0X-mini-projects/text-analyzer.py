# Exercise - 2

'''
Create a Text Analyzer.
'''

#=========================================================================================================

# Solution: 

text = 'I love Python Programming'                          # Text to be analyzed

print('Text Analyzer'.center(45, '-'), '\n')
print(f'{'Total Characters':<17}:{len(text)}')              # Total Character
print(f'{'Total Words':<17}:{len(text.split())}')           # Total Words
print(f'{'Capitalize':<17}:{text.capitalize()}')            # Convert - Capitalize
print(f'{'Upper Case':<17}:{text.upper()}')                 # Convert - Upper Case
print(f'{'Lower Case':<17}:{text.lower()}')                 # Convert - Lower Case
print(f'{'Swap Case':<17}:{text.swapcase()}')               # Convert - Swap Case
print(f'{'Title':<17}:{text.title()}')                      # Convert - Title
print(f'{'Starts with I':<17}:{text.startswith('I')}')      # Starts with I
print(f'{'Ends with g':<17}:{text.endswith('g')}')          # Ends with g