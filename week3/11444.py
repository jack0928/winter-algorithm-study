# 11444: 피보나치 수 6
'''
 1,000,000,000,000,000,000보다 작거나 같은 자연수
 -> 반복문 DP로 해도 시간/공간 복잡도 둘 다 터짐

 당연히 아래와 같은 코드는 불가
 n = int(input())

dp = [0 for _ in range(n+1)]
dp[0],dp[1] = 0,1

for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%1000000007)

그러면 O(N)으로 안 되니까 O(logN)을 써야 한다.
그렇다면 분할정복?
=> Fast Doubling Fibonacci

Fast Doubling은 피보나치 수를 절반으로 쪼개서 한 번에 두 개씩 계산하는 분할정복 기법이다.
 • 시간복잡도: O(log n)
 • n이 10¹⁸이어도 계산 가능

 <핵심 아이디어>
 - 짝수일 때
 F_{2k} = F_k \times (2F_{k+1} - F_k)
 - 홀수일 때
 F_{2k+1} = F_k^2 + F_{k+1}^2

 즉, k = n // 2만 알면 F(2k)와 F(2k+1)을 한 번에 계산

 <논리 흐름>
 - fib(n)은 (F(n), F(n+1)) 반환
 - fib(n//2) 결과로 F(2k), F(2k+1) 생성
 - n의 짝/홀에 따라 반환값 선택

'''

MOD = 1000000007

def fib(n):
    if n == 0:
        return (0, 1)

    # 절반 문제 해결
    a, b = fib(n // 2)  # a = F(k), b = F(k+1)
    '''
    n → n/2 → n/4 → n/8 → ... → 0
    -> 호출 횟수 = ⌊log₂ N⌋ + 1
    각 호출에서는 아래 Fast Doubling 공식 수행 O(1)
    
    따라서 전체 시간 복잡도
    (재귀 깊이) × (호출당 비용)
    = O(log N) × O(1)
    = O(log N)
    '''

    # Fast Doubling 공식
    c = (a * ((2 * b - a) % MOD)) % MOD   # F(2k)
    d = (a * a + b * b) % MOD             # F(2k+1)

    # 짝/홀 분기
    if n % 2 == 0:
        return (c, d)
    else:
        return (d, (c + d) % MOD)

n = int(input())
print(fib(n)[0])