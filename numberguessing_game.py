import random

print("Welcome to Number Guessing Game!!")
que = input("Do you want to play? ")
if que.lower() != "yes":
    print(":( Come again soon")
    quit()

print("Lets Play")
top_of_range = input("Enter the end number of range")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range<=0:
        print("Next time please put a number greater than 0")
        quit()
else:
    print("You need to type a digit")
    quit()

score = 0
while True:
    num = int(input("Your number: "))
    #r = random.randrange(0,10)
    r = random.randint(0,top_of_range)
    print("Computer's Number: ",r)
    if(num==r):
        print("Guessed it in :",score," chances.")
        break
    print("Keep typing: ")
    score += 1    
