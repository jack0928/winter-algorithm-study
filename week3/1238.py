# 1238: 파티

'''
단순하게 다익스트라로 각각 도시에서 X까지의 최단 거리를 구하고,
왕복이니까 그게 가장 큰 경우의 값 * 2 ?
-> 단방향 그래프니까 단순히 2배는 아니다.
+ 매 도시마다 다익스트라를 하면 O(N·M log N)이라 안 됨

필요한 값
- 각 도시에서 X까지의 최단 거리
- X에서 각 도시까지의 최단 거리: 얘는 다익스트라 한 번에 가능
각 배열을 구해서 합한 것의 max 값이 정답
(단방향이니까 i -> X, X -> i를 각각 따로 구해야 함)

'각 도시에서 X까지의 최단 거리'를 더 빨리 구하는 방법이 없나?
- 각 도시에서 다익스트라는 안 됨
- X에서 각 도시까지의 최단 거리는 빠르게 구할 수 있으니까, 그래프의 방향을 뒤집어서
다익스트라 한 번 하면 거리를 구할 수 있지 않나?

1. X에서 각 도시까지의 최단 거리 (다익스트라)
2. 그래프 방향 뒤집기
3. X에서 각 도시까지의 최단 거리 (다익스트라, 사실상 각 도시 -> X)
4. 최단 거리 배열 2개 합쳐서 정답 구하기

'''
import heapq
INF = int(1e9)

n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
reversed_graph = [[] for _ in range(n+1)]

distances = []
reversed_distances = []

for i in range(m):
    start,end,time = map(int, input().split())
    graph[start].append((end,time))
    reversed_graph[end].append((start,time))

def dijkstra(start, graph):
    distance = [INF] * (n+1)

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

# X -> 모든 도시
dist_from_x = dijkstra(x, graph)

# 모든 도시 -> X
dist_to_x = dijkstra(x, reversed_graph)

# 왕복 시간 최대값
answer = 0
for i in range(1, n+1):
    answer = max(answer, dist_from_x[i] + dist_to_x[i])

print(answer)