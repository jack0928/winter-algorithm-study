# 16496: 큰 수 만들기
'''
사전순 reverse 정렬까지는 바로 떠올랐는데, 3과 3_에서 3이 앞에 오도록 하는 부분이 생각나지 않았다.
'''
import sys
input = sys.stdin.readline

n = int(input())
numbers = input().split()

# 해당 수를 반복시켜서 10자리까지 채운다 (1,000,000,000보다 작거나 같은 음이 아닌 정수니까)
'''
'3'  → '3333333333'
'30' → '3030303030'
'''
numbers.sort(key=lambda x: x*10, reverse=True)

print(int(''.join(numbers)))
