import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

a, b = map(int, input().split())
a = list(str(a))
b = list(str(b))
a.reverse()
b.reverse()

print(max(int(''.join(a)),int(''.join(b))))