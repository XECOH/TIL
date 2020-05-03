def find(s, con, t):
    global minC
    visited[s] = 1
    if minC < con:
        return
    if t == n-1:
        con += table[s][0]
        if minC > con:
            minC = con
            return
    for e in range(1, n):
        if s == e: continue
        if visited[e] != 0: continue
        find(e, con+table[s][e], t+1)
        visited[e] = 0

for tc in range(1, int(input())+1):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]
    minC = 1000
    for e in range(1, n):
        visited = [0] * n
        find(e, table[0][e], 1)
    print('#{} {}'.format(tc, minC))