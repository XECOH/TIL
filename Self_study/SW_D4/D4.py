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

for tc in range(int(input())):
    iron = input()
    cnt = 0
    st = []
    i = 0
    while i < len(iron):
        if iron[i] =='(' and iron[i+1] == ')' and st != []:
            cnt += len(st)
            i += 1
        elif iron[i] =='(' and iron[i+1] != ')':
            st.append(iron[i])
            cnt += 1
        elif iron[i] == ')' and st != []:
            st.pop()
        i += 1
    print('#{} {}'.format(tc+1, cnt))
