# 2636

# def find(t, c):
#     global cheese
#     dr= [-1, 0, 1, 0]
#     dc= [0, 1, 0, -1]
#     check = [[0]*w for _ in range(h)]
#     if c == 0:
#         return t
#     else:
#         cnt = 0
#         melt = 0
#         for i in range(1, h):
#             for j in range(1, w):
#                 if cheeses[i][j] == 1:
#                     cnt += 1
#                     for k in range(4):
#                         if i+dr[k] < 0 or i+dr[k] >= h or j+dc[k] < 0 or j+dc[k] >= w: continue
#                         else:
#                             if cheeses[i+dr[k]][j+dc[k]] == 0 and check[j+dc[k]] != 1:
#                                 check[j+dc[k]] = 1
#                                 cheeses[i][j] = 0
#                                 melt += 1
#                                 break
#         cheese = cnt - melt
#         find(t+1, melt)

# h, w = map(int, input().split())
# cheeses = [list(map(int, input().split())) for _ in range(h)]
# cheese = 0
# print(find(0, 10000))
# print(cheese)

# 14502

# n, m = map(int, input().split()) # n이 세로 m이 가로
# maps = [list(map(int, input().split())) for _ in range(n)]


# 15688

# 17135

# a, b, c = map(int, input().split())
# a+(b*) > c*

n = int(input())
people = []
for _ in range(n):
    x, y = map(int, input().split())
    people += [[x, y]]
ans = sorted(people, key= lambda x: (x[0], x[1]), reverse=True)
dungchi = [0] * n
dungchi[people.index(ans[0])] = 1
t = 1
c = 0
i = 1
while i < n:
    if ans[i-1][0] > ans[i][0] and ans[i-1][1] > ans[i][1]:
        t += 1
        dungchi[people.index(ans[i])] = t+c
        t = t+c
        c = 0
        i += 1
    elif ans[i-1][1] < ans[i][1]:
        dungchi[people.index(ans[i])] = t
        c += 1
        i += 1
    elif ans[i-1][0] == ans[i][0]:
        dungchi[people.index(ans[i])] = t
        c += 1
        i += 1
print(*dungchi)

