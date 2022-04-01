import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
a = [False, False] + [True]*(1000)

for i in range(2, 1001):
  if a[i]:
    for j in range(2*i, 1001, i):
      a[j] = False

cnt = 0
for i in arr:
  if a[i]:
    cnt+=1
print(cnt)