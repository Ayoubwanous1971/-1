binary=[]
num=int(input("please enter decimal value:"))
x=num
while x!=0:
    remain=x%2
    binary.append(remain)
    x=x//2
    binary.reverse()
    n=""
    for i in binary:
        n=n+str(i)
print(n)
