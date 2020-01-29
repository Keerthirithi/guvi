sum=0
for i in range(0,10):
  if(i%2==0):
    a=i
    i=sum+i
    sum=i
print(sum)
