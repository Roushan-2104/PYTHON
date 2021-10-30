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
    if choice=="rock" and item=="scissor" or choice=="scissor" and item=="paper" or choice=="paper" and item=="rock" :
        player +=1
        print("\nYou Won : )")
        print("\nComputer's choice :",item)
        print("Your Choice : ",choice,"\n")
        

    elif choice=="scissor" and item=="rock" or choice=="paper" and item=="scissor" or choice=="rock" and item=="paper":
        computer+=1
        print("\nYou Lost :(")
        print("\nComputer's choice :",item)
        print("Your Choice : ",choice ,"\n")
        

    elif choice==item :
        print("\n Tied !!")
        print("\nComputer's choice :",item)
        print("Your Choice : ",choice ,"\n")
    
    print("Computer = ",computer)
    print("PLAYER = ",player,"\n")

    Out=True
    while Out==True:
        playnot = input("Want to play Again (yes,no) : ").lower()
        if playnot=="yes" or playnot=="no":
            Out=False
        else:
            print("\nWrong Input")
    if playnot == "yes":
        quit=False
    elif playnot =="no":
        quit=True
        
    

print("\n## FINAL SCORE ##\n")
if computer > player:
    print("Computer Wins :( !!")
    print("You Lost !!\n")
elif computer < player:
    print("You Wins :) !!\n")
elif computer==player:
    print("TIED !!")