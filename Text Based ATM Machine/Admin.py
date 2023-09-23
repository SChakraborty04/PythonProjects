import string
import random
import sys
import re

cust_profile = open("Customer_profile\cust_profile.txt","a+")

k = 1
temp =()
address = ()

def randompassword():
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  size = random.randint(4, 4)
  return ''.join(random.choice(chars) for x in range(size))

print("Welcome to KIIT BANKING SYSTEM Admin Panel")
print('This is Admin account.')

choice = int(input('Enter 0 to proceed, 1 to terminate:'))

while True:
    if(choice == 0):
      print('What would you like to do today? \n1.Create Customer profile\n2. View customer transaction history\n3. Search customer profile\n')
      choice = int(input('Enter your choice:'))
      if (choice == 1):
        firstname = input('Enter First Name:')
        lastname = input('Enter Last Name:')
        address = input('Enter Address:')
        number = input("Enter your phone number {Only 10 digit numbers are allowed allowed!}: ")
        if not re.match("^[0-9]*$", number):
            print("Error! Only numbers allowed!")
            sys.exit()
        elif len(number) > 10 or len(number) < 10:
            print("Error! Only 10 digits are allowed allowed!")
            sys.exit()
        username = lastname[0:2] + firstname
        username_integer = username + str(k)
        with open ('Customer_profile\cust_profile.txt','r') as f:
          data = f.read()
          if (username not in data):
              temp = username
              temp2 = randompassword()
              cust_profile.write('Username:'+username+'\t'+'Password:'+temp2+'\t'+'First Name:'+firstname+'\t'+'Last Name:'+ lastname+'\t'+'Address:'+ address+"\t"+'Phone number:'+ number+"\n")
              print("\nCreated username is:",temp,'and password is',temp2,'\n')
          else:
              k = k + 1
              temp = username_integer
              temp2 = randompassword()
              cust_profile.write('Username:'+username_integer+'\t'+'Password:'+temp2+'First Name:'+firstname+'\t'+'Last Name:'+ lastname+'\t'+'Address:'+ address+"\t"+'Phone number:'+ number+"\n")
              print('\nCreated username is:',temp,'and password is',temp2,"\n")
            
      elif(choice == 2):
        username = input('Enter username that you would like to view:')
        transactionfilename =  username +'_transactionhistory.txt'
        transactionfile = open("trans_fold/"+transactionfilename,'a')
        with open ("trans_fold/"+transactionfilename,'r') as f:
          f.seek(0)
          if f.read(1):
            print(f.read())
            break
          else:
            print('There is no transaction history for this customer')
            break
      elif(choice == 3):
        data = input('Please enter customer detail to search:')
        file = open ('Customer_profile\cust_profile.txt')
        for line in file:
          line = line.rstrip()
          if data in line:
            print(line)
        break

      else:
        print('Wrong Option')
        choice = int(input('Enter 0 to proceed, 1 to terminate:'))

    elif (choice == 1):
        print('Goodbye')
        break
    else:
        print('Wrong option')
        choice = int(input('Enter 0 to proceed, 1 to terminate:'))

cust_profile.close()


