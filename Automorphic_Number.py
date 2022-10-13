n=int(input())
n1=len(str(n))
s=n**2
l=s%pow(10,n1)
if(l==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")