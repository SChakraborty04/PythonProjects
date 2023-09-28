from cryptography.fernet import Fernet

'''def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as kf:
        kf.write(key)
'''
def read_key():
    file = open("key.key","rb")
    key=file.read()
    file.close()
    return key
masterpass=input("Enter the masterpassword")
'''   masterpass is "kiit"  '''
key= read_key()+masterpass.encode()
fer=Fernet(key)

def add():
    account=input("Enter your account name: ")
    passw=input("Enter account password: ")
    with open('password.txt', 'a') as f:
        f.write(account+"|"+fer.encrypt(passw.encode()).decode()+"\n")
def view():
    with open('password.txt', 'r') as f:
        for lines in f.readlines():
            data=lines.rstrip()
            user,password=data.split("|")
            print(f"Username: {user}\tPassword: {fer.decrypt(password.encode()).decode()}\n")

while True:
    c=input("Would you like to add a new password or view existing password?(Type add/view. Type q to QUIT): ")

    if c=="q":
        break
    elif c=="view":
        view()
    elif c=="add":
        add()
    else:
        print("Invalid input please try again!")
