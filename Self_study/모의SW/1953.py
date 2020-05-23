from collections import deque

def find(t, L, cnt):
    Q = deque()
    Q.append((r, c, 1))
    dR = [-1, 0, 1, 0]
    dC = [0, 1, 0, -1]
    pipe = [[], [0, 1, 2, 3], [0, 2], [1, 3], [0, 1], [1, 2], [2, 3], [0, 3]]
    x = [[0, 3, 4, 7], [0, 2, 4, 5], [0, 3, 5, 6], [0, 2, 6, 7]]
    while Q:
        if t == L:
            break
        R, C, T = Q.popleft()
        for k in pipe[dungeon[R][C]]:
            nR, nC = R + dR[k], C + dC[k]
            if nR < 0 or nR >= n or nC < 0 or nC >= m: continue
            if dungeon[nR][nC] not in x[k] and visited[nR][nC] == 0 and T+1 <= L:
                visited[nR][nC] = 1
                Q.append((nR, nC, T+1))
                cnt += 1
    return cnt

for tc in range(1, int(input())+1):
    n, m, r, c, l = map(int, input().split())
    dungeon = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    visited[r][c] = 1
    ans = find(1, l, 1)
    print('#{} {}'.format(tc, ans))