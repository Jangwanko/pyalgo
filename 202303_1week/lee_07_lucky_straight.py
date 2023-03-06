n=input()
#숫자를 문자로 입력받기
leng=len(n)
#문자열갯수 leng에 입력
result=0
#초기화 선언.
for i in range(leng//2):
    result+=int(n[i])
#앞의 절반까지 result에 입력
for j in range(leng//2,leng):
    result-=int(n[j])
#뒤 절반을 result에서 빼주기
if result==0:
    print("lucky")
#결과값이 0이라면..
else:
    print("ready")
