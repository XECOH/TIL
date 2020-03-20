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

# for tc in range(1, int(input())+1):
#     n = int(input())
#     rooms = [0] * 200
#     for i in range(n):
#         cr, mr = map(int, input().split())
#         if cr % 2:
#             cr = (cr//2)
#         else:
#             cr = (cr//2)-1
#         if mr % 2:
#             mr = (mr//2)
#         else:
#             mr = (mr//2)-1
#         for c in range(min(cr, mr), max(cr, mr)+1):
#             rooms[c] += 1
#     print('#{} {}'.format(tc, max(rooms)))

'''
*coaching*

for tc in range(1, int(input())+1):
    n = int(input())
    cnt = [0] * 201
    for _ in range(n):
        a, b = map(int, input().split())
        a = (a+1)//2
        b = (b+1)//2
        if a > b: a, b = b, a
        for i in range(a, b+1):
            cnt[i] += 1
    print('#{} {}'.format(tc, max(cnt)))
'''

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

# 1223

# def icp(t): #스택에 넣을 때
#     if t =='*':
#         return 2
#     else:
#         return 1

# def isp(t): # 스택안에
#     if t == '*':
#         return 2
#     else:
#         return 1

# def operation(arr):
#     op = ['*', '+']
#     st = []
#     for c in arr:
#         if c not in op:
#             st. append(c)
#         else:
#             if c == '*':
#                 op1= st.pop()
#                 op2= st.pop()
#                 st.append(op1*op2)
#             else:
#                 op1 = st.pop()
#                 op2 = st.pop()
#                 st.append(op1+op2)
#     return st[0]

# for tc in range(1, 2):
#     l = int(input())
#     c = list(map(str, input()))
#     operator = ['*', '+']
#     postfix = []
#     st = []
#     for i in c:
#         if i not in operator:
#             postfix.append(int(i))
#         else:
#             if st == []:
#                 st.append(i)
#             else:
#                 top = st[-1]
#                 if icp(i) > isp(top):
#                     st.append(i)
#                 elif icp(i) == isp(top):
#                     postfix.append(st.pop())
#                     st.append(i)
#                 else:
#                     while st:
#                         top = st[-1]
#                         if isp(top) < icp(i):
#                             break
#                         else:
#                             postfix.append(st.pop())
#                     st.append(i)    
#     while st:
#         postfix.append(st.pop())
#     print('#{} {}'. format(tc, operation(postfix)))

# 1222

# def icp(t): #스택에 넣을 때
#     return 1

# def isp(t): # 스택안에
#     return 1

# def operation(arr):
#     op = ['+']
#     st = []
#     for c in arr:
#         if c not in op:
#             st. append(c)
#         else:
#             op1 = st.pop()
#             op2 = st.pop()
#             st.append(op1+op2)
#     return st[0]

# for tc in range(1, 11):
#     l = int(input())
#     c = list(map(str, input()))
#     operator = ['+']
#     postfix = []
#     st = []
#     for i in c:
#         if i not in operator:
#             postfix.append(int(i))
#         else:
#             if st == []:
#                 st.append(i)
#             else:
#                 top = st[-1]
#                 if icp(i) > isp(top):
#                     st.append(i)
#                 elif icp(i) == isp(top):
#                     postfix.append(st.pop())
#                     st.append(i)
#                 else:
#                     while st:
#                         top = st[-1]
#                         if isp(top) < icp(i):
#                             break
#                         else:
#                             postfix.append(st.pop())
#                     st.append(i)    
#     while st:
#         postfix.append(st.pop())
#     print('#{} {}'. format(tc, operation(postfix)))

# 1227

# def miro(i, j):
#     dr = [-1, 0, 1, 0]
#     dc = [0, 1, 0, -1]
#     st = [[i, j]]
#     while st:
#         [ci, cj] = st.pop()
#         for k in range(4):
#             nr = ci + dr[k]
#             nc = cj + dc[k]
#             if nr < 0 or nr >= 100 or nc < 0 or nc >= 100: continue
#             if maze[nr][nc] == 1: continue
#             if maze[nr][nc] == 3: return 1
#             if maze[nr][nc] == 9: continue
#             maze[nr][nc] = 9
#             st.append([nr, nc])
#     return 0

# for tc in range(1, 2):
#     n = int(input())
#     maze = [list(map(int, input())) for _ in range(100)]
#     for i in range(100):
#         sr, sc= -1, -1
#         for j in range(100):
#             if maze[i][j] == 2:
#                 sr = i
#                 sc = j
#                 break
#         if sr != -1 and sc != -1: break
#     print('#{} {}'.format(tc, miro(sr, sc)))

# 3349

# for tc in range(1, int(input())+1):
#     w, h, n = map(int, input().split())
#     moving = [list(map(int, input().split())) for _ in range(n)]
#     minE = 0
#     for i in range(n-1):
#         if moving[i][0] < moving[i+1][0] and moving[i][1] < moving[i+1][1]:
#             if abs(moving[i][0]-moving[i][1]) == abs(moving[i+1][0]-moving[i+1][1]):
#                 minE += abs(moving[i][0]-moving[i][1])
#             else:


'''
coaching

for tc in range(1, int(input())+1):
    w, h, n = map(int, input().split())
    x, y = map(int, input().split())
    ans = 0
    for _ in range(n-1):
        tx, ty = map(int, input().split())
    생    # # 수직 이동
    략    # if x == tx: ans += abs(y-ty)
    가    # # 수평 이동
    능     # elif y == ty: ans += abs(x-tx)
        a = x - tx
        b = y - ty 
        # 대각선 이동
        # 좌상우하
        if a*b < 0 : ans += (abs(a)+abs(b))
        # 좌하우상
        else:
            ans += max(abs(a), abs(b))
        x , y = tx, ty
'''
# 4672

# for tc in range(1, int(input())+1):
#     words = list(input())
#     combi = sorted(list(set([(words[i], words.count(words[i])) for i in range(len(words))])), key = lambda x: x[1], reverse = True)
#     nwords = []
#     for i in range(len(combi)):
#         if combi[i][1] % 2 and combi[i][1] >= 2:
#             for _ in range(combi[i][1]):
#                 nwords.insert(len(nwords)//2, combi[i][0])
#         elif combi[i][1] % 2 == 0:
#             t = combi[i][1]
#             while t > 0:
#                 nwords.insert(0, combi[i][0])
#                 nwords.append(combi[i][0])
#                 t -= 2
#     sum = len(words)
#     for i in range(len(nwords)-1):
#         temp = ''
#         temp += nwords[i]
#         for j in range(i+1, len(nwords)):
#             temp += nwords[j]
#             if temp == temp[::-1]: sum += 1
#     print('#{} {}'.format(tc, sum))

# 1226

# def miro(sr, sc, n):
#     global maze
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#     visited = list()
#     if maze[sr][sc] == 3: return 1
#     visited.append(sr)
#     visited.append(sc)
#     while visited:
#         sr = visited.pop(0)
#         sc = visited.pop(0)
#         if maze[sr][sc] == 9: continue
#         maze[sr][sc] = 9
#         for k in range(4):
#             nr = sr + dr[k]
#             nc = sc + dc[k]
#             if 0 > nr or nr > n or nc < 0 or nc > n: continue
#             if maze[nr][nc] == 1: continue
#             if maze[nr][nc] == 3: return 1
#             if maze[nr][nc] == 9: continue
#             if maze[nr][nc] == 0:
#                 visited.append(nr)
#                 visited.append(nc)
#     return 0
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     maze = [list(map(int, input())) for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if maze[i][j] == 2:
#                 sr = i
#                 sc = j
#     print('#{} {}'.format(tc, miro(sr, sc, n)))

# 1210

# def search(r, c):
#     dr = [0, 0, -1]
#     dc = [1, -1, 0]
#     visited = [[0 for i in range(N)] for j in range(N)]
#     num = arr[r][c]

#     while True:
#         if r == 0: return c
#         for k in range(3):
#             nr = r + dr[k]
#             nc = c + dc[k]
#             if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
#             if visited[nr][nc] == 1: continue
#             if arr[nr][nc] == 0: continue
#             r = nr
#             c = nc
#             visited[nr][nc] = 1
#             num = arr[nr][nc]
#             break

# T = 10
# for tc in range(1, T+1):
#     t = int(input())
#     N = 100
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     for i in range(N):
#         if arr[99][i] == 2:
#             sp = search(99, i)

#     print('#{} {}'.format(tc, sp))

# 1224

# def operate(input_data, output_data):
#     operator = ['*', '+']
#     for i in input_data:
#         if i not in operator:
#             output_data.append(int(i))
#         elif i in operator:
#             if len(input_data) >= 2:
#                 if i == '+':
#                     op1 = output_data.pop()
#                     op2 = output_data.pop()
#                     output_data.append(op2 + op1)
#                 elif i == '*':
#                     op1 = output_data.pop()
#                     op2 = output_data.pop()
#                     output_data.append(op2 * op1)
#     return output_data.pop()

# def is_number(x): # 숫자인지
#     if x != '*' and x != '(' and x != ')' and x != '+':
#         return True
#     else:
#         return False

# def isp(token): # 스택의 top연산자 우선순위
#     if token == '(':
#         return 0
#     elif token == '+':
#         return 1
#     elif token == '*':
#         return 2

# def icp(token): # 스택으로 들어갈 연산자 우선 순위
#     if token == '(':
#         return 3
#     elif token == '+':
#         return 1
#     elif token == '*':
#         return 2

# for tc in range(1, 11):
#     l = int(input())
#     infix = list(input())
#     postfix = list()
#     st = list()
#     ans = list()
#     for i in infix:
#         if is_number(i):
#             postfix.append(i)
#         elif is_number(i) == False and st == []:
#             st.append(i)
#         elif i == ')':
#             while st[-1] != '(':
#                 postfix.append(st.pop())
#             st.pop()
#         elif is_number(i) == False and isp(st[-1]) < icp(i):
#             st.append(i)
#         elif is_number(i) == False and isp(st[-1]) >= icp(i):
#             while st:
#                 top = st[-1]
#                 if isp(top) <= icp(i):
#                     break
#                 postfix.append(st.pop())
#             st.append(i)
#     while st:
#         postfix.append(st.pop())
#     print('#{} {}'.format(tc, operate(postfix, ans)))

# 1861

# for tc in range(int(input())):
#     n = int(input())
#     room = [list(map(int, input().split())) for _ in range(n)]
#     c = [0] * ((n**2)+1)
#     maxT = -1
#     cnt = 1
#     minN = 123456789
#     dr = [-1, 0, 1, 0]
#     dc = [0, 1, 0, -1]
#     for i in range(n):
#         for j in range(n):
#             for k in range(4):
#                 nr = i+dr[k]
#                 nc = j+dc[k]
#                 if 0 <= nr < n and 0 <= nc < n:
#                     if room[nr][nc] - room[i][j] == 1:
#                         c[room[i][j]] = 1
#                         break
#     for i in range(len(c)):
#         if c[i] == 1:
#             cnt += 1
#         elif c[i] == 0:
#             if cnt > maxT:
#                 maxT = cnt
#                 minN = (i-cnt)+1
#                 cnt = 1
#             elif cnt == maxT:
#                 if minN > (i-cnt)+1:
#                     minN = (i-cnt)+1
#                     cnt = 1
#                 else:
#                     cnt = 1
#             else:
#                 cnt = 1

#     print('#{} {} {}'.format(tc+1, minN, maxT))

# 4613

# def find(x):
#     for i in range(0, x-3+1):
#         for j in range(i+1, x-2+1):
#             w = arr[:i+1]
#             b = arr[i+1:j+1]
#             r = arr[j+1:x]
#             coloring(w, b, r)

# def coloring(i, j, k):
#     global minC
#     c = 0
#     for x in i:
#         for y in range(m):
#             if flag[x][y] != 'W': c += 1
#     for x in j:
#         for y in range(m):
#             if flag[x][y] != 'B': c += 1
#     for x in k:
#         for y in range(m):
#             if flag[x][y] != 'R': c += 1
#     if minC > c: minC = c
#     return

# for tc in range(1, int(input())+1):
#     n, m = map(int, input().split())
#     flag = [list(input()) for _ in range(n)]
#     arr = [i for i in range(n)]
#     minC = 100000000000000
#     find(n)
#     print('#{} {}'.format(tc, minC))

# 6109

# for tc in range(1, int(input())+1):
#     n, d = map(input().split())
#     grid = [list(map(int, input().split())) for _ in range(int(n))]

# 3143

# for tc in range(1, int(input())+1):
#     a, b = input().split()
#     print('#{} {}'.format(tc, a.count(b)+(len(a)-len(b)*a.count(b))))

# 4259

# for tc in range(1, int(input())+1):
#     n = int(input())
#     nums= list(input().split())
#     result = 0
#     for num in nums:
#         result += (int(num[0:len(num)-1])**int(num[-1]))
#     print('#{} {}'.format(tc, result))

# 6109

# def rotate():
#     global grid
#     newarr = [[0 for _ in range(int(n))] for _ in range(int(n))]
#     for i in range(int(n)):
#         for j in range(int(n)):
#             newarr[j][int(n)-i-1] = grid[i][j]
#     grid = newarr

# for tc in range(1, int(input())+1):
#     n, d = input().split()
#     grid = [list(map(int, input().split())) for _ in range(int(n))]
#     result = []
#     if d == 'left':
#         rotate()
#         rotate()
#     elif d == 'up':
#         rotate()
#     elif d == 'down':
#         rotate()
#         rotate()
#         rotate()
#     for i in range(int(n)):
#         st = [j for j in grid[i] if j != 0]
#         for k in range(len(st)-1, 0, -1):
#             if st[k] == st[k-1]:
#                 st[k] *= 2
#                 st[k-1] = 0
#             else: continue
#         temp = [j for j in st if j != 0]
#         t = len(temp)
#         while t != int(n):
#             temp.insert(0, 0)
#             t += 1
#         result.append(temp)
#     grid = [result[i] for i in range(int(n))]

#     if d == 'left':
#         rotate()
#         rotate()
#     elif d == 'up':
#         rotate()
#         rotate()
#         rotate()
#     elif d == 'down':
#         rotate()

#     print('#{}'.format(tc))
#     for k in range(int(n)):
#         print(' '.join(map(str, grid[k])))

# 1868

# for tc in range(1, int(input())+1):
#     n = int(input())
#     table = [list(input()) for _ in range(n)]
#     dr = [-1, -1, -1, 0, 1, 1, 1, 0]
#     dc = [-1, 0, 1, 1, 1, 0, -1, -1]
#     minC = 0
#     check = []
#     for i in range(n):
#         for j in range(n):
#             popping = 0
#             for k in range(8):
#                 if i+dr[k] < 0 or i+dr[k] >= n or j+dc[k] < 0 or j+dc[k] >= n: continue
#                 if table[i+dr[k]][j+dc[k]] == '*':
#                     popping = -1
#                     break
#             st = []
#             if popping == 0:
#                 table[i][j] = 0
#                 minC += 1
#                 st.append([i, j])
#                 check.append([i, j])
#             while st:
#                 [r, c] = st.pop(0)
#                 for l in range(8):
#                     mine = 0
#                     cr = r+dr[l]
#                     cc = c+dc[l]
#                     if cr < 0 or cr >= n or cc < 0 or cc >= n: continue
#                     for m in range(8):
#                         nr = cr+dr[m]
#                         nc = cc+dc[m]
#                         if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
#                         if table[nr][nc] == '*': mine += 1
#                         else: continue
#                     if mine == 0 and [cr, cc] not in check: st.append([cr, cc])
#                     else: table[cr][cc] = mine
    
#     for i in range(n):
#         for j in range(n):
#             if table[i][j] == '.': minC += 1
#             else: continue
#     print('#{} {}'.format(tc, minC))
                    
# 4261

# keypad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
# for tc in range(1, int(input())+1):
#     s, n = map(str, input().split())
#     words = list(input().split())
#     cnt = 0
#     for i in range(int(n)):
#         if len(words[i]) == len(s):
#             for j in range(len(words[i])):
#                 if words[i][j] not in keypad[s[j]]: 
#                     break
#             else: cnt += 1
#     print(f'#{tc} {cnt}')

# 3501

# for tc in range(1, int(input())+1):
#     p, q = map(int, input().split())
#     if q == 1:
#         print('#{} {}'.format(tc, p))
#     elif q % 2 == 0 or q % 5 == 0 or (q % 2) % 5 == 0:
#         print('#{} {}'.fomrat(tc, p/q))
#     else:

# 5213

# result = [0]
# for i in range(1, 1000001):
#     sum = 0
#     for j in range(1, i+1):
#         if j % 2 == 1 and i % j == 0:
#             sum += j
#     result += [sum]

# for tc in range(1, int(input())+1):
#     l, r = map(int, input().split())
#     ans = 0
#     for t in range(l, r+1):
#         ans += result[t]
#     print('#{} {}'.format(tc, ans))

# 3812

# for tc in range(1, int(input())+1):
    
# 3378

# for tc in range(1, int(input())+1):
#     p, q = map(int, input().split())
#     master = [list(map(str, input())) for _ in range(p)]
#     mine = [list(map(str, input())) for _ in range(q)]
#     indent = [0]
#     a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
#     possible = []
#     for i in range(1, p):
#         a += master[i-1].count('(')
#         b += master[i-1].count(')')
#         c += master[i-1].count('{')
#         d += master[i-1].count('}')
#         e += master[i-1].count('[')
#         f += master[i-1].count(']')
#         cnt = 0
#         for j in master[i]:
#             if j != '.': break
#             else: cnt += 1
#         possible += [[(a-b), (c-d), (e-f), cnt]]

#     for r in range(1, 21):
#         for c in range(1, 21):
#             for s in range(1, 21):
                

    # a, b, c, d, e, f = 0, 0, 0, 0, 0, 0        
    # for i in range(1, q):
    #     a += mine[i-1].count('(')
    #     b += mine[i-1].count(')')
    #     c += mine[i-1].count('{')
    #     d += mine[i-1].count('}')
    #     e += mine[i-1].count('[')
    #     f += mine[i-1].count(']')
    #     if ((a-b) != 0 and R == -1) or ((c-d) != 0 and C == -1) or ((e-f) != 0 and S == -1):
    #         indent.append(-1)
    #     else:
    #         indentation = R*(a-b) + C*(c-d) + S*(e-f)
    #         indent.append(indentation)
        
    # print('#{} {}'.format(tc, ' '.join(map(str, indent))))

# 1808

# for tc in range(1, int(input())+1):
#     buttons = list(map(int, input().split()))
#     x = int(input())
#     minP = 1000000000000
#     nums =[i for i in range(10) if buttons[i] == 1]
#     check_x = 1
#     for k in range(len(str(x))):
#         if int(str(x)[k]) in nums: continue
#         else:
#             check_x = -1
#             break
#     if check_x == 1:
#         minP = len(str(x))+1
#     else:
#         for i in range(int(x**0.5), 0, -1):
#             if x % i == 0:
#                 check_i = 1
#                 check_xi = 1
#                 for j in range(len(str(i))):
#                     if int(str(i)[j]) in nums: continue
#                     else: 
#                         check_i = -1
#                         break
#                 for j in range(len(str(x//i))):
#                     if int(str(x//i)[j]) in nums: continue
#                     else:
#                         check_xi = -1
#                         break
#                 if check_i == 1 and check_xi == 1: 
#                     P = len(str(i)) + len(str(x//i)) + 2
#                     if P < minP: minP = P
#     if minP != 1000000000000:
#         print(f'#{tc} {minP}')
#     else:
#         print(f'#{tc} {-1}')

# 4050

# for tc in range(1, int(input())+1):
#     n = int(input())
#     c = list(map(int, input().split()))
#     c.sort(reverse=True)
#     minP = 0
#     for i in range(n):
#         if i%3 == 2: continue
#         else:
#             minP += c[i]
#     print('#{} {}'.format(tc, minP))

# 5987

# for tc in range(1, int(input())+1):
#     n, m = map(int, input().split())
    
# 1211

def find(r, c):
    global minD
    global si
    dr = [1, 0, 0]
    dc = [0, 1, -1]
    cnt = 0
    cr, cc = r, c
    nr, nc = cr+dr[0], cc+dc[0]
    while nr != 100:
        if laddar[cr+dr[1]][cc+dc[1]] == 1:
            rr, rc = cr+dr[1], cc+dc[1]
            while laddar[rr][rc] != 0:
                cnt += 1
                cr, cc = rr, rc
                rr, rc = cr+dr[1], cc+dc[1]
        elif laddar[cr+dr[2]][cc+dc[2]] == 1:
            lr, lc = cr+dr[2], cc+dc[2]
            while laddar[lr][lc] != 0:
                cnt += 1
                cr, cc = lr, lc
                lr, lc = cr+dr[2], cc+dc[2]
        else:
            cnt += 1
            cr, cc = nr, nc
            nr, nc = cr+dr[0], cc+dc[0]
    if minD > cnt:
        minD = cnt
        si = c
    elif minD == cnt:
        if si > c:
            si = c
    return

for tc in range(1, 11):
    n = int(input())
    laddar = [list(map(int, input().split())) for _ in range(100)]
    minD = 100000000
    si = 0
    for i in range(100):
        if laddar[0][i] == 1:
            find(0, i)
    print('#{} {}'.format(tc, si))