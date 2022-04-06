# 11729
# 7:10 -> 7:35
# base case : 마지막 원판만 남았을 때 -> 눈치보지 않고 바로 옮긴다. cnt+=1
# base case가 아닐 때 : 중간장대에 모두 옮긴 뒤, 마지막 장대에 옮긴다.

n = int(input())
cnt = 0

def hanoi(start, end, via, x):
    global cnt
    if x == 1: # base case
        print(f'{start} {end}')
        return

    hanoi(start, via, end, x-1)
    print(f'{start} {end}')
    hanoi(via, end, start, x-1)

print(2**n-1)
hanoi(1, 3, 2, n)
