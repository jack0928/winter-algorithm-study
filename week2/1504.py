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


'''
import sys
input = sys.stdin.readline
INF = int(1e9)

n,e = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

total_distance = 0

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))

v1, v2 = map(int, input().split())

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index

#다익스트라 알고리즘
def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


route = [(1,v1), (v1,v2), (v2,n)]
error_flag = 0

for start, end in route:
    dijkstra(start)
    if distance[end] != INF:
        total_distance += distance[end]
    else:
        print(-1)
        error_flag = 1
        break


if error_flag == 0:
    print(total_distance)

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