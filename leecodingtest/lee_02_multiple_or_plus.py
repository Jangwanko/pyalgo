n = input()
# 문자열 입력받기
count = int(n[0])
# 문자열을 숫자형으로 분해
for i in range(1, len(n)):
    # 문자열의 갯수대로 반복.
    number = int(n[i])
    # n으로 입력받은 문자열들을 순서대로 number라는 숫자형으로 변환.
    if number <= 1 or count <= 1:
        # count<=1을 해주는 이유는 첫번째수가 0일 경우를 위함.
        count += number
        # number가 1보다 작다면, 더할것
    else:
        count *= number
        # 그외엔 곱할것.
print(count)
