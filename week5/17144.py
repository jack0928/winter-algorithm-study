# 17144: 미세먼지 안녕!
'''
일단 단순 구현 문제 같음

미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
(r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
확산되는 양은 Ar,c/5이고 소수점은 버린다. 즉, ⌊Ar,c/5⌋이다.
(r, c)에 남은 미세먼지의 양은 Ar,c - ⌊Ar,c/5⌋×(확산된 방향의 개수) 이다.
공기청정기가 작동한다.
공기청정기에서는 바람이 나온다.
위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
'''
# 확산
def diffusion(room, height, width):
    will_be_added = [[0]*width for _ in range(height)]
    dxdy = [(0,1),(0,-1),(1,0),(-1,0)]

    for i in range(height):
        for j in range(width):
            if room[i][j] > 0:
                spread = room[i][j] // 5
                diffusion_counter = 0

                for dx, dy in dxdy:
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < height and 0 <= ny < width: # 집 밖이 아니라면
                        if room[nx][ny] != -1: # 공기청정기가 아니라면
                            will_be_added[nx][ny] += spread # 확산
                            diffusion_counter += 1

                will_be_added[i][j] -= spread * diffusion_counter # 확산 후 줄어들 미세먼지

    for i in range(height):
        for j in range(width):
            room[i][j] += will_be_added[i][j] # 이번 차례의 확산 적용

# 공기청정기 작동
def air_cleaning(room, devices, height, width):
    new_room = [row[:] for row in room]   # 기존 값 복사
    up, down = devices[0][0], devices[1][0]

    # 윗부분 (반시계)
    # 오른쪽
    for i in range(1, width-1):
        new_room[up][i + 1] = room[up][i]
    # 위로
    for j in range(up, 0, -1):
        new_room[j-1][width-1] = room[j][width-1]
    # 왼쪽
    for i in range(width-1, 0, -1):
        new_room[0][i -1] = room[0][i]
    # 아래
    for j in range(0, up):
        new_room[j+1][0] = room[j][0]

    new_room[up][1] = 0   # 공청기에서 나오는 바람

    # 아랫부분 (시계)
    # 오른쪽
    for i in range(1, width - 1):
        new_room[down][i + 1] = room[down][i]
    # 아래
    for j in range(down, height - 1):
        new_room[j + 1][width-1] = room[j][width-1]
    # 왼쪽
    for i in range(width - 1, 0, -1):
        new_room[height-1][i - 1] = room[height-1][i]
    # 위로
    for j in range(height-1, down, -1):
        new_room[j - 1][0] = room[j][0]

    new_room[down][1] = 0 # 공청기에서 나오는 바람

    # 공기청정기 위치 유지
    new_room[up][0] = -1
    new_room[down][0] = -1

    return new_room


r,c,t = map(int, input().split())
house = [[] for _ in range(r)]
air_cleaner = []
for i in range(r):
    line = list(map(int, input().split()))
    if -1 in line:
        air_cleaner.append((i, 0))
    house[i] = line

# T초만큼 작업 반복
for i in range(t):
    diffusion(house, r, c)
    house = air_cleaning(house, air_cleaner, r, c)


ans = 0
for i in range(r):
    ans += sum(house[i])

print(ans + 2) # 공기청정기 때문에 -2 됐으니까