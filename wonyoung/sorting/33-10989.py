import sys
sys.stdin = open("input.txt", "rt")

input = sys.stdin.readline
n = int(input())
temp = [0] * 10001
for i in range(n):
  temp[int(input())] +=1

for i in range(1, 10001):
  if temp[i] != 0:
    for _ in range(temp[i]):
      print(i)

