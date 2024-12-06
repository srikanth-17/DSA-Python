'''sch={
    "srikanth":1,
    "gururathnam":2,
    "kavitha":3
    }
a=sch.get("kavitha")
print(a)
print(sch)

aaa=dict()
n= input()
f=int(input())
aaa[n]=f
sch.update(aaa)
print(sch)'''

"""d=dict()
l=[1,2,3,4,5,6,7,8]
for i in range(1,len(l)+1):
    d[i]=[l[j] for j in range(i-1,len(j))]
print(d)"""



"""l=[3,4,6,8,1,2,7,5]
l.sort()
for i in range(len(l)):
    try:
        print(f"{i}-->{i+1}")
    except IndexError:
        pass"""


"""d={"name":"srikanth","age":21,"grade":'A'}
del d["grade"]
print(d)"""

"""x=-5
assert x>0, "Greater than zero"
print(x)"""