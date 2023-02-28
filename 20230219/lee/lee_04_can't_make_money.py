n = int(input())
money = list(map(int, input().split()))
money.sort()

target = 1
for i in money:
    if target < i:
        break
    else:
        target += 1

print(target)

# 1 1 2 3 5 를 입력하면 6이 나옴.
# 이해못함~~~~~~
