#가설 어떻게 해야 더 많아지거나 적어지는가?
#숫자를 정렬한후 작은수의 앞에는 나눗셈과 빼기를, 큰수의 앞에는 더하기와 곱하기를 한다고 하자.

n=int(input())
for _ in range(1,n):
    num=list(map(int,input().split()))
plus,minus,multi,div=map(int,input().split())
count=0
num1=num.sort()
for i in range(len(num)):
    for j in num1:
        if j==num[i]:
            count