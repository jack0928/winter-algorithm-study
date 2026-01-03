#1260: DFS와 BFS
from collections import deque

def dfs(graph, node):
    visited = [False] * (n + 1)
    stack = deque()

    stack.append(node)

    while stack:
        v = stack.pop() #LIFO
        if visited[v]: #visted 체크를 아래쪽 반복문에서 하고 false인 애들만 넣기에 없어도 가능은 할 듯
            continue

        visited[v] = True
        print(v, end=' ')

        for child in reversed(graph[v]):
            if not visited[child]:
                stack.append(child)


def bfs(graph, node):
    visited = [False] * (n + 1)
    queue = deque()

    queue.append(node)

    while queue:
        v = queue.popleft() #FIFO
        if visited[v]:
            continue

        visited[v] = True
        print(v, end=' ')

        for child in graph[v]:
            if not visited[child]:
                queue.append(child)


n,m,v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
for i in range(1, n+1):
    graph[i].sort()

dfs(graph, v)
print('\n', end='')
bfs(graph, v)