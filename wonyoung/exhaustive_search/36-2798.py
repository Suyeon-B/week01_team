# 3개를 뽑아서 m을 넘지 않는 최대한 가까운 수
import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
card = list(map(int, input().split()))
visited = [False] * n
answer = -1e9
def pickup(cnt, result):
  global answer
  if cnt == 3:
    if result <= m:
      answer = max(result, answer)
    return
  
  for i in range(n):
    if not visited[i]:
      visited[i] = True
      pickup(cnt+1, result+card[i])
      visited[i] = False

pickup(0,0)
print(answer)

""" 조합으로 풀기
from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))

combi = list(combinations(card,3))
maxSum = -1e9
for i in combi:
  if sum(i) <= m:
    maxSum = max(maxSum, sum(i))
print(maxSum)
"""