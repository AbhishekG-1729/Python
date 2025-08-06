s1 = input("Enter the string:\n")
l = s1.split()
dic = {}

for word in l:
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

print(dic)