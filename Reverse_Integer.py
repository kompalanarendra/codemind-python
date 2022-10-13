def rev(n):
    sum=0
    while(n>0):
        r=n%10
        sum=sum*10+r
        n//=10
    return sum
n=int(input())
if(n<0):
    n=abs(n)
    print(rev(n)*-1)
else:
    print(rev(n))