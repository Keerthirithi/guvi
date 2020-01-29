count=1
while(count>0):
    s=int(input("enter the source"))
    d=int(input("enter the destination"))
    km=d-s
    print(km)
    mini=1
    micro=2
    prime=3
    print("enter the choice")
    n=int(input())
    def mini():
        print("amount per km is 10")
        a=10
        b=10*km
        print("the amount iss:",b)
        return b
    def micro():
        print("amount per km is 20")
        a=20
        b=20*km
        print("the amount is:",b)
        return b
    def prime():
        print("amount per km is 100")
        a=100
        b=100*km
        print("the amount is:",b)
        return b
    if(n==1):
        mini()
    elif(n==2):
        micro()
    elif(n==3):
        prime()
    else:
        print("invalidchoice")
    d=input("do u want to continue")
    if(d=="yes"):
        count=1
        continue
    else:
        count=0
        exit
        
        










