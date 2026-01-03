#2644: 촌수계산
'''
문제 흐름
1. 트리 생성 (모든 간선의 비용이 1인 무방향 그래프)
2. 정점 간 최단거리 계산
-> BFS: 시작 정점에서 가까운 것부터 레벨 순서로 탐색하니까 처음 방문한 경우가 최단 거리
DFS로도 되지만 가능한 모든 경로 탐색 필요
3. 연결 안 된 경우 -1 출력
'''
from collections import deque

def bfs(graph, start, end):
    distance = [-1] * (n+1) #distance가 0이상이면 방문한 것이므로 visited 불필요
    queue = deque([start])
    distance[start] = 0

    while queue:
        v = queue.popleft()
        if v == end:
            return distance[v]

        for child in graph[v]:
            if distance[child] < 0: #방문하지 않았다면
                distance[child] = distance[v] + 1
                queue.append(child)

    return -1 #촌수계산 불가


n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(graph,a,b))


'''
트리의 조건
1.	사이클이 없다
2.	모든 정점이 연결되어 있다
3.	간선 수 = 정점 수 - 1
'''