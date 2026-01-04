#1715: 카드 정렬하기
'''
a,b,c
-> (a+b) + ((a+b) + c) = 2a + 2b + c
-> (a+c) + ((a+c) + b) = 2a + b + 2c
=> 그냥 크기순으로 나열하고 하나씩 더하면 되나?

a,b,c,d
-> (a+b) + ((a+b) + c) + ((a+b+c) + d) = 3a + 3b + 2c + d
-> (a+b) + (c+d) + ((a+b) + (c+d)) = 2a + 2b + 2c + 2d도 있음
=> 이럴 경우 (a+b)와 d간의 대소에 따라 달라지므로 단순 크기순 나열 후 합산은 안 됨
그렇다면 매번 가장 적은 카드 묶음 2개를 고르면 되지 않을까?
-> 다 매번 정렬하고 하면 N * O(NlogN) = O(N^2 logN)인데 N이 100000이므로 불가
-> 다 매번 탐색으로 찾아도 N * O(N) = O(N^2)이므로 얘도 불가
-> 우선순위 큐 같은 자료구조 활용하면 빠를 것 같음
=> 힙 쓰면 대충 N * (O(logN) + O(logN)) = O(NlogN)이라 가능
따라서 최소 힙 만들어서 푸는 문제인데 놀랍게도 파이썬은 heap 라이브러리도 제공
'''
import heapq
import sys

input = sys.stdin.readline

heap = []
answer = 0

n = int(input())

for _ in range(n):
    card = int(input())
    heapq.heappush(heap, card)

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    result = a+b
    answer += result
    heapq.heappush(heap, result)

print(answer)
