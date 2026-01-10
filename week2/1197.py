#1197: 최소 스패닝 트리
'''
런타임에러 나서
'''
# 루트 노드를 찾는 함수
def find_parent(parent, x):
    while parent[x] != x:
        x = parent[x]
    return x


# 합집합 연산하는 함수
def union_find(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int, input().split())
parent = [0] * (v+1)

edges = []
result = 0

for i in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost, a, b))

for i in range(1, v+1):
    parent[i] = i

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_find(parent, a, b)

print(result)
