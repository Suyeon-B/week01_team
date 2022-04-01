# 2557
# print('Hello World!')

# 10869
# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

# 2588
# a = int(input())
# b = input()
# print(a*int(b[2]))
# print(a*int(b[1]))
# print(a*int(b[0]))
# print(a*int(b))

# 9498
# def score(n):
#     if n>=90:
#         print('A')
#     elif n>=80:
#         print('B')
#     elif n>=70:
#         print('C')
#     elif n>=60:
#         print('D')
#     else:
#         print('F')
#
# n = int(input())
# score(n)

# 2753
# def is_lunar(n):
#     # 윤년일 때
#     if (n%4==0 and n%100!=0) or n%400==0:
#         return 1
#     return 0
#
# n = int(input())
# print(is_lunar(n))

# 1085
# x, y, w, h = map(int, input().split())
# a = h-y
# b = w-x
# print(min(x, y, a, b))


# 2739
# n = int(input())
# for i in range(1, 10):
#     result = n*i
#     print(f'{n}' + " * " + f'{i}' + " = " + f'{result}')

# 10950
# n = int(input())
# for i in range(n):
#     a, b = map(int, input().split())
#     print(a+b)

# 2438
# n = int(input())
# for i in range(1, n+1):
#     print('*'*i)

# 10871
# N, X = map(int, input().split())
# A = list(map(int, input().split()))
# for i in range(N):
#     if A[i] < X:
#         print(A[i], end=" ")

# 2562
# MAX, cnt = 0, 0
# for i in range(9):
#     n = int(input())
#     if n>MAX:
#         MAX = n
#         cnt = i
#
# print(MAX)
# print(cnt+1)

# 8958
# n = int(input())
# for i in range(n):
#     s = input()
#     score = 0
#     summary = 0
#     for j in range(len(s)):
#         if s[j] == 'O':
#             score += 1
#             summary += score
#         else:
#             score = 0
#     print(summary)

# 4344
# C = int(input())
# for i in range(C):
#     cnt = 0
#     scores = list(map(int, input().split()))
#     n = scores.pop(0)
#     avg = sum(scores)/n
#     for j in range(n):
#         if scores[j]>avg:
#             cnt+=1
#     result = cnt / n * 100
#
#     a = "{:.3f}".format(result)
#     print(a, end="")
#     print('%')

# 2577
# A = int(input())
# B = int(input())
# C = int(input())
# n = str(A*B*C)
# num_dic = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
# for i in range(len(n)):
#     num_dic[n[i]] += 1
# for i in range(10):
#     print(num_dic[str(i)])

# 15596
# def solve(a):
#     ans = sum(a)
#     return ans

# 11654
# a = input()
# print(ord(a))

# 2675
# n = int(input())
# for i in range(n):
#     r, s = input().split()
#     r = int(r)
#     for j in range(len(s)):
#         print(s[j]*r, end="")
#     print()

# 1152
# s = list(input().split())
# print(len(s))

# 2908
# a, b = input().split()
# bigger = 0
# if a[2]>b[2]:
#     bigger = a
# elif a[2]<b[2]:
#     bigger = b
# elif a[1]>b[1]:
#     bigger = a
# elif a[1]<b[1]:
#     bigger = b
# elif a[0]>b[0]:
#     bigger = a
# else:
#     bigger = b
# print(bigger[::-1])

