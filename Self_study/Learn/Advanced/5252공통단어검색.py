for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    words = [input() for _ in range(N+M)]
    A = words[:N]
    B = words[N:]
    cnt = 0
    for word in A:
        if word in B:
            cnt += 1
    print('#{} {}'.format(tc, cnt))
