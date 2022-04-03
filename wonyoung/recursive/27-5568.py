# 45분
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
n = int(input())
k = int(input())
arr = [input().strip() for _ in range(n)]
visited = [False] * n

answer = set()
def recur(cnt, li):
  if cnt == k:
    answer.add(''.join(li))
    return
  
  for i in range(n):
    if not visited[i]:
      visited[i] = True
      recur(cnt+1, li + [arr[i]])
      visited[i] = False

recur(0, [])
print(len(answer))