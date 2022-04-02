#30분
# https://shoark7.github.io/programming/algorithm/tower-of-hanoi
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

k = int(input())

def hanoi(n, start, sub, end):
  if n == 1:
    print(start, end)
    return
  
  hanoi(n-1, start, end, sub)
  print(start, end)
  hanoi(n-1, sub, start, end)

print(2**k-1)
if(k < 20):
  hanoi(k, 1, 2, 3)