# Question 6:
''' 
Take marks and print:
90+  → Grade A
75+  → Grade B
60+  → Grade C
Below 60 → Grade D
'''

#===================================
# Solution:
print('6.')

# Print Grade on the basis of marks
mark = int(input('Enter mark: '))

if mark >= 90:          # if condition - Grade A
    print('Grade A')
elif mark >= 75:        # elif condition - Grade B
    print('Grade B')
elif mark >= 60:        # elif condition - Grade C
    print('Grade C')
else:                   # else condition - Grade D
    print('Grade D')

#===================================