# 5568
# 입력된 숫자 카드에서 k장 선택해서 만들 수 있는 정수의 수
# 20분!! 걸렷당!! 예!!
import itertools

n = int(input())
k = int(input())
kards = []
for i in range(n):
    kards.append(input())

result=len(set(list(map(''.join, itertools.permutations(kards, k)))))

print(result)