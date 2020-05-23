import heapq

for tc in range(1, int(input())+1):
    v, e = map(int, input().split())
    graph = { i: [] for i in range(v+1) }
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    INF = float('inf')
    key = [INF] * (v+1)
    mst = [False] * (v+1)
    pq = []
    key[1] = 0
    heapq.heappush(pq, (0, 1))
    ans = 0
    while pq:
        k, node= heapq.heappop(pq)
        if mst[node] : continue
        mst[node] = True
        ans += k
        for v, val in graph[node]:
            if not mst[v] and key[v] > val:
                key[v] = val
                heapq.heappush(pq, (val, v))
    print('#{} {}'.format(tc, ans))