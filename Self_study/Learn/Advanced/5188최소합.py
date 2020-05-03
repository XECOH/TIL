def find(r, c, e, hap):
    global minS
    dr = [0, 1]
    dc = [1, 0]
    if r == c == e:
        hap += table[r][c]
        if minS > hap:
            minS = hap
            return
    if hap > minS :
        return
    for d in range(2):
        if r+dr[d] < 0 or r+dr[d] >= n or c+dc[d] < 0 or c+dc[d] >= n: continue
        find(r+dr[d], c+dc[d], e, hap+table[r][c])

for tc in range(1, int(input())+1):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]
    minS = 130
    find(0, 0, n-1, 0)
    print('#{} {}'.format(tc, minS))