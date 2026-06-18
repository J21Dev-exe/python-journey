# Question 1:
''' 
Input a character.

Print:

Vowel
or
Consonant
'''

#===================================
# Solution:
print('1.')

# Print Vowel or Consonant
letter = input('Enter the letter: ')

match letter:
    case 'a' | 'e' | 'i' | 'o' | 'u':               # Vowel
        print(f'{letter} is Vowel.')
    case _:                                         # Consonant
        print(f'{letter} is Consonant.')

#===================================