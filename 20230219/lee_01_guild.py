n=int(input())
finder=list(map(int,input().split()))

finder.sort()
member=0
count=0
for i in finder:
    count+=1
    if count>=i:
        member+=1
        count=0
print(member)

