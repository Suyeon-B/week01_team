import sys


sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n, r, c = map(int, input().split())

size = 2**n
max_value = size **2

def solution(size, max_value):
  global r, c
  if size == 2:
    # 수 검출 알고리즘
    arr = [[0,0], [0,0]]
    for i in range(1, -1, -1):
      for j in range(1, -1,-1):
        arr[i][j] = max_value
        max_value-=1
    print(int(arr[r][c]-1))
    return
  
  # r, c가 어디 사분면인지 확인 후 해당 사분면만 쪼개기
  
  if r < size/2 and c < size/2:
    # 왼쪽 위
    solution(size//2, max_value- (size/2)**2*3)
    return
  elif r < size/2 and c >= size/2:
    # 오른쪽 위
    c -= size//2
    solution(size//2, max_value - (size/2)**2*2)
    return
  elif r >= size/2 and c < size/2:
    # 왼쪽 아래
    r -= size//2
    solution(size//2, max_value - (size/2)**2*1)
    return
  else:
    # 오른쪽 아래
    r -= size//2
    c -= size//2
    solution(size//2, max_value - (size/2)**2*0)
    return
  
  
solution(size, max_value)