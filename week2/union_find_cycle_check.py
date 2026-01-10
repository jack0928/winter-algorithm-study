#서로소 집합은 '무방향' 그래프 내에서의 사이클 판별에 사용할 수 있다(방향 그래프는 DFS)
'''
union 연산은 간선으로 표현될 수 있다. 따라서 간선을 하나씩 확인하면서 두 노드가 포함되어 있는 집합을 합치는 걸 반복하면 사이클을 판별할 수 있다.
각 간선을 확인하며 두 노드의 루트 노드 확인
1. 루트 노드가 서로 다르다면 union 연산 수행
2. 루트 노드가 같다면 사이클이 발생한 것
'''

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
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
parent = [0] * (v+1) # 부모 테이블 초기화

# 처음에는 부모를 전부 자기 자신으로(즉, 연결 없음)
for i in range(1, v+1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a,b = map(int, input().split())
    # 사이클이 발생하면 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 없음")


'''
예시 입력
3 3
1 2
1 3
2 3

예시 출력
사이클 발생
'''