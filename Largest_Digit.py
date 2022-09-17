n=int(input())
r=0
while n>0:
    d=n%10
    if r<d:
        r=d
    n=n//10
print(r)   
    
    
    