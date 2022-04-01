# 2869
import math

A, B, V = map(int, input().split())
up_down = A-B
min_step = V-A
result = math.ceil(min_step/up_down)+1

print(result)