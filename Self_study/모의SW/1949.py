def find(r, c, cnt, t):
    global ans
    if cnt > ans:
        ans = cnt
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for d in range(4):
        nr, nc = r+dr[d], c+dc[d]
        if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
        if maps[nr][nc] < maps[r][c]:
            visited[r][c] = 1
            find(nr, nc, cnt+1, t)
        else:
            diff = maps[nr][nc]-maps[r][c]
            if diff <= t:
                visited[r][c] = 1
                find(nr, nc, cnt+1, t-maps[nr][nc]-maps[r][c])
            else: continue

for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    pick = 0
    ans = 0
    for i in range(n):
        if pick < max(maps[i]):
            pick = max(maps[i])
    for i in range(n):
        for j in range(n):
            if maps[i][j] == pick:
                visited = [[0]*n for _ in range(n)]
                find(i, j, 0, k)
    print('#{} {}'.format(tc, ans))