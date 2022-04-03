
# 그래프를 4등분으로 쪼개기 위해 2^n / 2 를 하고
# 해당되는 행, 열의 좌표값이 몇 사분면인지를 구한다.
# 지나온 순서들을 계산하기 위해 2사분면은 half*half(사분할 된 사각형중 하나의 넓이) 한개를 지나왔으므로 *1 3사분면은 *2 4사분면은 *3을 한다.
# 그 뒤 상대적인 좌표를 찾아야 하기에 줄어든 길이만큼 2사분면의 경우는 열의 값을 빼주고 3사분면은 행의 값을 뺀다 4사분면은 모두 뺸다.

# 재귀를 통해 반복하고 만약 최종적인 좌표가 2사분면이면 + 1 3사분면이면 +2 4사분면이면 +3을 해주면 끝


def solved(n,r,c):
    half = (2**n)//2
    result = 0
    if half == 1:
        if r == 0 and c == 0:
            return result
        elif r == 0 and c == 1:
            return result +1
        elif r == 1 and c == 0:
            return result +2
        elif r == 1 and c == 1:
            return result +3
    else:
        if r < half and c < half:             # 1사분면
            result = result + solved(n-1, r,c)
        elif r < half and c >= half:            # 2사분면
            result = result + half*half + solved(n-1, r, c-half)
        elif r >= half and c < half:            # 3사분면
            result = result + half*half*2 + solved(n-1, r-half, c)
        else:                                   # 4사분면
            result = result + half*half*3 + solved(n-1, r-half, c-half)
        return result

n,r,c = map(int, input().split(' '))

print(solved(n,r,c))