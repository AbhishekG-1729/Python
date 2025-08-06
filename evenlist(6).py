l=[]
n=int(input("Enter the number of entries:"))
for i in range(n):
    a=int(input("Enter value:"))
    l.append(a)
el=[] 
for i in l:
    if i%2==0:
        el.append(i)
print(l)
print("the even numbers of the input list are: ",el)