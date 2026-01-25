# 18428: 감시 피하기
'''
일단 N = 6이 최대 → (36-2)C3가 전체 경우의 수 34C3 = 5984
1. 그래프 탐색하면서 선생님의 위치 파악: O(N^2)인데 N <= 6이라
2. 34C3번 반복
- 해당 위치에 장애물 설치: O(3) → O(1)
- 각 선생님의 위치에서 감시 확인: O(T*(2N-1)) = O(T*N)인데 T <= 5, N <= 6이라
- 가능하면 반복 종료하고, 아니면 다음 경우 확인
=> 6000 * 5 * 6 = 180,000: 시간 충분
'''
from itertools import combinations

def observe(graph, teacher):
    found_student = False
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for i in range(4):
        current_row, current_col = teacher[0], teacher[1]
        while True:
            current_row += dx[i]
            current_col += dy[i]
            # 복도를 벗어난 경우 불가
            if current_row < 0 or current_row >= n or current_col < 0 or current_col >= n:
                break

            if graph[current_row][current_col] == 'S':
                found_student = True
                break
            elif graph[current_row][current_col] == 'O':
                break

    return found_student

n = int(input())
corridor = [[] for _ in range(n)]
teachers = []
students = []
empty = []
answer = 'NO'

for i in range(n):
    line = list(input().split())
    corridor[i] = line

# 선생님의 위치 파악
for i in range(n):
    for j in range(n):
        if corridor[i][j] == 'T':
            teachers.append((i,j))
        elif corridor[i][j] == 'S':
            students.append((i,j))
        else:
            empty.append((i,j))


# 시도해볼 장애물 조합 결정
for trial in combinations(empty, 3):
    # 장애물 설치
    for i,j in trial:
        corridor[i][j] = 'O'

    # 감시 테스트
    detected = False
    for teacher in teachers:
        if observe(corridor, teacher) == True:
            detected = True
            break

    if not detected:
        answer = 'YES'

    if answer == 'YES':
        break

    # 장애물 철거
    for i,j in trial:
        corridor[i][j] = 'X'

print(answer)