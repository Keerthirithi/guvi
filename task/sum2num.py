count=1
while(count>0):
   a=int(input("enter the number"))
   b=int(input("enter the number"))
   c=a+b
   print(c)

   print("do u want to continue")
   n=input()
   if (n=="yes"):
      count=1
      continue
   else:
      count=0
      exit()

    
