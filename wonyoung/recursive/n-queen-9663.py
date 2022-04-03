n = 8

# 퀸을 놓기전 놓을 수 있는 지 확인
# - 같은 행에 놓을 수 없음
# - 같은 대각선에 놓을 수 없음
# n-1 열까지 퀸을 놓았다면 cnt +=1

col = [0] * n
flag_a= [False] * n
flag_b= [False] * (2* n-1)
flag_c= [False] * (2* n-1)
cnt = 0
# i -> 놓은 행의 번호
def set(i):
  global cnt
  for j in range(n):    
    if not flag_a[j] and not flag_b[i+j] and not flag_c[i-j + (n-1)]:
      if i == n-1:
        cnt +=1
        return 
      col[i] = j
      flag_a[j] = flag_b[i+j] = flag_c[i-j + (n-1)] = True
      set(i+1)
      flag_a[j] = flag_b[i+j] = flag_c[i-j + (n-1)] = False

set(0)
print(cnt)