# 1486

# for tc in range(int(input())):
#     n, b = map(int, input().split())
#     h = list(map(int, input().split()))
#     diff = 10000
#     for i in range(1<<n):
#         sum = 0
#         for j in range(n):
#             if i&(1<<j):
#                 sum += h[j]
#         if b <= sum and sum-b < diff:
#             diff = sum-b
#     print('#{} {}'.format(tc+1, diff))

# 1258

# for tc in range(int(input())):
#     rl = list()
#     n = int(input())
#     cont = [list(map(int, input().split())) for _ in range(n)]
#     for i in range(n):
#         r = 0
#         for j in range(n):
#             if cont[j][i] != 0:
#                 r += 1
#                 if (j+1 <n and cont[j+1][i] == 0) or j+1 == n:
#                     rl.append(r)
#                     r = 0
#             elif cont[j][i] == 0:
#                 continue
#     cnt = [0] * (max(rl)+1)
#     for r in rl:
#         for c in range(max(rl)+1):
#             if r == c:
#                 cnt[c] += 1
#     rl = list(set(rl))
#     ans = list()
#     for r in rl:
#         if cnt[r] != 0:
#             ans.append([r, cnt[r]])
#     ans.sort(key = lambda x: x[0] * x[1])
#     print('#{} {} '.format(tc+1, len(ans)), end = '')
#     for i in range(len(ans)):
#         print('{} {}'.format(ans[i][0], ans[i][1]), end= ' ')
