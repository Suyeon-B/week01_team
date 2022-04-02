import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
borad = [[0]*n for _ in range(n)]

answer = 0
def attack(x,y):
  return
def queen(cnt):
  global answer
  if cnt == n:
    answer +=1
    return
  
  for i in range(n):
    for j in range(n):
      if borad[i][j] == 0:
        borad[i][j] = 'Q'
        # 공격 가능 부분 표시

queen(0)
