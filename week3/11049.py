# 11049: 행렬 곱셈 순서
'''
3-1 알고리즘 DP 파트에서 나왔던 Chained Matrix Multiplication
-> 2차원 배열 DP

M[i,j] = min{ M[i,k] + M[k+1,j] + C(i−1)C(k)C(j) }
for i <= k <= j-1. // k를 하나씩 올려가며
M[i,i] = 0


'''
import sys
input = sys.stdin.readline
INF = 2**31
n = int(input())
matrices = []

# dp[i][j] = i번 행렬부터 j번 행렬까지 곱하는 최소 연산 횟수
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(n):
    r, c = map(int, input().split())
    matrices.append((r, c))

# 구간 길이 (행렬 곱셈이니까 2부터 시작)
for length in range(2, n+1): # length = 구간에 포함된 행렬의 개수
    for i in range(1, n - length + 2): # i = 구간의 시작 인덱스
        j = i + (length - 1) # j = 구간의 끝
        dp[i][j] = INF

        for k in range(i, j):
            # M[i,j] = min{ M[i,k] + M[k+1,j] + C(i−1)C(k)C(j) }
            cost = dp[i][k] + dp[k+1][j] + matrices[i-1][0] * matrices[k-1][1] * matrices[j-1][1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[1][n])