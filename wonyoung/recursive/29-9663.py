import sys

sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

# n = int(input())
n = 15

pos = [0] * n
flag_a = [False] * n
flag_b = [False] * (2*n - 1)
flag_c = [False] * (2*n - 1)

cnt = 0
def put() -> None:

  for i in range(n):
    for j in range(n):
      print('■' if pos[i] == j else '□', end='')
    print()
  print()

def set(i: int) -> None:
  global cnt
  #i열에 퀸 배치
  for j in range(n):
    if not flag_a[j] and not flag_b[i+j] and not flag_c[i-j+(n-1)]:
      pos[i] = j
      if i == n-1:
        # put()
        cnt +=1
        return
      else:
        flag_a[j] = flag_b[i+j]= flag_c[i-j+(n-1)] =True
        set(i+1)
        flag_a[j] = flag_b[i+j]= flag_c[i-j+(n-1)] =False

set(0)
print(cnt)