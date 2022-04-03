n = int(input())
in_list = list(map(int ,input().split()))
visited = [False]*n
answer = 0
def sol(li):
  global answer
  if len(li) == n:
    total = 0
    for i in range(n-1):
      total += abs(li[i]- li[i+1])
    answer = max(answer, total)
    return
  
  for i in range(n):
    if not visited[i]:
      visited[i] = True
      li.append(in_list[i])
      sol(li)
      visited[i] = False
      li.pop()

sol([])
print(answer)

# 순열을 사용하여 모든 가능한 수를 찾음
"""
from itertools import permutations

n = int(input())
arr = list(map(int ,input().split()))

permu = list(permutations(arr, n))
def calculator(li):
  total = 0
  for i in range(len(li)-1):
    total += abs(li[i]-li[i+1])
  return total

answer = -1e9
for li in permu:
  answer = max(answer, calculator(li))

print(answer)
"""