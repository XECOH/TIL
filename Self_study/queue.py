# 5097 

# for tc in range(int(input())):
#     n, m = map(int, input().split())
#     nums = list(map(int, input().split()))
#     while m > 0:
#         f = nums.pop(0)
#         nums.append(f)
#         m -= 1
#     print('#{} {}'.format(tc+1, nums[0]))

# 5105

# def miro(i, j):
#     global cnt
#     q = 0
#     dr = [-1, 0, 1, 0]
#     dc = [0, 1, 0, -1]
#     st = [[i, j, q]]
#     while st:
#         [ci, cj, q] = st.pop()
#         for k in range(4):
#             nr = ci + dr[k]
#             nc = cj + dc[k]
#             if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
#             if maze[nr][nc] == 1: continue
#             if maze[nr][nc] == 3:
#                 cnt.append(q)
#                 break
#             if maze[nr][nc] == 9: continue
#             maze[ci][cj] = 9
#             q += 1
#             st.append([nr, nc, q])
#             q -= 1
#     return

# for tc in range(1, int(input())+1):
#     n = int(input())
#     maze = [list(map(int, input())) for _ in range(n)]
#     cnt = []
#     si, sj = -1, -1
#     for i in range(n):
#         for j in range(n):
#             if maze[i][j] == 2:
#                 si, sj = i, j
#                 break
#         if si != -1 and sj != -1: break
#     miro(si, sj)
#     if len(cnt) != 0:
#         print('#{} {}'.format(tc, min(cnt)))
#     else:
#         print('#{} {}'.format(tc, 0))

# 5099

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    o = [0] * n
    c = list(map(int, input().split()))
    i = 0
    j = 0
    com = n
    while o.count([-1, -1]) != (n-1):
        if com > 0 and i < m:
            o[j] = [c[i] , i+1]
            j += 1
            i += 1
            com -= 1
        else:
            if j == n:
                j = 0
            while True:
                if o[j][0] == -1:
                    j += 1
                    if j >= n:
                        j = 0
                if o[j][0] != -1:
                    o[j][0] = o[j][0]//2
                else:
                    j += 1
                    if j >= n:
                        j = 0
                if o[j][0] != -1:
                    o[j][0] = o[j][0]//2
                if o[j][0] == 0:
                    o[j][0] = -1
                    o[j][1] = -1
                    com += 1
                    break
                else:
                    j += 1
                if j == n:
                    j = 0
    for i in range(n):
        if o[i][0] != -1:
            print('#{} {}'.format(tc, o[i][1]))
            break
        

#5102

# def find(sn, en, cnt):
#     global visited
#     if graph[sn][en] == 1:
#         return cnt
#     else:
#         for i in range(1, v + 1):
#             if visited[sn] != 1 and graph[sn][i] == 1:
#                 visited[sn] = 1
#                 find(i, en, cnt + 1)
#                 visited[sn] = 0


# for tc in range(int(input())):
#     v, e = map(int, input().split())
#     graph = [[0 for _ in range(v + 1)] for _ in range(v + 1)]
#     for i in range(e):
#         nod1, nod2 = map(int, input().split())
#         graph[nod1][nod2] = 1
#         graph[nod2][nod1] = 1
#     s, g = map(int, input().split())
#     visited = [0] * (v + 1)
#     find(s, g, 0)
#     print('#{} {}'.format(tc + 1, find(s, g, 0)))
