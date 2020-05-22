for tc in range(1, int(input())+1):
    v, e = map(int, input().split())
    adj = [[0] * (v+1) for _ in range(v+1)]
    for _ in range(e):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w
        adj[n2][n1] = w
    INF = float('inf')
    key = [INF] * (v+1)
    p = [None] * (v+1)
    mst = [False] * (v+1)
    key[0] = 0
    cnt = 0
    result = 0
    while cnt < v+1:
        min = INF
        u = -1
        for i in range(v+1):
            if not mst[i] and key[i] < min:
                min = key[i]
                u = i
        mst[u] = True
        result += min
        cnt += 1
        for j in range(v+1):
            if adj[u][j] > 0 and not mst[j] and key[j] > adj[u][j]:
                key[j] = adj[u][j]
                p[j] = u
    print('#{} {}'.format(tc, result))