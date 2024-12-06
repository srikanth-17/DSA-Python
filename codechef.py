'''n=int(input())
for x in range(n):
    l=[int(i) for i in input().split()]
    x=l[0]+l[1]
    y=l[2]-1
    if x<=y:
        print(0)
    else:
        print(x-y)'''
n=int(input())
for i in range(n):
    c=0
    a=int(input())
    s=input()
    vow=['a','e','i','o','u']
    x=0
    while(x<a):
        if s[x] not in vow:
            c=c+1
        