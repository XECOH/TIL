for tc in range(1, int(input())+1):
    n, b = map(int, input().split())
    h = list(map(int, input().split()))
    diff = 10000
    for i in range(1<<n):
        sum = 0
        for j in range(n):
            if i&(1<<j):
                sum += h[j]
        if b <= sum and sum-b < diff:
            diff = sum-b
    print(f'#{tc} {diff}')