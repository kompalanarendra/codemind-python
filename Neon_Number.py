n=int(input())
sqrt=n*n
sum=0
while(sqrt>0):
    a=sqrt%10
    sum+=a
    sqrt=sqrt//10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")
    