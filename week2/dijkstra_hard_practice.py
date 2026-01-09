#heap을 사용해서 최단 거리가 가장 짧은 노드를 선형 탐색보다 빠르게 찾는다: O(V^2) -> O(ElogV), E는 간선의 개수
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split()) #노드의 개수, 간선의 개수
start = int(input()) #시작 노드
graph = [[] for _ in range(n+1)] #노드의 연결 정보가 들어갈 배열
visited = [False] * (n+1) #방문 여부 기록
distance = [INF] * (n+1) #처음에는 최단 거리 테이블의 값 모두 무한

#모든 간선 정보 입력
for i in range(m):
    a,b,c = map(int, input().split()) #a번 노드 -> b번 노드: 비용 c
    graph[a].append((b,c))

#이 부분이 다른 부분
def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: #큐가 비어있지 않다면
        #최단 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist,now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

#모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("도달 불가")
    else:
        print(distance[i])


'''
예시 입력
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

예시 출력
0
2
3
1
2
4
'''