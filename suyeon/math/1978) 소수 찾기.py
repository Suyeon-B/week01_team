# 1978
import math
def is_prime(n):
    if n == 1:
        return False
    limit = int(math.sqrt(n)) # sqrt(n) 까지만 검사해보면 됨
    for i in range(1, limit+1):
        if i == 1:
            continue
        if n%i == 0:
            return False
    return True

N = int(input())
numbers = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if is_prime(numbers[i]):
        cnt += 1

print(cnt)