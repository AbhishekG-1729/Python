m=int(input("Enter the starting no ="))
n=int(input("Enter the ending no ="))
if(m%2==1):
    m=m+1
if(n%2==1):
    n=n-1
res=sorted({num**2 for num in range(m,n+1,2)})
print(res)