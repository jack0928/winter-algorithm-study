#find 함수를 경로 압축 기법을 통해 시간 복잡도를 개선한 경우
def find_parent(parent, x):
    if parent[x] != x: #루트 노드가 아닐 경우 부모를 타고 재귀적으로
        parent[x] = find_parent(parent, parent[x]) #parent[x]에 값을 넣는 방식으로
    return parent[x] #x에서 parent[x]로!!
'''
함수를 이렇게 수정하면 find 함수 호출 이후, 해당 노드의 루트 노드가 바로 부모 노드가 된다
본인이 루트 노드면 본인이고, 따로 부모가 있으면 나중에 합쳐질 걸 미리 빠르게 하는 느낌
-> 시간 복잡도를 개선할 수 있다
나머지 코드는 똑같이
'''

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#노드의 개수와 간선(union 연산)의 개수 입력 받기
v,e = map(int, input().split())
parent = [0] * (v+1) #부모 테이블 초기화

#처음에는 부모를 전부 자기 자신으로(즉, 연결 없음)
for i in range(1, v+1):
    parent[i] = i

#union 연산 수행
for i in range(e):
    a,b = map(int, input().split())
    union_parent(parent, a, b)

#각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end= '')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

#부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')

'''
입력 예시
6 4
1 4
2 3
2 4
5 6

출력 예시
각 원소가 속한 집합: 1 1 1 1 5 5
부모 테이블: 1 1 1 1 5 5

단, 이번에는 find 함수 개선으로 부모 테이블이 다르게 형성된다
'''