#sum of list items

sum=0
print("enter no of elements")
n=int(input())
print("enter the item elemnt")
for i in range(n):
    item=int(input())
    list=[i,item]
    sum=sum+item
print("sum of elements is: ")
print(sum)
