s = input()
#문자열 입력받기
result = []
#리스트 선언
value = 0
#숫자 초기화

for i in s:
    if i.isalpha():
        result.append(i)
    #i에 문자가 있다면 result로 넣기
    elif i.isalnum():
        value += int(i)
    #i에 숫자가 있다면 value에 더하기
result.sort()
#문자정렬
result=''.join(result)
#문자 공백없이 붙이기
print(result,value)
#끄아악 숫자 어떻게 딱 붙임?
