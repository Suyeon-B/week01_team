# 1914
# 20보다 작은 경우에만 재귀함수 돌리기!
import sys

n = int(sys.stdin.readline())
def hanoi(n, start, to):
    if n == 1:
        print(f'{start} {to}')
        return

    hanoi(n-1, start, 6-start-to)
    print(f'{start} {to}')
    hanoi(n-1, 6-start-to, to)


print(2**n-1)
if n<=20:
    hanoi(n, 1, 3)
