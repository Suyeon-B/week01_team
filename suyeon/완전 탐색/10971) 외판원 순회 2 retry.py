# 10971
# 4:57 -> 5:35
import itertools
n = int(input())
result = 0
min_result = float('inf')

# paths 순열로 미리 생성
paths = list(range(n))
paths = list(itertools.permutations(paths, n))

# distances 입력
distances = {}
for i in range(n):
    distances[i] = list(map(int, input().split()))

def permut(n):
    result = 0
    min_result = float('inf')

    # 유효한 path인지 검사
    # 최소 비용 업데이트
    # 검사 중 이미 최소 비용보다 커지면 break
    for path in paths: # ex) (1, 2, 3, 4)
        for i in range(n-1): # 1, 2, 3, 4로 가는 경로 구해야 함.
            if distances[path[i]][path[i+1]] == 0: # 길이 없을 때
                result = 0
                break
            result += distances[path[i]][path[i+1]]
            if result > min_result: # 여태까지 구한 게 이미 최소가 아니라면 break
                result = 0 
                break
            if i == n-2: # 끝 도시까지 다 돌았으면 min_result 업뎃
                result += distances[path[i+1]][path[0]]
                if (result > min_result) or (distances[path[i+1]][path[0]] == 0): # 여태까지 구한 게 이미 최소가 아니거나 길이 없으면 break
                    result = 0 
                    break
                min_result = result
                result = 0
    return min_result

print(permut(n))