#print fizz for multiple of 3, buzz for multiple of 5 and fizzbuzz for multiple of both

for i in range(0,50):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)