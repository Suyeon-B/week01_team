# 개념 이해 후 직접 작성
# row[x] = i -> (x, i)에 퀸을 두겠다는 의미.
# 퀸은 행, 열에 같은 퀸이 올 수 없으니
# 애초에 x값(행)은 고정으로 +1씩 지정해줌 (같은 행에 퀸이 배치되지 않도록)
# 이후 check 함수에서 1. 같은 열 2. 대각선(왼, 오) 를 체크함.

n = int(input())
result = 0
row = [0]*n

def check(x): # 같은 열에 있을 때, 대각선(왼,오)에 있을 때를 검사
    for i in range(x):
        if (row[x] == row[i]) or (abs(row[x] - row[i]) == abs(x-i)):
            return False
    return True

def n_queen(x):
    global result
    if x == n : # base case. 카운팅 끝!
        result+=1
        return
    else: # 아직 더 놓을 퀸이 있음
        for i in range(n):
            row[x] = i # (x, i)에 퀸을 둠
            if check(x): # 놓을 수 있으면
                n_queen(x+1) # 다음 거 검사

n_queen(0)
print(result)