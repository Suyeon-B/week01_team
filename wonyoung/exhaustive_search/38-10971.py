# 순열 풀이 -> 시간초과, pypy 메모리 초과
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False]*n

result = 1e9
def solution(start, cnt, cost,city):
  # 모든 도시 방문 출발 도시로 이동
  global result
  if cnt == n:
    if arr[city][start] == 0 :
      # 출발한 도시로 돌아 갈 수 없을 때 return
      return
    cost += arr[city][start]
    result = min(cost, result)
    return
  
  for i in range(n):
    if not visited[i]:
      if arr[city][i] == 0:
        continue
      visited[i] = True
      solution(start, cnt+1, cost+arr[city][i], i)
      visited[i] = False

for i in range(n):
  visited[i] = True
  solution(i, 1, 0, i)
  visited[i] = False
print(result)