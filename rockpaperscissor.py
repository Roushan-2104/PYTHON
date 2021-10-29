import random

print("\n## Welcome to Rock , Paper , Scissor ##")


computer = 0
player = 0

quit = False

while quit==False:
    wrong=True
    item = random.choice(["ROCK" , "PAPER" , "SCISSOR"]).lower()
    while wrong==True:
        choice = input("\nEnter your Choice (Rock , Paper , Scissor) : ").lower()
        if choice=="rock" or choice=="paper" or choice == "scissor":
            wrong = False
        else:
            print("Wrong Input!!\n")
    if item==choice:
        player +=1
        print("\nYou Won : )")
        print("\nComputer's choice :",item)
        print("Your Choice : ",choice,"\n")
        

    elif item!=choice:
        computer+=1
        print("\nYou Lost")
        print("\nComputer's choice :",item)
        print("Your Choice : ",choice ,"\n")
        

    else :
        print("\n What are you doing man !!!!")
    
    print("Computer = ",computer)
    print("PLAYER = ",player,"\n")

    playnot = input("Want to play Again (yes,no) : ").lower()
    if playnot == "no":
        quit=True
    elif playnot =="yes":
        quit=False
    else:
        print('You typed wrong vro , Now play again !! ')

print("\n## FINAL SCORE ##\n")
if computer > player:
    print("Computer Wins :( !!")
    print("You Lost !!\n")
elif computer < player:
    print("You Wins :) !!\n")
elif computer==player:
    print("TIED !!")