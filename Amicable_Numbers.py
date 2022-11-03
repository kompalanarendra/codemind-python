a=int(input())
b=int(input())
m=n=0
for i in range(1,a):
    if(a%i==0):
        m+=i
for i in range(1,b):
    if(b%i==0):
        n+=i
if(m==b and n==a):
    print("Amicable")
else:
    print("Not Amicable")
    