import sys
sys.stdin = open("input.txt", "rt")

input = sys.stdin.readline

n = int(input())
arr = set([input().strip() for _ in range(n)])
arr = list(arr)
arr = sorted(arr, key = lambda x:(len(x), x))

for i in arr:
  print(i)