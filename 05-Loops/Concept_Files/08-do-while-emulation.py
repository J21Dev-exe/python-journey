# Do-While Loop 

while True:                                         # while condition
    option = input('Enter your choice: ').lower()   # Enter option
    if option == 'no':                              # if condition - break
        print('Thank You!')
        break
    elif option == 'yes':                           # elif condition
        print('Bring it on!')
    else:                                           # else conditon
        print('Invalid Input\nTryAgain')