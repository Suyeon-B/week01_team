from itertools import permutations
import sys
sys.stdin = open("input.txt", "r")

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

li = list(permutations(list(range(n)),n))

result = 1e9
for city_list in li:
  cost = 0
  for i in range(n-1):
    if w[city_list[i]][city_list[i+1]] == 0:
      break
    if i == (n-2) and w[city_list[i+1]][city_list[0]] != 0:
      cost += w[city_list[i]][city_list[i+1]]
      cost += w[city_list[i+1]][city_list[0]]
      result = min(result, cost)
    else:
      cost += w[city_list[i]][city_list[i+1]]
    if cost >= result:
      # 기존의 result 보다 값이 크면 이미 최소값이 아님
      break

print(result)