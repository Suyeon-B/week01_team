# 9963
# 체크해야 할 조건
# 1) 입력에서 부터 같은 행에 오지 못하게 구성
# 2) 같은 열에 있는지 검사
# 3) 대각선(왼, 오) 검사

n = int(input())
result = 0
row = [0]*n

def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
    return True

def n_queen(x):
    global result
    if x == n: # base case
        result +=1
        return
    else:
        for i in range(n):
            row[x] = i # (x, i)에 퀸을 놓음
            if check(x):
                n_queen(x+1)


n_queen(0)
print(result)