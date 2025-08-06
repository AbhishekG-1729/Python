n=int (input("Enter the number ="))
l=[]
l2=[]
for i in range(0,n,1):
    a=int(input ("Enter the 1st number =\n"))
    b=int(input ("Enter the 2nd number =\n"))
    l.append([a,b])
temp=[]
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j][1]>l[j+1][1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
for i in l:
    l2.append(tuple(i))
print(l2)