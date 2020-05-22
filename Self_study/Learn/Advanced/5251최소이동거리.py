for tc in range(1, int(input())+1):
    N, E = map(int, input().split())
    graph = {i :[] for i in range(N+1)}
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
    INF = float('inf')
    d = [INF] * (N+1)
    p = [None] * (N+1)
    visited = [False] * (N+1)
    d[0] = 0
    cnt = 0
    while True:
        min = INF
        u = -1
        for i in range(N+1):
            if not visited[i] and d[i] < min:
                min = d[i]
                u = i
        visited[u] = True
        if u == N: break
        for (j, k) in graph[u]:
            if not visited[j] and d[u] + k < d[j]:
                d[j] = d[u] + k
                p[j] = u
    print('#{} {}'.format(tc, d[N]))