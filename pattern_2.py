#pattern

print("enter the no of rows")
no=int(input())
for i in range(0,no):
    for j in range(no-1,i,-1):
       print(end=" ")
    for k in range(0,2*i+1):
        print("*",end=" ")
    print("\r")
