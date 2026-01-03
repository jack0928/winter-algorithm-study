from collections import deque

graph = {
    'A': ['B','G'],
    'B': ['C','D','E'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': ['H'],
    'H': ['I'],
    'I': [],
}

def dfs(graph, node):
    visited = []
    stack = deque()

    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        print(s, end=' ')

        for child in reversed(graph[s]):
            if child not in visited:
                visited.append(child)
                stack.append(child)


def bfs(graph, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        q = queue.pop(0)
        print(q, end=' ')

        for child in graph[q]:
            if child not in visited:
                visited.append(child)
                queue.append(child)

dfs(graph, 'A')
print('\n')
bfs(graph, 'A')
