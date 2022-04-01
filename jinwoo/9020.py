
# 문제 링크 : https://www.acmicpc.net/problem/9020

# 시간초과.. 시간 복잡도 이상은 없는거 같은데 잘 모르겠음. 에라토스테네스의 체를 이용해 시간 복잡도를 줄여서 통과함
# 참고 블로그 : https://yoonsang-it.tistory.com/31
""" T = int(input())

for i in range(T):
    N = int(input())
    check = 0
    A = int(N/2)
    B = N-A
    while True:
        for k in range(2, A):
            if A % k == 0:
                break
            if k == A-1:
                check = check+1
        if check == 1:
            for k in range(2, B):
                if B % k == 0:
                    break
                if k == B-1:
                    check = check+1
        if check == 2:
            print(str(B) + ' ' + str(A))
            break
        check = 0
        A = A+1
        B = B-1 """


def Goldbach():
    check = [False, False] + [True] * 10000
    
    for i in range(2, 101):
        if check[i] == True:
            for j in range(i + i, 10001, i):
                check[j] = False
    
    T = int(input())
    for i in range(T):
        N = int(input())
        A = int(N/2)
        B = N-A

        while True:
            if check[A] and check[B]:
                print(B, A)
                break
            A = A+1
            B = B-1

Goldbach()