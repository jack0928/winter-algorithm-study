#11404: 플로이드
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)] #최단 거리 나타내는 2차원 리스트

#자신 -> 자신 비용은 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0


for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c) # 한 도시에서 다른 도시로 가는 버스가 여러 개일 수 있음

#점화식: graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()