n,k = map(int, input().split())
count = 0
while(n!=1):
    if(n%k==0):
        n /= k
    else:
        n -= 1
    count += 1

print(count)

#k로 나누는 건 1을 빼는 것보다 무조건 이득이므로 나눌 수 있을 때까지 1을 빼고, 나눌 수 있을 때마다 나누면 된다.
#이때 1씩 빼지 말고 나머지만큼 한 번에 빼면서 그만큼 count를 높이는 게 낫다.