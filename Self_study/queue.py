#5102

def find(sn, en, cnt):
    global visited
    if graph[sn][en] == 1:
        return cnt
    else:
        for i in range(1, v + 1):
            if visited[sn] != 1 and graph[sn][i] == 1:
                visited[sn] = 1
                find(i, en, cnt + 1)
                visited[sn] = 0


for tc in range(int(input())):
    v, e = map(int, input().split())
    graph = [[0 for _ in range(v + 1)] for _ in range(v + 1)]
    for i in range(e):
        nod1, nod2 = map(int, input().split())
        graph[nod1][nod2] = 1
        graph[nod2][nod1] = 1
    s, g = map(int, input().split())
    visited = [0] * (v + 1)
    find(s, g, 0)
    print('#{} {}'.format(tc + 1, find(s, g, 0)))