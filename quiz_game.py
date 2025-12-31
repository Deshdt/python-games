print("Welcome to my Quiz")

points = 0
play = input("Do you want to play the game? ")
if play.lower() != "yes":
    print(":( Hope to see you soon!")
    quit()

print("Hooray! Lets play :)")

ans1 = input("what does cpu stand for? ")
if ans1.lower() == "central processing unit":
    print("Correct!")
    points=points+1
else:
    print("Incorrect!No woories answer next question")

ans2 = input("what does hci stand for? ")
if ans2.lower() == "human computer interface":
    print("Correct!")
    points=points+1
else:
    print("Incorrect!No woories answer next question")

ans3 = input("what does ram stand for? ")
if ans3.lower() == "random access memory":
    print("Correct!")
    points=points+1
else:
    print("Incorrect!No woories answer next question")

ans4 = input("what does css stand for? ")
if ans4.lower() == "cascading stylesheet":
    print("Correct!")
    points=points+1
else:
    print("Incorrect!No woories answer next question")

ans5 = input("what does html stand for? ")
if ans5.lower() == "hyper text markup language":
    print("Correct!")
    points=points+1
else:
    print("Incorrect!")

print("Your Score:",points,"/5")
per = (points/5)*100
print("Your Percentage:",per)