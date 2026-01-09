#13549: 숨바꼭질
'''
-1,+1,*2의 3개의 child로 확장되는 단순 구조 트리에 대한 BFS?
-> 가장 빠른 시간(가장 얕은 레벨) 찾는 거니까 BFS
-> 단, 순간이동은 0초 (순간이동의 우선순위가 높은가)
-> 비용이 여러 개니까 다익스트라?
아무튼 순간이동의 레벨이 걷기보다는 낮아야 함
BFS에서는 먼저 들어온 애들이 거리도 짧았는데 이제는 그런 게 안 통함
-> 큐에 넣는 순서를 거리에 맞춰서 해주면?
=> 순간이동은 큐의 앞쪽에, 걷기는 큐의 뒷쪽에 넣는다!!
'''
from collections import deque

def bfs(start, end):
    distance = [-1] * 200001
    queue = deque([start])
    distance[start] = 0

    while queue:
        v = queue.popleft()
        if v == end:
            return distance[v]

        #순간이동
        if 0 <= 2 * v <= 100001 and distance[2 * v] == -1:
            distance[2 * v] = distance[v]
            queue.appendleft(2 * v)

        #걷기
        for next_v in (v - 1, v + 1):
            if 0 <= next_v <= 100001 and distance[next_v] == -1:
                distance[next_v] = distance[v] + 1
                queue.append(next_v)

    return abs(end-start)

n,k = map(int, input().split())

print(bfs(n,k))