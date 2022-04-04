# 10971
# try 27496128번째 쯤... 시간 초과 나옴 ㅠㅠ
# 불필요한 연산 최적화 후.. 틀렸다고 나옴 하하
# result 초기화 안해서 틀렸던 것!!! 하하하하하하
n = int(input())
paths = []
distances = {}
graph = {}
for i in range(1, n + 1):
    distances[i] = list(map(int, input().split()))
    temp = []
    for j in range(n):
        if distances[i][j] != 0:
            temp.append(j+1)
    graph[i] = temp


def dfs(graph, start, end, visited=[]):
    visited = visited + [start]

    # 도착할 경우, paths에 경로 기록
    if start == end:
        paths.append(visited)
            
    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, end, visited)
        
    return paths

def find_min_path(start):
    result = 0
    results = [20000000]
    paths = dfs(graph,start,n)
    for path in paths:
        if len(path) == n:
            for i in range(n):
                if i == n-1:
                    result += distances[path[i]][path[0]-1]
                    results[0] = result
                    result = 0
                else:
                    result += distances[path[i]][path[i+1]-1]
                    if result < results[0]:
                        continue
                    else:
                        result = 0
                        break
    return results[0]

min_result = 20000000
for i in range(1, n+1):
    if min_result > find_min_path(i):
        min_result = find_min_path(i)
print(min_result)