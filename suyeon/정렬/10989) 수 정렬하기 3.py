# 10989
# pypy3가 python3보다 빨라도, 메모리는 더 잡아먹는다는 사실....
# 어떻게 알았냐구요? 저도 알고 싶지 않았어요 ㅎㅎ 하하
import sys
n = sys.stdin.readline()
numbers = [0] * 10001
for i in range(int(n)):
    numbers[int(sys.stdin.readline())] += 1

for i in range(10001):
    if numbers[i] != 0:
        for j in range(numbers[i]):
            print(i)