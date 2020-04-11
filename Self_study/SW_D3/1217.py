def power(N, M, k):
    global ans
    if M == k:
        return
    else:
        ans *= N
        power(N, M, k+1)

for tc in range(1, 11):
    ans = 1
    t = int(input())
    n, m = map(int, input().split())
    power(n, m, 0)
    print('#{} {}'.format(tc, ans))