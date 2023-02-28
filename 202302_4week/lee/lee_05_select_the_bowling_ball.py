N = int(input())
ball = list(map(int, input().split()))
ball.sort()
count = 0
for i in range(N):
    if ball[i] == ball[i+1]:
        pass

# 볼의 무게가 세개연속으로 똑같이 나온다면 이걸 어떻게 해결하지?
