
# 문제 링크 : https://www.acmicpc.net/problem/1065

N = int(input())

result = 0

# 100보다 작은 수들은 그 자체가 등차수열이기 때문에 한수 = N의 수이다.
if N < 100:
    result = N
    print(result)
# 100보다 큰 수들은 모든 경우의 수를 계산해서 첫번째 자리수 -> 두번째 자리수 -> 세번째 자리수 각각의 등차가 같을 경우 result를 + 시킨다.
else:
    for i in range(100, N+1):
        x = str(i)
        if int(x[1]) - int(x[0]) == int(x[2]) - int(x[1]):
            result = result+1
    result = result+99
    print(result)

