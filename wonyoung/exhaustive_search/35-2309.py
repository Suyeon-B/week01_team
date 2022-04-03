# 조합 라이브러리를 사용하여 9개중 7개를 뽑았을 때 합이 100이 되는 경우를 찾는 방식
from itertools import combinations
import sys
sys.stdin = open("input.txt", "rt")

input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]
combin = list(combinations(arr, 7))
for i in combin:
  if sum(i) == 100:
    i = list(i)
    i.sort()
    for hobit in i:
      print(hobit)
    break