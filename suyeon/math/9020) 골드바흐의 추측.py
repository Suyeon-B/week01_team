# 9020
# 30분 걸렸슝
import math
def is_prime(n):
    if n == 1:
        return False
    limit = int(math.sqrt(n)) # sqrt(n) 까지만 검사해보면 됨
    for i in range(1, limit+1):
        if i == 1:
            continue
        if n%i == 0:
            return False
    return True

def get_goldbach(n, a):
    result = [a, n-a]
    result.sort()
    print('%d %d'%(result[0], result[1]))

def get_biggest_prime(a, n):
    while True:
        if is_prime(a):
            if is_prime(n-a):
                return a
        a+=1

def print_goldbach(n):
    biggest_prime = get_biggest_prime(n//2, n)
    get_goldbach(n, biggest_prime)


t = int(input())
for i in range(t):
    n = int(input())
    print_goldbach(n)