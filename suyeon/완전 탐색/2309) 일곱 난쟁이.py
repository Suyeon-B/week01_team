# 2309
# 2:21 -> 2:38
dwarfs = []
for i in range(9):
    tall = int(input())
    dwarfs.append(tall)

total = sum(dwarfs)
over = total - 100
break_or_not = 0
for i in range(9):
    for j in range(9):
        if i!= j:
            if dwarfs[i]+dwarfs[j] == over:
                t1 = dwarfs[i]
                t2 = dwarfs[j]
                dwarfs.remove(t1)
                dwarfs.remove(t2)
                break_or_not = 1
                break
    if break_or_not != 0:
        break
dwarfs.sort()
print(*dwarfs, sep = "\n")