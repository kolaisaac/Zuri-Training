#import datetime 
import datetime
import random

# User Database
user_database = {
    'Seyi': 'passwordSeyi',
    'Mike': 'passwordMike',
    'Love': 'passwordLove',
    'Seun': 'passwordSeun',
    'Bisi': 'passwordBisi',
}

# declaration of variables

# now = datetime.datetime.now() 
# name = input("What is your name? \n")
# allowedUser = ['Seyi', 'Mike', 'Love']
# allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']

# Login Function

def login():
    now = datetime.datetime.now()
    name = input("What is your name? \n")
    password = input("Your password? \n")
    if(name in user_database and password == user_database[name]):
        # Welcome message
        # Display of current Date and Time

        print ("Welcome %s" % name)
        print ("Current date and time: %s" % now.strftime("%Y-%m-%d %H:%M:%S") )
    else:
        print('Password or Username Incorrect, Please try again!')


def bankOperations():
    
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')

    selectedOption = int(input('Please select an option:'))

    if (selectedOption == 1):
        print('You selected %s' % selectedOption)
        amountToWithdraw = int(input('How much would you like to withdraw:'))
        bankOperations()
        
    elif (selectedOption == 2):
        print('You selected %s' % selectedOption)
        amountToDeposit = int(input('How much would you like to deposit?:'))
        bankOperations()
        
    elif (selectedOption == 3):
        print('You selected %s' % selectedOption)
        reportComplaint = input('What issue will you like to report?:')
        bankOperations()

    elif (selectedOption == 4):
        print('Thank you for using our service')
        exit()
        
    else:
        print('Invalid Option Selected, please try again')

print('Welcome, What would you like to do?')
print('1. Login')
print('2. Register')

actionSelect = int(input('Select an option \n'))

if(actionSelect == 1):
    isLoginSuccessful = False

    while isLoginSuccessful == False:
        isLoginSuccessful = login()

    bankOperations()

else:
    print('Login failed, Username or Password incorrect. Please try again!')