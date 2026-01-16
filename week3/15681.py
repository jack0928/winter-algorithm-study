# 15681: 트리와 쿼리
'''
입력 이해
9 5 3 // 정점이 9개이고(간선 9-1개), 루트 노드가 5인, 문제는 3개 나옴
1 3 // 간선 정보 시작
4 3
5 4
5 6
6 7
2 3
9 6
6 8 // 간선 정보 끝
5 // 5를 루트로 하는 서브트리에 속한 정점의 수를 구하라
4 // 4를 루트로 하는 서브트리에 속한 정점의 수를 구하라
8 // 8을 루트로 하는 서브트리에 속한 정점의 수를 구하라

dp[i]를 i번 정점을 루트로 하는 서브트리에 속한 정점의 수라고 하면 (그림 그려서 참조)
dp[1] = 1
dp[2] = 1
dp[3] = dp[1] + dp[2] + 1
dp[4] = dp[3] + 1
dp[5] = dp[4] + dp[6] + 1 // 근데 이렇게 하려면 dp[6]이 dp[5]보다 먼저 되어야 하니까 i가 이게 아닐 듯
dp[6] = dp[7] + dp[8] + dp[9] + 1
dp[7] = 1
dp[8] = 1
dp[9] = 1

정점의 레벨이 높은 애들부터 dp를 채우도록 정렬?
- 재귀 활용?
- bfs/dfs로 트리 탐색 한 번 돌리면서 각 정점별로 레벨을 확인하고 깊이가 깊은 애들부터 dp 계산?
-> 자식부터 보려면 DFS post-order?
=> post-order를 타고 돌면서 값을 계산해놓고 올라온다


예전에는 트리 탐색이라 단순히 bfs로 풀려다가 실패
'''

import sys
input = sys.stdin.readline

n,r,q = map(int, input().split())
graph = [[] for _ in range(n+1)] # 인접 리스트

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [0] * (n+1)


# 방문상태 0: 내려가는 중
# 방문상태 1: 자식 다 계산 후 올라오는 중 (post-order)
stack = [(r, 0, 0)] # (노드, 부모, 방문상태)

while stack:
    u, parent, state = stack.pop()

    if state == 0:
        stack.append((u, parent, 1)) # post-order를 위해 다시 push, 계산 후에 볼 거니까 state = 1
        for v in graph[u]:
            if v == parent: # 무방향이니까 다시 부모로 돌아갈 수 있어서 그러지 않도록
                continue
            stack.append((v, u, 0))
    else: # state == 1
        dp[u] = 1 # 자기자신 포함
        for v in graph[u]:
            if v != parent: # 각 자식들 값을 합산
                dp[u] += dp[v]

ans = []
for _ in range(q):
    x = int(input())
    ans.append(dp[x])

for res in ans:
    print(res)



'''
<메모리 초과> 재귀 DFS의 호출 스택 메모리 때문인가?
-> 스택으로 구현
import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline

n,r,q = map(int, input().split())

# 인접 리스트
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [0] * (n+1)

def dfs(u, parent):
    dp[u] = 1  # 자기 자신 포함

    for v in graph[u]:
        if v == parent: # 무방향이니까 다시 부모로 돌아갈 수 있어서 그러지 않도록
            continue
        dfs(v, u)  # 자식 먼저 계산
        dp[u] += dp[v]  # post-order로 올라가면서 누적 합

dfs(r, 0)

ans = []
for _ in range(q):
    x = int(input())
    ans.append(dp[x])

for res in ans:
    print(res)
'''