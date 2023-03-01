n = input()
num = n.split('-')

answer = []

for i in num:
    count = 0
    plus = i.split('+')
    for j in plus:
        count += int(j)
    answer.append(count)
minus = answer[0]
for j in range(1, len(answer)):
    minus -= answer[j]
print(minus)
