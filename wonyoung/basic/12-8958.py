import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  p = input().strip()
  score = 0
  temp = 1
  for i in p:
    if i == 'O':
      score+=temp
      temp +=1
    else:
      temp = 1
  print(score)
