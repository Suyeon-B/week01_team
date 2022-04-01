n = int(input())

# 연도 4의 배수 and not 100의 배수 or 400의 배수

if n%4==0 and not n%100 ==0 or n%400 ==0:
  print(1)
else:
  print(0)