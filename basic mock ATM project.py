
import datetime
import random
import string

# User Database
# user_database = {
#     'Seyi': 'passwordSeyi',
#     'Mike': 'passwordMike',
#     'Love': 'passwordLove',
#     'Seun': 'passwordSeun',
#     'Bisi': 'passwordBisi',
# }
user_database = {}
# declaration of variables

# now = datetime.datetime.now() 
# name = input("What is your name? \n")
# allowedUser = ['Seyi', 'Mike', 'Love']
# allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']

# Login Function

def init():

    isValidOptionSelected = False
    print("Welcome to BLEST Bank")

    while isValidOptionSelected == False:

        haveAccount = int(input("Do you have account with us: 1 (Yes) 2 (No) \n"))


        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            register()
        else:
            print("You have selected invalid option")

    

def login():
 
    print("Login to your Account")
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

    bankOperations()


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

def generateAccountNumber():

    print("Generating Account Number")
    return(''.join(random.choices(string.digits, k=10)))
#2print("Your Account Number is %s" % generateAccountNumber())

#  
def register():
    print("***** Register for a new Account *****")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your lastname? \n")
    password = input("Type the password you want \n")

    accountNumber = generateAccountNumber()

    user_database[accountNumber] = [first_name, last_name, email, password]

    print("Your Account has been created successfully")

    login()


init()



