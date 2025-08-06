s=str(input("Enter the string "))
l=[]
for i in s:
    if i not in l:
        print(i" ",end="")
        l.append(i)
