import sys
sys.stdin = open("input.txt", "r")

x, y = map(int, input().split())
n = int(input())
w = [x]
h = [y]
for i in range(n):
    a, b = map(int, input().split())
    if a == 0: # 가로 점선
        h.append(b)
    else: # 세로 점선
        w.append(b)
num_of_pieces = (len(w)+1)*(len(h)+1)

w.sort()
h.sort()
areas = []
print('len', len(w))
for i in range(len(w)):
  print(i)
# 넓이 구하기
for i in range(len(w)):
    if i == 0:
        width = w[i]
    elif i == len(w):
        width = x-w[i]
    else:
        width = w[i]-w[i-1]
    for j in range(len(h)):
        if j == 0:
            height = h[j]
        elif j == len(h):
            width = y-h[j]
        else:
            height = h[j] - h[j - 1]
        areas.append(width*height)
result = max(areas)
print(result)