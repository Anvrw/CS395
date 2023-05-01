import random

choices = ["rock", "paper", "scissors"]
yesChoices = ["yes", "no"]

userCount = 0
compCount = 0
playCount = -1
# if user == comp ==> it's a tie
# u:p c: s ==> you lose
# u:p c: r ==> you win
# u:r c: p ==> you lose
# u:r c: s ==> you win
# u:s c: p ==> you win
# u:s c: r ==> you lose
replayCheck = 'yes'
while(replayCheck == 'yes' and playCount != 0):
    if playCount == -1:
        playCount = int(input('How many times would you like to play?'))
    #Call Method to Play the Game
    #No inputs but outputs will be 1 if win, 0 if tie, -1 if lose
    #Call here then prompt to play again

    user = input("Please chose rock, paper, scissors: ").lower()

    while user not in choices:
        user = input(f"Your input {user} is not valid. Please enter rock, paper, or scissors").lower()

    comp = random.choice(choices)

    print(f"user: {user}")
    print(f"comp: {comp}")

    if comp == user:
        print("it's a tie!")
        print(userCount, compCount)

    elif ((user=="paper" and comp=="scissors") or (user=="rock" and comp=="paper") or (user=="scissors" and comp=="rock")):
        print("you lose!")
        compCount = compCount + 1
        print(userCount, compCount)

    elif ((user=="paper" and comp=="rock") or (user=="rock" and comp=="scissors") or (user=="scissors" and comp=="paper")):
        print("you win!")
        userCount = userCount + 1
        print(userCount, compCount)

    else:
        print("something went wrong")

    playCount -= 1

    if playCount == 0:
        user = input("Would you like to play again?\n").lower()

        while user not in yesChoices:
            print("Not Recognized. Choose Between Yes or No")
            user = input("Would you like to play again?\n").lower()
        if (user == 'no'):
            replayCheck = 'no'
        else:
            playCount = -1



