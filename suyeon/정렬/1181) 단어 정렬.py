# 1181
n = int(input())
words = []
for i in range(n):
    words.append(input())
words.sort(key=str.lower())
for i in range(n-1):
    if words[i] != words[i+1]:
        print(words[i])