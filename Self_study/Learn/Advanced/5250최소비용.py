from collections import deque

for tc in range(1, int(input())+1):
    n = int(input())
    regions = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    Q = deque()
    Q.append((0, 0, 0))
    minE = 100000000000000
    while Q:
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        sr, sc, expenditure = Q.popleft()
        visited[sr][sc] = 1
        for d in range(4):
            if sr+dr[d] < 0 or sr+dr[d] >= n or sc+dc[d] < 0 or sc+dc[d] >= n: continue
            if sr == sc == n-1:
                if minE > expenditure:
                    minE = expenditure
            else:
                if visited[sr+dr[d]][sc+dc[d]] != 1:
                    diff = regions[sr+dr[d]][sc+dc[d]]-regions[sr][sc]
                    if diff <= 0:
                        Q.append((sr+dr[d], sc+dc[d], expenditure+1))
                    else:
                        Q.append((sr+dr[d], sc+dc[d], expenditure+1+diff))
    print('#{} {}'.format(tc, minE))