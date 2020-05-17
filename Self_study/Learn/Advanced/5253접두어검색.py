for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    words = [input() for _ in range(N+M)]
    A = words[:N]
    B = words[N:]
    As = set()
    for i in range(N):
        for j in range(len(A[i])):
            As.add(A[i][:j+1])
    cnt = 0
    for word in B:
        if word in list(As):
            cnt += 1
    print('#{} {}'.format(tc, cnt))
