# 2138: 전구와 스위치
'''
i번을 누를 때마다 또다시 i개의 선택지가 생기는 트리를 백트래킹?
-> 백트래킹 하기에도 선택지가 너무 많지 않나?

그리디?

000
110(1)
001(2)
010(3)

000
111(2)
001(1)
010(3)

000
110(1)
101(3)
010(2)

000
011(3)
101(1)
010(2)

000
111(2)
100(3)
010(1)

000
011(3)
101(1)
010(2)

-> 스위치를 누르는 순서는 중요하지 않은 것 같다.
- 그렇다면 같은 스위치를 2번 누르면 결국 원래랑 똑같으니 의미가 없는 게 아닌가?
- 그러면 각 스위치를 누를까 말까만 결정하면 된다.
=> 이걸 어떻게 판단하느냐만 알아내면 끝
근데 앞에서부터 순서대로 누른다고 가정했을 때, i+1번까지 누르고 나면, i번 버튼은 더 이상 바꿀 수 없다.
-> 앞에서 눌렀냐에 따라 자동으로 뒤에 것이 정해지나?

00000 -> 11111
1번째: 눌러야 하나? -> 11로 가야하니 누르자
2번째: 눌러야 하나? -> 1번 전구가 1로 유지되어야 하니 누르지 말자
3번째: 눌러야 하나? -> 2번 전구가 1로 유지되어야 하니 누르지 말자
4번째: 눌러야 하나? -> 3번 전구가 1로 바뀌어야 하니 누르자
5번째: 눌러야 하나? -> 4번 전구가 1로 유지되어야 하니 누르지 말자
=> 2번
- 근데 첫번째 버튼은 어떻게 선택하지? 같으면 누르지 말고, 다르면 눌러야 하나?
-> 그건 아니다. 예제 입력을 보면 0으로 시작해서 0으로 끝나지만 첫번째 버튼을 눌러야 한다.

000 -> 010
1번째: 눌러야 하나? -> 0이니 누르지 말자로 하면 틀림. 왜 눌러야 할까? 일단 누르고 넘어가자
2번째: 눌러야 하나? -> 1번 전구가 0이 되어야 하니 누르자 001
3번째: 눌러야 하나? -> 2번 전구가 1이 되어야 하니 누르자

아니면 첫 번째 전구를 누르는 경우, 안 누르는 경우 둘 다 해보고 결정?
일단 해보자


'''
n = int(input())
start = list(map(int, input()))
end = list(map(int, input()))

start_first_yes = start[:]
start_first_no = start[:]
ans1, ans2 = 0,0

# 1,0 뒤집기
# x = 1 - x
def press(switches, i):
    if i == n-1:
        switches[i - 1] = 1 - switches[i - 1]
        switches[i] = 1 - switches[i]
    elif i == 0:
        switches[0] = 1 - switches[0]
        switches[1] = 1 - switches[1]
    else:
        switches[i - 1] = 1 - switches[i - 1]
        switches[i] = 1 - switches[i]
        switches[i + 1] = 1 - switches[i + 1]

# 첫번째를 누르는 경우
# print(start_first_yes, 0)
# print("case press")
press(start_first_yes, 0)
ans1 += 1

for i in range(1, n):
    # print(start_first_yes, i)
    if start_first_yes[i-1] != end[i-1]: # 앞의 전구가 바뀌어야 하면 누르자
        # print("press!", i)
        press(start_first_yes, i)
        ans1 += 1


# print('------------------------')

# 첫번째를 안 누르는 경우
# print(start_first_no, 0)
# print("case not press")

for i in range(1, n):
    # print(start_first_no, i)
    if start_first_no[i-1] != end[i-1]: # 앞의 전구가 바뀌어야 하면 누르자
        # print("press!", i)
        press(start_first_no, i)
        ans2 += 1



# print('------------------------')
# print('------------------------')

# print(start_first_yes, ans1)
# print(start_first_no, ans2)

ans = []
if start_first_yes == end:
    ans.append(ans1)
if start_first_no == end:
    ans.append(ans2)
if len(ans) == 0:
    print(-1)
else:
    print(min(ans))