
# 문제 링크 : https://www.acmicpc.net/problem/2628

# 기본 접근 방법은 x 좌표 리스트와 y 좌표 리스트를 만들고 해당 리스트에 시작점과 끝점을 넣었음.
# 그리고 종이를 자를때마다 x좌표를 잘랐으면 x 리스트에 넣고, y 리스트를 잘랐으면 y리스트에 넣고 순서대로 정렬함
# 각 리스트를 조회에 간격이 제일 넓은 경우의 수 끼리 곱하면 정답이 나옴


x,y = map(int, input().split())

n = int(input())

listx = [0]
listy = [0]
listx.append(x)
listy.append(y)

for _ in range(n):
    location, length = map(int, input().split(' '))
    if location == 1:
        listx.append(length)
    else:
        listy.append(length)

listx.sort()
listy.sort()

tempx = 0
maxX = 0
tempy = 0
maxY = 0
for i in listx:
    if i - tempx > maxX:
        maxX = i-tempx
    for j in listy:
        if j -tempy > maxY:
            maxY = j - tempy
        tempy = j;
    tempx = i

print(maxX*maxY)
