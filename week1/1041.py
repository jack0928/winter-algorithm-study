#1041: 주사위
'''
그리디 같은데 감이 안 옴
N이 3이상인 경우 주사위당 보여지는 면의 개수는 1/2/3
A<B<C<D<E<F라고 가정
=> 여기서 (A+B+C)는 합이 제일 작은 세 면의 조합, (A+B)는 합이 제일 작은 두 면의 조합, A는 가장 작은 수
1) N = 1
-> A-F 중 제일 큰 수가 있는 면을 제외한 다섯 면의 합
A+B+C+D+E
2) N = 2
-> 4(A+B+C) + 4(A+B) = 8A + 8B + 4C
3) N = 3
-> 4(A+B+C) + 4*(1+2)(A+B) + ((1*2)*4 + 1^2)A = 4(A+B+C) + 12(A+B) + 9A = 25A + 16B + 4C
4) N = 4
-> 4(A+B+C) + 4*(2+3)(A+B) + ((2*3)*4 + 2^2)A = 4(A+B+C) + 20(A+B) + 28A = 52A + 24B + 4C
5) N = 5
-> 4(A+B+C) + 4*(3+4)(A+B) + ((3*4)*4 + 3^2)A = 4(A+B+C) + 28(A+B) + 57A = 89A + 32B + 4C

=> 전개도에서 합이 제일 작은 세 면의 조합, 합이 제일 작은 두 면의 조합, 제일 작은 수를 찾아서 N에 맞게 계산
[공식]
(N>=2): 4*(합이 제일 작은 세 면의 조합) + (4*(N-2)(N-1))*(합이 제일 작은 두 면의 조합) + ((N-2)(N-1)*4 + (N-2)^2)*(가장 작은 수))
(N==1): (전체 면의 합) - (가장 큰 수)

이제 합이 제일 작은 세 면의 조합, 합이 제일 작은 두 면의 조합을 찾는 방법만 하면 끝

가능한 세 면의 조합: [ABC, ABD, ACE, ADE, FBC, FBD, FCE, FDE]
가능한 두 면의 조합: [AB, AC, AD, AE, BC, BD, BF, CE, CF, DE, DF, EF] BE가 잘못 들어갔었다

(N-2)(N-1)*4 + (N-2)^2
'''

import sys
input=sys.stdin.readline

n = int(input())
dice = list(map(int, input().split()))

com1, com2, com3 = 0, 0, 0 #combination
combinations_3 = ['012', '013', '024', '034', '125', '135', '245', '345']
combinations_2 = ['01', '02', '03', '04', '12', '13', '15', '24', '25', '34', '35', '45']
min_com3 = 150
min_com2 = 100
min_com1 = 100

for combination in combinations_3:
    result = 0
    for i in range(3):
        result += dice[int(combination[i])]

    if result <= min_com3:
        min_com3 = result

com3 = min_com3

for combination in combinations_2:
    result = 0
    for i in range(2):
        result += dice[int(combination[i])]

    if result <= min_com2:
        min_com2 = result

com2 = min_com2

com1 = min(dice)

if n == 1:
    answer = sum(dice) - max(dice)
else:
    answer = 4*com3 + 4*((n-2)+(n-1))*com2 + ((n-2)*(n-1)*4 + (n-2)*(n-2))*com1 #공식

print(answer)