# 10989
import sys
n = int(sys.stdin.readline())
numbers = []
for i in range(n):
    numbers.append(int(input()))

numbers.sort()
for i in range(n):
    print(numbers[i])