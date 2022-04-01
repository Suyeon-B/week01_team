num1 = int(input())
num2 = int(input())

for i in range(len(str(num2))-1,-1, -1):
  print(int(str(num2)[i])*num1)
print(num1*num2)
