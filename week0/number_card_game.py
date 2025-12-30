n,m = map(int, input().split())
#board = [[] for _ in range(n)]
numbers = []

for i in range(n):
    cards = list(map(int, input().split()))
    # board[i] = cards
    numbers.append(min(cards))

print(max(numbers))