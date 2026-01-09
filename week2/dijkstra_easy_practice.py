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

#방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 #가장 최단 거리가 짧은 노드
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
        distance[j[0]] = j[1] #distance[b] = c: b까지의 거리가 c인 거니까

    for i in range(n-1): #시작 노드를 제외한 전체 노드
        #현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        #현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            #현재 노드를 거쳐서 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

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