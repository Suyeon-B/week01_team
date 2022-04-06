# 2447
# retry 필요
import sys
sys.setrecursionlimit(10**6) 

def append_star(LEN):
    if LEN == 1:
        return ['*']
    
    stars = append_star(LEN//3)
    L = []

    for star in stars:
        L.append(star*3)
    for star in stars:
        L.append(star+' '*(LEN//3)+star)
    for star in stars:
        L.append(star*3)
    
    return L

n = int(sys.stdin.readline().strip())
print('\n'.join(append_star(n)))