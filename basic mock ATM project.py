
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
user_database = {
    2015639512: ["Seun", 'Isaac', 'seunisaac@gmail.com', 'password', 2050]
}
# declaration of variables

# now = datetime.datetime.now() 
# name = input("What is your name? \n")
# allowedUser = ['Seyi', 'Mike', 'Love']
# allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']

# Initialization function

def init():

    print("Welcome to BLEST Bank")

    have_account = int(input("Do you have account with us: 1 (Yes) 2 (No) \n"))


    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print("You have selected invalid option")
        init()

# Login Function    

def login():
 
    print("***** Login to your Account ******")
    account_number_from_user = input("What is your Account Number? \n")

    valid_account_number = account_number_validation(account_number_from_user)

    if valid_account_number:

        password = input("Your password? \n")

        for account_number, user_details in user_database.items():
            if account_number == int(account_number_from_user):
                if user_details[3] == password:
                    bank_operations(user_details)
                    
        print('Password or Username Incorrect, Please try again!')

        login()
    else:
        init()

def account_number_validation(account_number):
    # Chect if inputed account_number exit
    if account_number:

        if len(str(account_number)) == 10:

            try:
                int(account_number)
                return True
            except ValueError:
                print("Invalid Account Number, Account number should be an integer")
                return False
            except TypeError:
                print("Invalid account type")
                return False

        else:
            print("Account Number cannot be less than or more than 10 digits")
            return False
    else:
        print("Account number is a required field")
        return False

def register():
    print("***** Register for a new Account *****")

    now = datetime.datetime.now()

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your lastname? \n")
    password = input("Type the password you want \n")

    account_number = generate_account_number()

    user_database[account_number] = [first_name, last_name, email, password]

    print("Your Account has been created successfully")
    print(" == === ==== ====== ==== === ==")
    print("Your Account number is: %d" % account_number)
    print("Keep it Safe \n")
    print ("Current date and time: %s" % now.strftime("%Y-%m-%d %H:%M:%S") )
    print(" == === ==== ====== ==== === ==")

    login()

def bank_operations(user):
    print('Welcome %s %s ' % (user[0], user[1]))

    # print('These are the available options:')
    # print('1. Withdrawal')
    # print('2. Cash Deposit')
    # print('3. Complaint')
    # print('4. Logout')

    selectedOption = int(input('Please select an option: (1) Deposit (2) Withdraw (3) Logout (4) Exit \n'))

    if selectedOption == 1:
        
        deposit_operation()

    elif selectedOption == 2:
       
       withdrawal_operation()
        
    elif selectedOption == 3:
        
        logout()

    elif selectedOption == 4:
        print('Thank you for using our service \n')
        exit()
        
    else:
        print('Invalid Option Selected, please try again')
        bank_operations(user)

def generate_account_number():

    #Sprint("Generating Account Number")
    return random.randrange(1111111111, 9999999999)
#2print("Your Account Number is %s" % generateAccountNumber())


def withdrawal_operation():
    print('Withdrawal')

def deposit_operation():
    print('Deposit Operations')

def current_balance(user_details):
    return user_details[4]


def logout():
    login()

init()



