import sys
input = sys.stdin.readline

n = int(input())

while(n<1001):
  cnt = 0
  for i in range(1, n+1):
    if i <100:
      cnt+=1
    else:
      arr = list(map(int, str(i)))
      temp = 0
      for j in range(len(arr)-1):
        if j == 0:
          temp = arr[j] - arr[j+1]
        else:
          if temp == arr[j] - arr[j+1]:
            cnt+=1
  print(n, cnt)
  n+=1