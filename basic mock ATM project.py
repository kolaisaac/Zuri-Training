#import datetime 
import datetime

# declaration of variables

now = datetime.datetime.now() 
name = input("What is your name? \n")
allowedUser = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']

if(name in allowedUser):
    password = input("Your password? \n")
    userId = allowedUser.index(name)

    if(password == allowedPassword[userId]):

        # Welcome message
        # Display of current Date and Time

        print('Welcome %s' % name)
        print ("Current date and time: %s" % now.strftime("%Y-%m-%d %H:%M:%S") )
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option:'))

        if (selectedOption == 1):
            print('You selected %s' % selectedOption)
            amountToWithdraw = int(input('How much would you like to withdraw:'))
            print('take your cash')
        elif (selectedOption == 2):
            print('You selected %s' % selectedOption)
            amountToDeposit = int(input('How much would you like to deposit?:'))
            print('current balance')
        elif (selectedOption == 3):
            print('You selected %s' % selectedOption)
            reportComplaint = input('What issue will you like to report?:')
            print('Thank you for contacting us')
        else:
            print('Invalid Option Selected, please try again')
    else:
        print('Password Incorrect, Please try again')

else:
    print('Name not found, please try again')

