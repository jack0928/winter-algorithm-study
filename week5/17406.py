# 17406: 배열 돌리기 4
'''
배열 연산이 대충 최대 50*50이고, 주어지는 연산의 개수가 최대 6이니까
최악의 경우에 2500 * 6! = 1,800,000 -> 단순 구현?

돌릴 때 기준: 돌리려는 배열만 봤을 때(이거 기준 0부터 인덱스 다시) 대각선 2개를 제외하고, 네 구역으로 나누면 i,j 값으로 구분 가능?
-> e.g. 인덱스가 0이 아니라 1부터 있다는 가정
- i > j이고, i + j가 2*(s+1)보다 작으면 위로
- i > j이고, i + j가 2*(s+1)보다 크면 왼쪽으로
- i < j이고, i + j가 2*(s+1)보다 작으면 오른쪽으로
- i < j이고, i + j가 2*(s+1)보다 크면 아래로

- i > j이고, i + j == 2*(s+1)면 위로
- i < j이고, i + j == 2*(s+1)면 아래로
- i == j이고, i < (s+1)이면 위로
- i == j이고, i > (s+1)이면 아래로
- i == j이고, i == (s+1)이면 가만히

위로 -> new_will_be_rotated[i-1][j] = will_be_rotated[i][j]



2	3	4	5	6
3	4	5	6	7
4	5	6	7	8
5	6	7	8	9
6	7	8	9	10
이걸로 해보면 느낌 옴


1. array에서 (r,c,s) 범위만 잘라서
2. will_be_rotated에서 한 칸 회전 로직 수행하고
3. 다시 원래 array 위치에 덮어쓰기


=> 가능은 할 것 같은데 조건을 잘못 정리

이렇게 말고 몇 번째 테두리인지로 정리가 안 되나?
'''
from itertools import permutations
import copy

def rotate(array, r, c, s):
    will_be_rotated = []
    for i in range(r-s, r+s+1):
        will_be_rotated.append(array[i-1][c-s-1: c+s+1])

    new_will_be_rotated = [row[:] for row in will_be_rotated]

    size = 2*s + 1

    for i in range(size):
        for j in range(size):
            layer = min(i, j, size-1-i, size-1-j) # 몇 번째 테두리인가
            # (위쪽 거리, 왼쪽 거리, 아래쪽 거리, 오른쪽 거리)중 가장 가까운 게 그 값

            # 중심은 회전 안 하기
            if layer == s:
                continue

            top, left = layer, layer
            bottom, right = size-layer-1, size-layer-1

            ni, nj = i, j

            # 위쪽 변인 경우 (top, left ~ right-1) -> 오른쪽
            if i == top and left <= j < right:
                ni, nj = i, j+1

            # 오른쪽 변인 경우 (top ~ bottom-1, right) -> 아래
            elif j == right and top <= i < bottom:
                ni, nj = i+1, j

            # 아래쪽 변인 경우 (bottom, left+1 ~ right) -> 왼쪽
            elif i == bottom and left < j <= right:
                ni, nj = i, j-1

            # 왼쪽 변인 경우 (top+1 ~ bottom, left) -> 위
            elif j == left and top < i <= bottom:
                ni, nj = i-1, j

            new_will_be_rotated[ni][nj] = will_be_rotated[i][j]

    # 원래 array에 다시 대입
    for i in range(size):
        for j in range(size):
            array[r - s - 1 + i][c - s - 1 + j] = new_will_be_rotated[i][j]

n,m,k = map(int, input().split())
input_array = [[] for _ in range(n)]
rotations = []
answer = 1e9

# 배열 입력
for i in range(n):
    line = list(map(int, input().split()))
    input_array[i] = line

# 회전 연산 입력
for _ in range(k):
    r,c,s = map(int, input().split())
    rotations.append((r,c,s))


for perm in permutations(rotations, k):
    # 원본 배열 복사
    temp = copy.deepcopy(input_array) # 원본 배열 유지 위해 deep copy

    # 순서대로 회전 적용
    for r,c,s in perm:
        rotate(temp,r,c,s)

    # 각 행 합 계산
    for row in temp:
        answer = min(answer, sum(row))

print(answer)