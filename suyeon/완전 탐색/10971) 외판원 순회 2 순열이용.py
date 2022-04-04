# 10971
# 순열을 이용한 풀이 
import itertools

n = int(input())
distances = {}
graph = {}
for i in range(1, n + 1):
    distances[i] = list(map(int, input().split()))
    temp = []
    for j in range(n):
        if distances[i][j] != 0:
            temp.append(j+1)
    graph[i] = temp


def find_min_distance():
    result = 0
    results = [20000000]
    paths = [i+1 for i in range(n)]
    paths = itertools.permutations(paths, n)

    for path in paths:
        for i in range(n):
            if i == n-1:
                if distances[path[i]][path[0]-1] != 0:
                    result += distances[path[i]][path[0]-1]
                    if result < results[0]:
                        results[0] = result
                result = 0
            else:
                if distances[path[i]][path[i+1]-1] != 0:
                    result += distances[path[i]][path[i+1]-1]
                else:
                    result = 0
                    break

                if result > results[0]:
                    result = 0
                    break

    return results[0]

print(find_min_distance())
