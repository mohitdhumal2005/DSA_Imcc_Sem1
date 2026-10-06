#get the value of n from user

n=int(input("enter no of rows"))
for i in range(2,n+1):
    for j in range(1,i+1):
        print(j, end="")
    print()