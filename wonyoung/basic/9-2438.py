n = int(input())

for i in range(1, n+1):
  temp = ''
  for j in range(i):
    temp += '*'
  print(temp)