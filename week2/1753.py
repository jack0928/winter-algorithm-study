#1753: 최단경로
'''
공교롭게도 방금 전에 다익스트라 빠른 버전을 공부했는데 해당 코드를 구현하는 문제이다.
우선순위 큐를 사용해서 현재 가장 가까운 노드를 찾는 시간을 줄인다. (선형 탐색 -> 우선순위 큐)
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v,e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)
distance = [INF] * (v+1)

for i in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:  # 현재까지의 거리가 지금보다 작으면 무의미
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(k)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])