import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

s = input().strip().split(' ')
cnt = 0
for i in s:
  if i != '':
    cnt+=1
print(cnt)