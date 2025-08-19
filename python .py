n=(input("enter the number"))
l=list(n)
m=len(l)
for i in range(0,m):
    for j in range(i+1,m):
        if l[i]+l[j]==9:
            print(i,j)