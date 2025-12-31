import random

comp_score = 0
your_score = 0

options = ["r","p","s"]
print("Type R for Rock/ P for Paper/S for Scissors/ Q for Quitting the game")
while True:
    urinput = input("Enter your option: ")
    if urinput.lower() == "q":
        print("Your Score: ",your_score," Computer Score: ",comp_score)
        if your_score>comp_score:
            print("You Win!")
        elif your_score == 0 and comp_score == 0:
            print("No Score Yet")
        elif your_score == comp_score :
            print("It's a Draw")    
        else:
            print("Computer Wins")        
        break

    if urinput.lower() not in options :
        print("Please Enter Correct Alphabet")
        continue
    
    num  = random.randint(0,2)
    #rock: 0, paper:1, scissor:2
    #options[0]=r options[1]=p options[2]=s
    compinput=options[num]
    print("Computer",compinput)
    if urinput.lower() == "r" and compinput == 's':
        your_score += 1
        print("You win!")
    elif urinput.lower() == "p" and compinput == 'r':
        your_score += 1
        print("You win!")
    elif urinput.lower() == "s" and compinput == 'p':
        your_score += 1
        print("You win!")
    elif urinput.lower() == compinput:
        print("It's a Draw!")         
    else:
        comp_score += 1
        print("Computer wins!")


print("goodbye")    