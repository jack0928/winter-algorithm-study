#1717: 집합의 표현
'''
union_find_optimized 베이스로 짰는데 런타임에러(RecursionError)
-> 아마 find_parent의 재귀 부분: 최악의 경우 트리가 너무 깊게 자라서 그러는 듯
그러면 재귀 없이 구현?
'''
def find_parent(parent, x):
    while parent[x] != x:
        x = parent[x]
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int, input().split())
parent = [0] * (n+1)
answer = []

for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    x,a,b = map(int, input().split())
    if x == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent,a) == find_parent(parent,b):
            answer.append('YES')
        else:
            answer.append('NO')

for ans in answer:
    print(ans)