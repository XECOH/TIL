def find(R, C, t, L):
    global ans
    dR = [-1, 0, 1, 0]
    dC = [0, 1, 0, -1]
    if t == L: return
    else:
        if visited[R][C] != 0: return
        else:
            visited[R][C] = 1
            if dungeon[R][C] == 1:
                for k in range(4):
                    nR, nC = R + dR[k], C + dC[k]
                    if nR < 0 or nR >= m or nC < 0 or nC >= n: continue
                    if dungeon[nR][nC] != 0 and visited[nR][nC] == 0:
                        ans += 1
                        find(nR, nC, t+1, L)
            elif dungeon[R][C] == 2:
                for k in range(0, 4, 2):
                    nR, nC = R + dR[k], C + dC[k]
                    if nR < 0 or nR >= m or nC < 0 or nC >= n: continue
                    if dungeon[nR][nC] != 0 and visited[nR][nC] == 0:
                        ans += 1
                        find(nR, nC, t+1, L)
            elif dungeon[R][C] == 3:
                for k in range(1, 4, 2):
                    nR, nC = R + dR[k], C + dC[k]
                    if nR < 0 or nR >= m or nC < 0 or nC >= n: continue
                    if dungeon[nR][nC] != 0 and visited[nR][nC] == 0:
                        ans += 1
                        find(nR, nC, t+1, L)
            elif dungeon[R][C] == 4:
                for k in range(1, 3):
                    nR, nC = R + dR[k], C + dC[k]
                    if nR < 0 or nR >= m or nC < 0 or nC >= n: continue
                    if dungeon[nR][nC] != 0 and visited[nR][nC] == 0:
                        ans += 1
                        find(nR, nC, t+1, L)
            elif dungeon[R][C] == 5:
                for k in range(1, 3):
                    nR, nC = R + dR[k], C + dC[k]
                    if nR < 0 or nR >= m or nC < 0 or nC >= n: continue
                    if dungeon[nR][nC] != 0 and visited[nR][nC] == 0:
                        ans += 1
                        find(nR, nC, t+1, L)
            elif dungeon[R][C] == 6:
                for k in range(2, 4):
                    nR, nC = R + dR[k], C + dC[k]
                    if nR < 0 or nR >= m or nC < 0 or nC >= n: continue
                    if dungeon[nR][nC] != 0 and visited[nR][nC] == 0:
                        ans += 1
                        find(nR, nC, t+1, L)
            elif dungeon[R][C] == 7:
                for k in range(0, 4, 3):
                    nR, nC = R + dR[k], C + dC[k]
                    if nR < 0 or nR >= m or nC < 0 or nC >= n: continue
                    if dungeon[nR][nC] != 0 and visited[nR][nC] == 0:
                        ans += 1
                        find(nR, nC, t+1, L)
    return

for tc in range(1, int(input())+1):
    n, m, r, c, l = map(int, input().split()) # 세로, 가로, 맨홀 뚜껑 세로, 맨홀 뚜껑 가로, 탈출 소요 시간
    dungeon = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    ans = 0
    find(r, c, 0, l)
    print('#{} {}'.format(tc, ans))