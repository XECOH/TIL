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

# for tc in range(1, int(input())+1):
#     n, m = map(int, input().split())
#     cheez = list(map(int, input().split()))
#     oven = [[cheez[i], i+1] for i in range(n)]
#     i = n
#     while len(oven) != 1:
#         if oven[0][0] != 0:
#             oven[0][0] //= 2
#             if oven[0][0] == 0:
#                 oven.pop(0)
#                 if i < m:
#                     oven.append([cheez[i], i+1])
#                     i += 1
#             else:
#                 pizza = oven.pop(0)
#                 oven.append(pizza)
#     print('#{} {}'.format(tc, oven[0][1]))
        
#5102

# def find(s, d):
#     global minA
#     visited = [0] * (v+1)
#     que = [[s, 0]]
#     while que:
#         [sn, q] = que.pop(0)
#         for i in range(1, v+1):
#             if sn == d:
#                 minA.append(q)
#                 break
#             if visited[i] != 1 and graph[sn][i] == 1:
#                 visited[sn] = 1
#                 q += 1
#                 que.append([i, q])
#                 q -= 1
#     return

# for tc in range(1, int(input())+1):
#     minA = []
#     v, e = map(int, input().split())
#     graph = [[0]*(v+1) for _ in range(v+1)]
#     for _ in range(e):
#         n1, n2 = map(int, input().split())
#         graph[n1][n2] = graph[n2][n1] = 1
#     s, g = map(int, input().split())
#     find(s, g)
#     if len(minA) != 0:
#         print('#{} {}'.format(tc, min(minA)))
#     else:
#         print('#{} {}'.format(tc, 0))
