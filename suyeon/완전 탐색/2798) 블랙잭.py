# 2798
# 2:40 -> 2:52
from itertools import permutations

n, m = map(int, input().split())
kards = list(map(int, input().split()))

permut = list(permutations(kards, 3))
MAX = 0
for i in range(len(permut)):
    if (sum(permut[i]) <= m) and (MAX < sum(permut[i])) :
        MAX = sum(permut[i])

print(MAX)