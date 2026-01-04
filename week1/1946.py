#1946: 신입사원
'''
일단 서류 기준 정렬
-> 1등인 애는 무조건 통과: 얘를 기준?
'''
import sys
input=sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    answer = 0
    applicants = []
    for _ in range(n):
        resume,interview = map(int, input().split())
        applicants.append((resume, interview))

    applicants.sort() #서류심사순 정렬: 처음 애 뒤에 오는 애들은 무조건 서류에서 뒤떨어지므로 인터뷰에서 얘를 이겨야 함

    answer += 1 #서류 심사 1등한 애
    interview_standard = applicants[0][1] #서류 1등의 인터뷰를 최초 기준으로

    for rank in applicants:
        if rank[1] < interview_standard:
            answer += 1
            interview_standard = rank[1] #새로 추가된 애보다 서류가 떨어지므로 얘보다 높은 인터뷰를 해야 함(당연히 얘의 인터뷰 순위가 최초보다 높음)

    print(answer)



