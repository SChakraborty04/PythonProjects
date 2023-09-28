import random
print("Lets play a number guessing game!")
high=int(input("Enter the upperbound number(greater than 0): "))
number=random.randint(0,high+1)
tries=1
while True:
    guess = int(input(f"Enter the number that you have guessed which lies b/w 0 and {high}: "))
    if(guess==number):
        print(f"You have guessed the number in {tries} tries.\n")
        break
    else:
        print("Sorry it is not the number. Please try again.")
        tries+=1