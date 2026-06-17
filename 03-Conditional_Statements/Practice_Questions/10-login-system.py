# Question 10:
''' 
Create a simple login system:
If username is correct:
    Check password

If password is correct:
    Print Login Successful

Otherwise:
    Print Wrong Password

If username is incorrect:
    Print Invalid Username
'''

#===================================
# Solution:
print('10.')

print('Credentials'.center(25, '-'),'\n')
# Print category acc to BMI
username = input('Username: ')      # Username
password = input('Password: ')      # Password

usr = 'J21'
ps_wrd = 'Zexan@21'

if (username == usr):                           # if condition - checks username
    if (password == ps_wrd):                    # if condition - checks password
        print('Login Successfull!!')
    else:
        print('Incorrect Password!')
else:
    print('Incorrect Username! TRY AGAIN!')
#===================================