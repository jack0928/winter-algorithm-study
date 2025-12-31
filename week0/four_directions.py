n = int(input())
directions = list(input().split())
x, y = 1, 1
num = 0

#LRUD
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for direction in directions:
    if direction == 'L' and y > 1:
        num = 0
    elif direction == 'R' and y < n:
        num = 1
    elif direction == 'U' and x > 1:
        num = 2
    elif direction == 'D' and x < n:
        num = 3
    else:
        continue

    x += dx[num]
    y += dy[num]

print(x,y)