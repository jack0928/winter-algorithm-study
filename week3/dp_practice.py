'''
1. 재귀
- 재귀(그냥 재귀): 같은 부분 문제를 또 계산함 → 느려질 수 있음

시간복잡도: 대략 O(2^n)

fib(5)를 구할 때
 • fib(3)이 여러 번,
 • fib(2)는 더 여러 번 계산됨.

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

2. DP Top-down(메모이제이션): 재귀 + 저장

한 번 구한 fib(k)는 딱 1번만 계산.

시간복잡도: O(n)

memo = {}
def fib(n):
    if n <= 2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

3. DP Bottom-up(테이블): 반복문 + 저장

재귀 호출 없이, 작은 것부터 쌓아감.

시간복잡도: O(n)
(백준에서 보통 이게 가장 안정적)

def fib(n):
    dp = [0]*(n+1)
    dp[1] = 1
    if n >= 2:
        dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


“재귀 = 느림”은 오해 (중요)

재귀가 느린 게 아니라,
 • 중복 부분 문제가 있을 때
 • 저장을 안 하면 느린 거야.

즉,
 • 중복 없는 재귀(예: 트리 DFS)는 충분히 빠를 수 있음.
 • 중복 있는 재귀(피보나치, 계단 오르기, 최적화 문제 등)는 DP가 필요.


DP 푸는 사고 순서 (⭐ 중요)

① 상태 정의 (State)
 • dp[i] = i번째까지 고려했을 때의 답

② 점화식 (Transition)
 • 이전 상태로부터 현재 상태 계산
 • 예:
dp[i] = dp[i-1] + dp[i-2]

③ 초기값 (Base Case)
 • 가장 작은 문제의 답
 • 예:
dp[1] = 1, dp[2] = 1

④ 계산 순서
 • 작은 문제 → 큰 문제


'''

def recursive_fib(n):
    if n <= 2:
        return 1
    return recursive_fib(n-2) + recursive_fib(n-1)


memo = {}
def top_down_dp_fib(n):
    if n <= 2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = top_down_dp_fib(n - 1) + top_down_dp_fib(n - 2)
    return memo[n]


def bottom_up_dp_fib(n):
    dp = [0]*(n+1)
    dp[1] = 1
    if n>=2:
        dp[2] = 1

    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
