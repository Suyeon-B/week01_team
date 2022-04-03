# 14888
import itertools
n = int(input())
numbers = list(map(int, input().split()))
temp = list(map(int, input().split()))
operator = {0:['+', 0], 1:['-', 0], 2:['*', 0], 3:['//', 0]}
for i in range(4):
    if temp[i] != 0:
        operator[i][1] += temp[i]

opers = []
for i in range(4):
    for j in range(operator[i][1]):
        opers.append(operator[i][0])

permut_oper = list(set(itertools.permutations(opers, len(opers))))

def operation(a, b, oper):
    if oper == '+':
        return a+b
    elif oper == '-':
        return a-b
    elif oper == '*':
        return a*b
    else:
        return int(a/b)

last = numbers[0]
result = []
while True:
    i=1
    for j in range(len(permut_oper)):
        for w in range(len(opers)):
            last = operation(last, numbers[i], str(permut_oper[j][w]))
            i+=1
        i=1
        result.append(last)
        last=numbers[0]
    break
print(max(result))
print(min(result))

