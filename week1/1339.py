#1339: 단어 수학
'''
1. 각 알파벳이 총 얼마나 더해지는지 정리 (ex. ABC면 100*A + 10*B+ C)
2. 정리해서 많은 순으로 큰 숫자 배정
3. 합산

처음에 딕셔너리 기억 안 나서 헷갈림
'''

n = int(input())
answer = 0
weights = {} #딕셔너리

for _ in range(n):
    number = input()
    L = len(number)
    for i in range(L):
        ch = number[i]
        if ch not in weights:
            weights[ch] = 0
        weights[ch] += 10 ** (L - i - 1) #자릿수 고려

weights = list(sorted(weights.items(), key=lambda x: x[1], reverse=True)) #가중치 높은순 정렬 후 리스트로(인덱스 사용 위해)

for i in range(9, 9-len(weights), -1):
    answer += i * weights[9-i][1]

print(answer)