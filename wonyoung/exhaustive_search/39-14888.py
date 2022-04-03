import sys
sys.stdin = open("input.txt", "r")

n = int(input())
numbers = list(map(int, input().split()))
sign = list(map(int, input().split()))

min_result = 1e9
max_result = -1e9
temp = []
def solution(index, result):
  global min_result, max_result
  if index == n:
    min_result = min(min_result, result)
    max_result = max(max_result, result)
    
    return
  
  if sign[0] > 0:
    sign[0] -= 1
    solution(index+1, result + numbers[index])
    sign[0] += 1

  if sign[1] > 0:
    sign[1] -=1
    solution(index+1, result - numbers[index])
    sign[1] +=1

  if sign[2] > 0:
    sign[2] -=1
    solution(index+1, result * numbers[index])
    sign[2] +=1

  if sign[3] > 0:
    sign[3] -=1
    solution(index+1, int(result / numbers[index]))
    sign[3] +=1

solution(1, numbers[0])

print(max_result)
print(min_result)