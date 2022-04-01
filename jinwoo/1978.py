#문제 링크 : https://www.acmicpc.net/problem/1978

# 해당 문제의 경우 시간제한은 2초이고 최악의 경우 연산이 10만번이 조금 넘으므로 O(N)의 알고리즘을 짜도 무방하다고 판단했음

N = int(input())

numList = list(map(int, input().split(' ')))
count = 0
for num in numList:
    if num == 2:                                # 2인 경우는 자동으로 증가
        count = count+1
    else:
        for i in range(2, num):
            if num % i == 0:                    # 소수의 조건에 위배되는 순간 for문을 탈출
                break
            if i == num-1:                      # 조건에 부합한다면 count 증가
                count = count +1

print(count)    