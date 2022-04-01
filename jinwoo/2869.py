
# 문제 링크 : https://www.acmicpc.net/problem/2869

import math

A,B,V = map(int, input().split(' '))


V = V-B                                 # 아침에 정상에 올랐다 저녁에 다시 내려가는 것을 방지해 주기 위해 V-B
H = A-B                                 # H 값 -> 하루에 올라갈 수 있는 높이

result = V/H


print(math.ceil(result))                # 3.4일도 4일이 걸리는 것이기 때문에 올림 연산 실행
