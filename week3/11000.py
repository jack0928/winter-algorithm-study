# 11000: 강의실 배정
'''
일단 수업을 안 듣는 경우는 없으니
dp[i] = i번째 수업까지 포함했을 때 '지금까지' 사용한 강의실의 수?
라고 생각해보자

일단 dp를 돌 때 현재 강의실의 수와 max 값을 유지해야 하는가?

현재까지 빌린 강의실 수 classroom
가용 가능 강의실 수 avaliable_classroom


if (모든 강의실이 운영 중):
    dp[i] = dp[i-1] + 1
else:
    dp[i] = dp[i-1]

필요한 정보
- 빌린 강의실 수
- 사용 중인 강의실 수
- 현재 진행 중인 수업이 끝나는 시간

-> 이건 DP가 아니지
---------------------------------------------------------------------------------
혹시 DP가 아닌가?

일단 필요한 정보
- 강의실을 몇 개 썼는지
- 각 강의실이 언제 끝나는지

근데 그냥 매번 가장 빨리 끝나는 강의실 찾아서 하면 안 되나? (그리디)

1. 현재 가장 빨리 끝나는 수업 찾기
2. 해당 수업의 종료시간이 이번에 들어온 수업보다 빠르면 유지, 아니면 추가


for s,t in classes[1:]:
    # 종료시간 중에 min 찾아서 그 값이 이번의 s보다 같거나 빠르면 room 유지, 아니면 +1
    # 현재 s,t running에 추가
    # 종료시간 기준 running 정렬
    # 종료 시간이 s 보다 빠르면 running에서 삭제

'''
import heapq

n = int(input())
classes =[]
room = 1

for _ in range(n):
    s,t = map(int, input().split())
    classes.append((s,t))

classes.sort()
running = [] # 운영 중인 수업: 종료 시간만 알면 됨
heapq.heappush(running, classes[0][1])

for s,t in classes[1:]:
    # 끝난 수업들 종료
    while running and running[0] <= s: # 진행 중인 수업이 있고, 그 중 종료 시간이 현재 수업 시작 시간보다 빠른 게 있다면
        fastest_available_time = heapq.heappop(running) # 그 수업은 종료 시키고

    heapq.heappush(running, t) # 현재 t running에 추가

    # 끝난 수업들 종료하고 현재 수업 추가하면 현재 수업이 들어왔을 때 운영 중인 강의실 수를 알 수 있다
    room = max(room, len(running))

print(room)