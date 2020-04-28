def find(r, c, t):
    global minT
    if t > minT:
        return
    if r == c == n-1:
        if t < minT:
            minT = t
        return
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    st = []
    for k in range(4):
        if r+dr[k] < 0 or r+dr[k] >= n or c+dc[k] < 0 or c+dc[k] >= n :

for tc in range(1, int(input())+1):
    n = int(input())
    maps = [list(map(int, input())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    minT = 100000
    find(0, 0, 0)
    print('#{} {}'.format(tc, minT))