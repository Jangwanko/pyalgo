n=int(input())
m=list(map(int,input().split()))
m.sort()

if n/2==0:
    print(m[-1]+m[0])
else:
    print(m[-1])

#check