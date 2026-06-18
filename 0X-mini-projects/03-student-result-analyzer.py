# Exercise - 3

'''
Take:

Student Name
Marks
Attendance %

Conditions:
Attendance < 75%
    Not Eligible for Exam

Otherwise:

90+  Grade A
75+  Grade B
60+  Grade C
Below 60 Grade D
'''

#=========================================================================================================

# Solution: 

print('Student Information'.center(40, '-'))

name = input('Enter Student Name: ')
marks = float(input('Enter Marks: '))
attendence = int(input('Enter Attendence(in %): '))


print('RESULT'.center(40, '-'))
if (attendence > 75):
    if (marks > 90):
        print(f'Name: {name}')
        print('Grade: A')
        print('Status: Pass')
    elif (marks > 75):
        print(f'Name: {name}')
        print('Grade: B')
        print('Status: Pass')
    elif (marks > 60):
        print(f'Name: {name}')
        print('Grade: C')
        print('Status: Pass')
    else:
        print(f'Name: {name}')
        print('Grade: D')
        print('Status: Pass')
else:
    print(f'{name} is Not Eligible for Examination')
    print('Status: Fail')
