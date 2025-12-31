
name = input("Enter your name: ")
print("Welcome ",name," to the adventure!")

print("You have to choose any one of the two options provided in your story.Keep playing until you win or lose.")

print("\nLets Begin:")

ans = input("You are on a road, it has come to an end you can either go [left or right]. Which way would you like to go? ").lower()

if ans == "left":
    ans = input("You come to Race track, would you [run or walk]?").lower()

    if ans == "walk":
        ans = input("walked a lot you reached swimming pool further you want to [swim or walk] around?").lower()

        if ans == "walk":
            print("You were too slow to reach the destination.You Lost!")

        elif ans == "swim":
            ans = input("You reached the end. Do you want to [go ahead or swim] back.").lower()

            if ans == "go ahead":
                ans = input("Do you want to [swim or walk]?").lower()

                if ans == "swim":
                    print("Exhausted because you swam a lot. You Lost!")

                elif ans == "walk":
                    ans = input("You find a bus do you want to [ride a bus or run]?").lower()

                    if ans == "ride a bus":
                        print("You don't have cash.You Lost.")

                    elif ans == "run":
                        print("You Reached your Destination.Congratulations You Won!")

                    else:
                        print("Not a valid option.You Lost.")

                else:
                    print("Not a valid option.You Lost.")

            elif ans == "swim back":
                print("You were so close.You Lost!")

            else:
                print("Invalid option.You Lost!")

        else:
            print("Not a valid option.You Lost!.")

    elif ans == "run":
        ans = input("You reached faster arrived in forest.Do you want to [change route or continue]?").lower() 

        if ans == "change route":
            ans = input("You reached a River [swim or take nearby road]").lower()

            if ans == "swim":
                print("The River is too cold.You Lost!")

            elif ans == "take nearby road":
                ans = input("You are on the road.Do you want to [walk or ride a bus]?").lower()

                if ans == "walk":
                    print("You are too tired now.You Lost!")

                elif ans =="ride a bus":
                    print("You reached your destination.Congratulations You Won!")

                else:
                    print("Not a valid choice.You Lost!")

            else:
                print("Not a valid option.You Lost")

        elif ans == "continue":
            print("Dead End,You cannot go ahead.You Lost.")

        else:
            print("Invalid Option.You Lost.")

    else:
        print("Invalid option.You Lost.")

elif ans == "right":
    ans = input("After walking for a while the road ends.You want to go to the [left or right]?").lower()

    if ans == "left":
        ans = input("Hooray! A shortcut.You can either [run or ride a bus].").lower()

        if ans == "run":
            print("You lost your route and went into a deep jungle, now you are late. You Lost.")

        elif ans == "ride a bus": 
            ans = input("You are very close.Do you want to [run or walk]?").lower()

            if ans=="run":
                ans = input("You tripped,Do you want to take a [break or walk].").lower()

                if ans == "break":
                    print("You rested a bit too long.You Lost!")

                elif ans == "walk":
                    print("You never gave up, you Deserve this Win. Congratulations You Win!")

                else:
                    print("Invalid option. You Lost.")

            elif ans == "walk":
                print("You were slow. You Lost.")

            else:
                print("Invalid option. You Lost.")

        else:
            print("Invalid option. You Lost.")

    elif ans == "right":
        print("It's a dead end.You Lost.")

    else:
        print("Invalid option. You Lost.")

else:
    print("Invalid option. You Lost.")                  