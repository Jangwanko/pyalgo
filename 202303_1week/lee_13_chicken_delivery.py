from itertools import combinations
# 리스트의 모든 경우의수를 구하는 패키지.

n, m = map(int, input().split())
# 도시의 크기 입력.
city = list(list(map(int, input().split())) for _ in range(n))
# 집과 치킨집의 위치 입력.
result = 999999
house = []
# 집의 좌표
chick = []
# 치킨집의 좌표

for i in range(n):
    for j in range(n):
        # i와 j 이중 for 문
        if city[i][j] == 1:
            house.append([i, j])
            # 집의 위치 찾기
        elif city[i][j] == 2:
            chick.append([i, j])
            # 치킨집의 위치 찾기.

for chi in combinations(chick, m):
    # 각 치킨집의 위치 탐색.
    temp = 0
    # 각 집마다 치킨집과의 거리 초기화.
    for h in house:
        chi_len = 999
        # 각 집마다 치킨집과의 거리.
        for j in range(m):
            chi_len = min(chi_len,
                          abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
            # abs로 절대값을 씌워 거리 계산.
        temp += chi_len
    result = min(result, temp)

print(result)
