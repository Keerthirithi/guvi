count=1
while(count>0):
    player1=str(input("enter the action"))
    player2=str(input("enter the action"))
    if(player1=="rock" and player2=="paper"):
        print("player1 win")
    elif(player1=="paper" and player2=="scissor"):
        print("player2 win")
    elif(player1=="scissor" and player2=="rock"):
        print("player2 win")
    elif(player1=="paper" and player2=="paper"):
        print("both are same")
    elif(player1=="rock" and player2=="rock"):
        print("both are same")
    elif(player1=="scissor" and player2=="scissor"):
        print("both are same")
    elif(player1=="paper" and player2=="rock"):
        print("player2 win")
    elif(player1=="scissor" and player2=="paper"):
        print("player1 win")
    elif(player1=="rock" and player2=="scissor"):
        print("player1 win")
    d=input("do u want to continue")
    if(d=="yes"):
        count=1
        continue
    else:
        count=0
        exit

    
