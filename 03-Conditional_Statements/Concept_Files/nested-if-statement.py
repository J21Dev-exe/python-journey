# nested if-else statement

age = 22
citizen = True

if age >= 18:
    if citizen:
        print('Eligible to vote!')
    else:
        print('Not a citizen!')
else:
    print('Underage')