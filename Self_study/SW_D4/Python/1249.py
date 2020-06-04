from collections import deque

def find():
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    while Q:
        [sr, sc] = Q.popleft()
        for k in range(4):
            nr, nc = sr+dr[k], sc+dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if visited[sr][sc] + maps[nr][nc] < visited[nr][nc]:
                    visited[nr][nc] = visited[sr][sc] + maps[nr][nc]
                    Q.append([nr, nc])

for tc in range(1, int(input())+1):
    n = int(input())
    maps = [list(map(int, input())) for _ in range(n)]
    inf = float('INF')
    visited = [[inf]*n for _ in range(n)]
    visited[0][0] = 0
    Q = deque()
    Q.append([0, 0])
    find()
    print(f'#{tc} {visited[n-1][n-1]}')