l1=[]
n=int(input ("Enter the value of n ="))
print("Enter elements =")
for i in range(n):
  a=int(input())
  l1.append(a)
l2=[]
for i in l1:
   if i not in l2:
    print (i)
    l2.append(i)
   else:
    l2.append(i)
