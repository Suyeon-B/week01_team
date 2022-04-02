# 2750
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
for i in range(n):
    numbers.sort()
    print(numbers[i])