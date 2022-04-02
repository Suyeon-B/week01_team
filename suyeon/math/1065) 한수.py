# 1065

# 밑에건 시간 줄여보겠다고 더러워진 코드 ㅎㅎ 하하
# n = input()
# result = int(n)
# def find_left_hansu(n):
#     left_hansu = 0
#     hs = hansu_start[n[0]]
#     while hs<=int(n):
#         if hs>int(n):
#             return left_hansu
#         else:
#             hs+=12
#             left_hansu += 1
#     return left_hansu
#
# hansu_start = {'1': 111, '2':210, '3':321, '4':420, '5':531, '6':630, '7':741, '8':840, '9':951}
# if int(n)<100:
#     print(result)
# elif int(n) < 1000:
#     result = 99
#     if n[0] != '1':
#         result += ((int(n[0])-1)*5)
#     result += find_left_hansu(n)
#     print(result)
# else:
#     print(144)

# python에서 빠르게 입력 받는 법 배웠음~~
# import sys
# a = sys.stdin.readline().rstrip()
# print(a)

import sys
int_n = int(sys.stdin.readline().rstrip())
cnt = 0
if int_n < 100:
    print(int_n)
elif int_n <= 1000:
    cnt = 99
    while int_n>99:
        temp = str(int_n)
        a = int(temp[0]) - int(temp[1])
        b = int(temp[1]) - int(temp[2])
        if a==b:
            cnt +=1
        int_n-=1
    print(cnt)
