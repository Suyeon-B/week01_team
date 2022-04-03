from itertools import combinations
import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
card = list(map(int, input().split()))

combi = list(combinations(card,3))
maxSum = -1e9
for i in combi:
  if sum(i) <= m:
    maxSum = max(maxSum, sum(i))
print(maxSum)
