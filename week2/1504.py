# 1504: 특정한 최단 경로
'''
일단 단순하게 생가해봤을 때는 start -> v1, v1 -> v2, v2 -> end를 각각 최단 경로로 가면 될 것 같다.
최단 경로 알고리즘은?

<시간복잡도>
다익스트라: O(V^2)
개선 다익스트라: O(ElogV)
플로이드-워셜: O(N^3)

이때 문제에서 N은 최대 800, E는 최대 200,000
따라서 최악의 경우
다익스트라: 640,000
개선 다익스트라: 대충 2,000,000
플로이드 워셜: 512,000,000
-> 다익스트라는 각 경우에 대해 계산해야 되니까 3을 곱한다고 해도 얘는 다익스트라인 것 같다.

근데 다익스트라는 방문처리를 하니까 visited 리스트를 매 계산마다 초기화 해야 한다
Ex) start -> v1 끝나고 초기화 후 v1 -> v2

바로 틀림 -> 다익스트라는 아닌 것 같다


맞는데 몇 가지 실수가 있었다.
1. 코드 바꾸면서 visited랑 distance 초기화 누락
2. v1,v2 말고 v2,v1도 가능한 거였다

'''

# [오답 원인 정리]
# 이 코드는 다익스트라 알고리즘 자체의 문제가 아니라, 다익스트라를 여러 번 호출하면서
# distance와 visited 배열을 매번 초기화하지 않고 재사용한 것이 문제였다. - 밥 먹으러 가면서 코드 수정하다가 생긴 문제
# 이전 다익스트라 실행 결과가 다음 실행에 그대로 남아 있어 최단 거리 계산이 왜곡되었고,
# 특히 visited 배열이 이미 True로 설정된 상태에서 다시 탐색을 시도해 정상적인 탐색이 불가능했다.
# 다익스트라는 각 시작 정점마다 독립적인 최단 거리 계산이 필요하므로,
# distance와 visited는 반드시 매 실행마다 새로 생성하거나 초기화해야 한다.


# 다익스트라 알고리즘 (배열 기반)
# - 매 단계마다 방문하지 않은 정점 중 최단 거리를 선형 탐색
# - 시간 복잡도: O(V^2)
# - 구현은 단순하지만, Python에서는 for문 중첩으로 인해 느릴 수 있음
# - 정점 수가 작고 간선 수가 적을 때만 실용적

# 개선 다익스트라 (우선순위 큐 / heapq 사용)
# - 최단 거리 정점을 힙에서 바로 꺼냄
# - 시간 복잡도: O(E log V)
# - heap 연산은 C로 구현되어 Python에서도 매우 빠름
# - 간선 수가 많거나 (E가 큼), BOJ 그래프 문제에서 표준적인 선택
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


# 개선 다익스트라 (heapq 사용)
def dijkstra(start):
    distance = [INF] * (n+1)
    pq = []

    distance[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        dist, now = heapq.heappop(pq)

        # 이미 더 짧은 경로가 있으면 무시
        if distance[now] < dist:
            continue

        for nxt, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[nxt]:
                distance[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))

    return distance

# 3번만 다익스트라 실행
dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

# 경로 1: 1 → v1 → v2 → n
path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]

# 경로 2: 1 → v2 → v1 → n
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]

answer = min(path1, path2)

print(answer if answer < INF else -1)

'''
dijkstra(1)
if distance[v1] != INF:
    total_distance += distance[v1]
else:

visited = [False] * (n+1) #방문 여부 초기화
dijkstra(v1)
total_distance += distance[v2]
visited = [False] * (n+1) #방문 여부 초기화
dijkstra(v2)
total_distance += distance[n]'''