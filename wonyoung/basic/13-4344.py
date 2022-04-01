import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline 

t = int(input())
for _ in range(t):
  arr = list(map(int ,input().split()))
  n = arr.pop(0)
  avg = sum(arr)/n
  over = 0
  for i in arr:
    if i > avg:
      over+=1
  answer = (over/n)*100
  print("{:.3f}".format(answer)+"%")