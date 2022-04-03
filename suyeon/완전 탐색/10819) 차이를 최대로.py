# 10819
# 2:52 -> 3:04
from itertools import permutations

n = int(input())
A = list(map(int, input().split()))

permut = list(permutations(A, n))
MAX = 0
result = 0
for i in range(len(permut)):
    for j in range(n-1):
        result += abs(permut[i][j]-permut[i][j+1])
    if MAX < result:
        MAX = result
    result = 0

print(MAX)