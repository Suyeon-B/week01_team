# 1065
import sys
sys.stdin = open("input.txt", "rt")
# n = input()
n = '100'
result = int(n)
def find_left_hansu(n):
    left_hansu = 0
    hs = hansu_start[n[0]]
    while hs<=int(n):
        if hs>int(n):
            return left_hansu
        else:
            hs+=12
            left_hansu += 1
    return left_hansu

hansu_start = {'1': 111, '2':210, '3':321, '4':420, '5':531, '6':630, '7':741, '8':840, '9':951}
while(int(n)<1001):
  if int(n)<100:
      print(n,result)
  elif int(n) < 1000:
      result = 99
      if n[0] != '1':
          result += ((int(n[0])-1)*5)
      result += find_left_hansu(n)
      print(n,result)
  else:
      print(n,144)
  n = int(n) +1
  n = str(n)