from collections import deque
# deque 사용

n, m, k, x = map(int, input().split())
# 도시의 개수, 도로, 거리정도, 출발도시 입력.

graph = [[]for _ in range(n+1)]
# 도시의 개수를 graph에 이중 리스트로 입력
for _ in range(m):
    # 도로갯수 만큼 반복
    a, b = map(int, input().split())
    # 이동하는 거리 입력.
    graph[a].append(b)

    distance = [-1]*(n+1)
    distance[x] = 0

    q = deque([x])
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if distance[next_node] == -1:
                distance[next_node] = distance[now]+1
                q.append[next_node]
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)
