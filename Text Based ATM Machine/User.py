import os
import datetime


def depositcash():
    deposit_amount = float(input('Please enter amount to be deposited:'))
    username = input('Please enter username:')
    filename = "balance_" + username + '.txt'
    transactionfilename = username + '_transactionhistory.txt'
    transactionfile = open("trans_fold/" + transactionfilename, 'a')
    file = open("balance/" + filename, 'a')
    balance = 0
    new_balance = 0
    with open("balance/" + filename, 'r') as file:
        for i in file:
            balance = float(i)
    with open("balance/" + filename, 'w+') as file2:
        new_balance = balance + deposit_amount
        new_balance = str(new_balance)
        file2.write(new_balance)
        print('Your new balance is:', new_balance)
    with open("trans_fold/" + transactionfilename, 'a') as file3:
        balance = str(balance)
        deposit_amount = str(deposit_amount)
        file3.write(str(datetime.datetime.now()))
        file3.write(
            '\nPrevious balance: ' + balance + '. Deposit amount is:' + deposit_amount + '. New balance:' + new_balance + '\n')

    file.close()
    return 1


def withdrawalcash():
    withdrawn_amount = float(input('Please enter amount to be withdrawn:'))
    username = input('Please enter username:')
    filename = "balance_" + username + '.txt'
    transactionfilename = username + '_transactionhistory.txt'
    transactionfile = open("trans_fold/" + transactionfilename, 'a')
    file = open("balance/" + filename, 'a')
    balance = 0
    new_balance = 0

    with open("balance/" + filename, 'r') as file:
        for i in file:
            balance = float(i)
    with open("balance/" + filename, 'w+') as file2:
        if withdrawn_amount > balance:
            print('You have insufficient balance. Your balance is:', balance)


        else:
            new_balance = balance - withdrawn_amount
            new_balance = str(new_balance)
            file2.write(new_balance)
            print('Your new balance is:', new_balance)
            with open("trans_fold/" + transactionfilename, 'a') as file3:
                balance = str(balance)
                withdrawn_amount = str(withdrawn_amount)
                file3.write(str(datetime.datetime.now()))
                file3.write(
                    '\nPrevious balance: ' + balance + '. Withdrawn amount is:' + withdrawn_amount + '. New balance:' + new_balance + '\n')
    file.close()
    return 1


def balance():
    username = input('Please enter username:')
    filename = 'balance_' + username + '.txt'
    file = open("balance/" + filename, 'a')
    with open("balance/" + filename, 'r') as file:
        for i in file:
            balance = float(i)
        file.seek(0)
        if file.read(1):
            print('Your balance is:', balance)

        else:
            print('You have no balance left.')
    file.close()
    return 1


print("Welcome to KIIT ATM user system")
print('Please login to proceed.')

cust_profile = open('Customer_profile\cust_profile.txt', 'r')
data = cust_profile.read()
username = input('Please enter your username:')
password = input('Please enter your password:')
if username in data and password in data:
    print('Login Successful')
    opt = int(input('Do you want to continue? Enter 0 to continue, 1 to Terminate:'))
    while True:
        if (opt == 0):
            while (1):
                print(
                    'What would you like to do today? \n1. Deposit Money\n2. Withdraw Money\n3. Check Balance\n4. Check Transaction History')
                opt = int(input('Enter your choice:'))
                if (opt == 1):
                    depositcash()
                elif (opt == 2):
                    withdrawalcash()
                elif (opt == 3):
                    balance()
                elif (opt == 4):
                    transactionfilename = username + '_transactionhistory.txt'
                    transactionfile = open("trans_fold/" + transactionfilename, 'a')
                    with open("trans_fold/" + transactionfilename, 'r') as f:
                        f.seek(0)
                        if f.read(1):
                            print(f.read())
                            f.close()
                            break
                        else:
                            print('There is no transaction history.')
                            f.close()
                            break
                opt = int(input('Do you want to continue? Select 0 to Continue, 1 to Terminate:'))

        elif (opt == 1):
            print('Goodbye')
            break
        else:
            opt = int(input('Do you want to continue? Select 0 to Continue, 1 to Terminate.'))
