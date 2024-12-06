def fact(x):
    if x==1:
        print(1)
    else:
        print(x*fact(x-1))

n=int(input())
for i in range(n):
    a=int(input())
    print(fact(a))
