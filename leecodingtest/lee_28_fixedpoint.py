# n=int(input())
# fix=list(map(int,input().split()))
# ans=-1
# for i in range(n):
#     if i == fix[i]:
#         ans=i
#         break
#     else:
#         pass
# print(ans)
# 그냥 문제를 풀면 이렇게 해도 답은 나오지만 시간제한..

def binary_search(array, start, end):
    if start > end:
        return None
    # 입력된 갯수의 오류.
    mid = (start+end)//2

    if array[mid] == mid:
        return mid
    # 고정점 리턴.

    elif array[mid] > mid:
        return binary_search(array, start, mid-1)
    # 왼쪽으로 검색.

    else:
        return binary_search(array, mid+1, end)
    # 오른쪽으로 검색.


n = int(input())
array = list(map(int, input().split()))
index = binary_search(array, 0, n-1)
#


if index == None:
    print(-1)
# 고정점 없음.
else:
    print(index)
# 고정점 출력.

# 진행예시
# n=5로, array=[-15,-6,1,3,7]로 넣을경우.
# binary_search 함수에는 ([-15,-6,1,3,7],0,4)로 실행.
# 임의의 mid 값 2, array[2]=1로 고정점이 아님.
# mid값이 array[mid]보다 크므로 else문으로 들어가 mid값에 1을 추가한후 다시 def실행.
# 임의의 mid 값 3, array[3]=3이므로 고정점.
# array[mid]와 mid값이 같으므로 if문 실행, 고정점 리턴.
