S = input()
chan0 = 0
# 전부 0으로 바꿀경우
chan1 = 0
# 전부 1로 바꿀경우

if S[0] == '1':
    # 입력받은 문자열의 첫번째가 1일경우
    chan0 += 1
    # 0으로 변환한다에 1 더함.
else:
    chan1 += 1

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        # 대상이 된 숫자가 다음차례의 수와 다를경우
        if S[i+1] == '1':
            chan0 += 1
            # 다음차례의 수가 1이었다면 0교환에 1더하기
        else:
            chan1 += 1
print(min(chan0, chan1))
