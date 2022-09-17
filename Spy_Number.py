n=int(input())
s=0
p=1
while n>0:
    k=n%10
    s=s+k
    p=p*k
    n=n//10
if(s==p):
    print("Spy Number")
else:
    print("Not Spy Number")