n = int(input())
finder = list(map(int, input().split()))

finder.sort()
# 공포도 정렬. [1,2,2,2,3]
member = 0
party = 0
for i in finder:
    party += 1
    # 멤버 영입중.
    if party >= i:
        # 멤버의 공포도가 1이라면 한명으로 끝, 2라면 2명.
        member += 1
        # party가 성립되면 카운트 +1
        party = 0
        # 초기화
print(member)
