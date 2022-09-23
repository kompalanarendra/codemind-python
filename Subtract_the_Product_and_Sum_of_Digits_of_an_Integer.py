n=int(input())
m=1
s=0
while n>0:
    r=n%10
    m*=r
    s+=r
    n=n//10
print(m-s)    