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

# 1218

# for tc in range(1, 11):
#     l = int(input())
#     data = input()
#     st = []
#     result = 1
#     for i in data:
#         if i == '(' or i == '<' or i == '{' or i == '[':
#             st.append(i)
#         elif i == ')':
#             if st[-1] == '(':
#                 st.pop()
#             else:
#                 result = 0
#                 break
#         elif i == ']':
#             if st[-1] == '[':
#                 st.pop()
#             else:
#                 result = 0
#                 break
#         elif i == '>':
#             if st[-1] == '<':
#                 st.pop()
#             else:
#                 result = 0
#                 break
#         elif i == '}':
#             if st[-1] == '{':
#                 st.pop()
#             else:
#                 result = 0
#                 break
#     print('#{} {}'.format(tc, result))

# 1223

# for tc in range(1, 2):
#     l = int(input())
#     data= list(input())
#     st = []
#     op = ['+', '*']
#     ndata = []
#     for i in data:
#         if i not in op:
#             ndata.append(int(i))
#         elif i in op:
#             if st == []:
#                 st.append(i)
#             else:
#                 ndata.append(st.pop())
#                 st.append(i)
#     while st:
#         ndata.append(st.pop())
#     print(ndata)

# 5432

# for tc in range(int(input())):
    # iron = input()
    # cnt = 0
    # st = []
    # i = 0
    # while i < len(iron):
    #     if iron[i] =='(' and iron[i+1] == ')' and st != []:
    #         cnt += len(st)
    #         i += 1
    #     elif iron[i] =='(' and iron[i+1] != ')':
    #         st.append(iron[i])
    #         cnt += 1
    #     elif iron[i] == ')' and st != []:
    #         st.pop()
    #     i += 1
    # print('#{} {}'.format(tc+1, cnt))


# 7701

# for tc in range(int(input())):
#     n = int(input())
#     names = set()
#     for i in range(n):
#         names.add(input())
#     names = list(names)
#     names.sort(key = lambda x: (len(x), x))
#     print('#{}'.format(tc+1))
#     for name in names:
#         print('{}'.format(name))

# 4672

# for tc in range(int(input())):
#     word = input()

#     print('#{} {}'.format(tc+1, cnt))

# 1868

# for tc in range(int(input())):
#     n = int(input())
#     table = [list(map(str, input())) for _ in range(n)]

# 1494

# for tc in range(int(input())):
#     n = int(input())
#     td = [[0]*(2000001) for _ in range(200001)]
#     for t in range(n):
#         x, y = map(int, input().split())
#         if x < 0:
#             x = -x
#         if y < 0:
#             y = -y
#         if x >= 0:
#             x = x + 100000
#         if y >= 0:
#             y = y + 100000
#     for row in td:
#         print(row)

# 4408

for tc in range(1, int(input())+1):
    n = int(input())
    rooms = [0] * 401
    for i in range(n):
        cr, mr = map(int, input().split())
        for c in range(cr+1, mr+1):
            rooms[c] += 1
    print('#{} {}'.format(tc, max(rooms)))
    

# 3347

# for tc in range(1, int(input())+1):
#     n, m = map(int, input().split())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     cnt = [0] * n
#     for i in range(m):
#         j = 0
#         while j < n:
#             if b[i] >= a[j]:
#                 cnt[j] += 1
#                 break
#             j += 1
#     print('#{} {}'.format(tc, cnt.index(max(cnt))+1))
