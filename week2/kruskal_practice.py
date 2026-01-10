'''
신장 트리(Spanning Tree): 하나의 그래프가 있을 때
1. 모든 노드를 포함하면서 (트리)
2. 사이클이 존재하지 않는 (트리)
3. 부분 그래프
를 신장 트리라고 한다.

우리는 가능한 한 최소 비용으로 신장 트리를 찾아야 할 때가 있다.
예를 들어, N개의 도시가 있을 때, 모든 도시를 연결하는 최소 비용을 구하는 경우와 같은 경우

이럴 때 필요한 게 '최소 신장 트리(MST: Minimum Spanning Tree) 알고리즘'이다.
대표적으로 Kruskal 알고리즘이 있다.

이는 그리디 알고리즘으로 분류되는데, 먼저 모든 간선에 대하여 정렬을 수행한 뒤,
가장 거리가 짧은 간선부터 집합에 포함시키면 된다. (이때, 사이클을 발생시킬 수 있다면 집합에 포함시키지 않는다)

1. 간선 데이터를 비용에 따라 오름차순으로 정렬
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
-> 사이클이 발생하지 안을 때만 MST에 포함
3. 모든 간선에 2번 과정 반복 적용
'''
from encodings.punycode import decode_generalized_number


# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x: #루트 노드가 아닐 경우 부모를 타고 재귀적으로
        parent[x] = find_parent(parent, parent[x]) #parent[x]에 값을 넣는 방식으로
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력 받기
v,e = map(int, input().split())
parent = [0] * (v+1) #부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

#처음에는 부모를 전부 자기 자신으로(즉, 연결 없음)
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a,b,cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost,a,b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

'''
예시 입력
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

출력 예시
159
'''