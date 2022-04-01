# 시간 측정 못 했어요 ㅠ
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

temp = 10000
arr=[False, False] + [True] *(temp-1)

for i in range(1, temp+1):
  if arr[i]:
    for j in range(2*i, temp+1, i):
      arr[j] = False

t = int(input())
for _ in range(t):
  n = int(input())
  answer = []
  for i in range(2, n//2 +1):
    if arr[i] and arr[n-i]:
      answer.append((i, n-i))
  
  min_value = 1e9
  index = -1
  for i in range(len(answer)):
    a, b = answer[i]
    if min_value > abs(a-b):
      min_value = abs(a-b)
      index = i
  print(*answer[index])