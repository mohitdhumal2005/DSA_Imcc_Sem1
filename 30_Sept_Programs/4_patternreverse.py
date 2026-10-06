#get the value of n from user

n=int(input("enter no of rows"))
for i in range (n,0,-1):
    for j in range(i,0,+1):
        print(j, end="")
    print()