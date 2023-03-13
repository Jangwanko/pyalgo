n=int(input())
fix=list(map(int,input().split()))
ans=-1
for i in range(n):
    if i == fix[i]:
        ans=i
        break
    else:
        pass
print(ans)
        