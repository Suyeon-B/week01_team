# 9963
def z(n, r, c, cnt):
    if n==1:
        last(r, c, cnt)
    else:
        mid = 2**n//2

        if mid <= r:
            if mid <= c: # 4                   
                cnt += mid**2*3
                if (r-mid <= 1) and (c-mid <= 1):
                    last(r-mid, c-mid, cnt)
                    return                 
                z(n-1, r-mid, c-mid, cnt)
            else: # 3
                cnt += mid**2*2
                z(n-1, r-mid, c, cnt)
        else:
            if mid <=c: # 2
                cnt += mid**2*1
                z(n-1, r, c-mid, cnt)
            else: # 1
                z(n-1,r,c, cnt)

def last(r, c, cnt):
    cnt+=(2*r+c+1)-1
    print(cnt)

n, r, c = map(int, input().split())
z(n, r, c, 0)