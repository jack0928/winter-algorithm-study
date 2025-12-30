n,m,k = map(int, input().split())
numbers = list(map(int, input().split()))
answer1, answer2 = 0, 0

numbers.sort(reverse=True)

#효과적인 방법
first = numbers[0]
second = numbers[1]

count = int(m/(k+1)) * k
count += m % (k+1)

answer2 = (count) * first
answer2 += (m - count) * second


#간단한 방법
k_count = k

while(m>0):
    if k_count == 0:
        k_count = k
        answer1 += numbers[1]
    else:
        answer1 += numbers[0]
        k_count -= 1
    m -= 1

print(answer1, answer2)