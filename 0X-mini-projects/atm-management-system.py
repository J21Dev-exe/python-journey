# Exercise - 4

'''
Input:

1 - Balance
2 - Withdraw
3 - Deposit

Print corresponding option.
'''

#=========================================================================================================

# Solution: 

print('ATM'.center(40, '-'))

print('\n1. Check Balance\n2. Withdraw\n3. Deposit\n')

option = int(input('What do you want to do: '))

# default balance
balance = 2000
amount1 = 0
amount2 = 0

match option:
    case 1:                                                                     # Check balance
        print(f'Your balance is: ₹{balance}')
        
    case 2:                                                                     # Withdraw amount
        wd_balance = int(input('The amount you want to withdraw: ₹'))
        
        if balance > wd_balance:                                                # if condition - valid transaction
            amount1 = balance - wd_balance
            print(f'\nAmount withdrawn: ₹{wd_balance}')                         # display amount - withdrawn
            print('Successfully Withdrawn!')
        else:                                                                   # else condition - invalid transaction
            print("\nYou don't have that much in your account")
        
        # Display Balance
        key = input('\nDo you want to display balance? ').lower()
          
        if key == 'yes':                                                        # if condition - display balance 
            print(f'\nBalance: ₹{amount1}')
            print('Transaction successful !')
            print("\nYou're welcome\nThank You! for visiting")
        else:                                                                   # else condition - exit
            print("\nYou're welcome\nThank You! for visiting")
            
    case 3:                                                                     # Deposit amount
        dp_balance = int(input('The amount you want to deposit: ₹'))
        amount2 = balance + dp_balance
        
        print(f'\nAmount deposited: ₹{dp_balance}')                             # display amount - deposit
        print('Successfully Deposited!')
        
        # Display Balance
        key = input('\nDo you want to display balance? ').lower()
        
        if key == 'yes':                                                        # if condition - display balance
            print(f'\nBalance: ₹{amount2}')
            print('Transaction successful !')
            print("\nYou're welcome\nThank You! for visiting")
        else:                                                                   # else condition - exit
            print("\nYou're welcome\nThank You! for visiting")
            
    case _:                                                                     # Default case
        print('Invalid Option!')