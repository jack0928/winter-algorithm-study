#10026: 적록색약
'''
구역 구분은 DFS로 하고 (이코테 얼음 문제)
G를 R로, 혹은 R을 G로 한 뒤 다시 한 번?
-> 런타임 에러
찾아보니 전에 봤던 파이썬 재귀 깊이 문제(10000칸이 다 같은 색깔이면 너무 깊음)
-> sys.setrecursionlimit(10**7) 하니까 메모리 초과
=> DFS를 재귀 맑 다른 식으로 구현해야 할 듯
'''
from collections import deque

#각 지점에 적용할 dfs
def dfs(color, x, y):
    stack = deque([(x,y)]) #그냥 deque((x, y))로 하니까 이상하게 들어가는 듯
    visited[x][y] = 1

    while stack:
        cx,cy = stack.pop()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]: #상하좌우
            nx,ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n: #범위 확인
                if visited[nx][ny] == 0 and drawing[nx][ny] == color:
                    visited[nx][ny] = 1 # 방문 확인
                    stack.append((nx, ny))

n = int(input())
drawing = []

#그림 입력
for _ in range(n):
    line = list(input())
    drawing.append(line)

#일반적인 사람
visited = [[0]*n for _ in range(n)] #방문 확인용
normal_result = 0
#모든 그리드에서 dfs로 뻗어나가며 구역 확인
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(drawing[i][j], i, j) #이젠 True 따로 반환 안 하니까 dfs가 끝나면 구역 하나
            normal_result += 1

#G -> R
for i in range(n):
    for j in range(n):
        if drawing[i][j] == 'G':
            drawing[i][j] = 'R'


#적록색약인 사람
visited = [[0] * n for _ in range(n)]  # 방문 확인용 초기화
color_weak_result = 0
# 모든 그리드에서 dfs로 뻗어나가며 구역 확인
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(drawing[i][j], i, j)
            color_weak_result += 1

print(normal_result, color_weak_result)
