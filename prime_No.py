#prime no
flag=1
print("enter a no:")
p=input()
t=int(p)
prime=t//2
#print(prime)
for i in range(2,prime):
    if t%i == 0:
        flag=0
if flag==0:
    print("not a prime no")
else:
    print("prime no")