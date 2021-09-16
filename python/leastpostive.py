def findleast(a,s):
    for i in a:
        if s==i:
            s=s+1
            s=findleast(a,s)
    return s




a=[]
s=0
a=map(int,input().split())
print(findleast(a,s))

