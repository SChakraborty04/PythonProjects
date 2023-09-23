import os

print("Welcome to KIIT Banking System.")
print("Are you 1>Admin or 2>User?")
choice = int(input("Please enter your choice "))
if (choice == 1):
    n = 3
    while (n != 0):
        password = input("Enter Admin Password ")
        if (password == "KiitAdmin"):
            os.system('Admin.py')
            break
        else:
            n = n - 1
            print("The password is not Admin password.Tries remain.", n)
if (choice == 2):
    os.system('User.py')
else:
    exit(0)
