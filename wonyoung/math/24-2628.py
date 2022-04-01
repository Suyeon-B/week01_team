# 시간 측정 못 함
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

x, y = map(int, input().split())
list_x = [0]
list_y = [0]
n = int(input())
for _ in range(n):
  a, b = map(int, input().split())
  if a == 0:
    list_y.append(b)
  else:
    list_x.append(b)
list_x.append(x)
list_y.append(y)
list_x.sort()
list_y.sort()
result = -1e9
for i in range(1, len(list_x)):
  for j in range(1, len(list_y)):
    width = list_x[i] - list_x[i-1]
    hight = list_y[j] - list_y[j-1]
    result = max(result, width*hight)

print(result)