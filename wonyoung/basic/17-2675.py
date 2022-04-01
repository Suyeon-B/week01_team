import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n, s = input().strip().split()
  answer = ''
  for i in s:
    for _ in range(int(n)):
      answer+= i
  
  print(answer)