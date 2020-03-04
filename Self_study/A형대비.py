# 4008 > 시간초과...
# def cal(op1, op2, operator):
#     if operator == '+':
#         return op1 + op2
#     elif operator == '-':
#         return op1 - op2
#     elif operator == '*':
#         return op1 * op2
#     elif operator == '/':
#         if op1 < 0 and abs(op1) % op2 != 0:
#             return (op1 // op2) +1
#         elif op1 < 0 and abs(op1) % op2 ==0 :
#             return op1 // op2
#         else:
#             return op1 // op2
# ans = []
# for tc in range(int(input())):
#     temp = []
#     n = int(input())
#     op = list(map(int, input().split()))
#     opr = ['+', '-', '*', '/']
#     oper = []
#     nums= list(map(int, input().split()))
#     for i in range(4):
#         for j in range(op[i]):
#             oper.append(opr[i])
#     for i in range(1<<(n-1)):
#         for j in range(1, )
#         st = []
#         st.append(nums[0])
#         for i in range(n-1):
#             c = cal(st.pop(), nums[i+1], p[i])
#             st.append(c)
#         temp.append(st.pop())
#     ans.append(max(temp) - min(temp))
#
# j = 1
# for i in ans:
#     print('#{} {}'.format(j, i))
#     j += 1

# coaching

# def f(n, k, r):
#     global minV, maxV
#     if n == k:
#         if maxV < r:
#             maxV = r
#         if minV > r:
#             minV = r
#     if op[0] > 0:
#         op[0] -= 1 # 한개 사용
#         f(n+1, k, r+num[n])
#         op[0] += 1 # 한개 되돌림
#     if op[1] > 0:
#         op[1] -= 1 # 한개 사용
#         f(n+1, k, r-num[n])
#         op[1] += 1 # 한개 되돌림
#     if op[2] > 0:
#         op[2] -= 1 # 한개 사용
#         f(n+1, k, r*num[n])
#         op[2] += 1 # 한개 되돌림
#     if op[3] > 0:
#         op[3] -= 1 # 한개 사용
#         if r < 0 and r % num[n] != 0:
#             f(n+1, k, (r//num[n])+1)
#         else:
#             f(n+1, k, r//num[n])
#         op[3] += 1 # 한개 되돌림
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     op = list(map(int, input().split()))
#     num = list(map(int, input().split()))
#     minV = 100000000
#     maxV = -100000000
#     f(1, N, num[0])
#     print('#{} {}'.format(tc, maxV-minV))

# 1952
#
# def fare(m, s):
#     global minf
#     fare(m+1, )
#
#
# for tc in range(int(input())):
#
#     mon = list(map(int, input().split()))
#     print('#{} {}'.format(tc+1, minf))
'''
재귀함수이용해서 부분집합 만들기
a = [1, 2, 3]
k = len(a)
b = [0] * k
def f(n, k):
    if n == k: # 배열을 벗어나면
        for i in range(k):
            if b[i] == 1:
                print(a[i], end=' ')
        print()
    else:
        b[n] = 0
        f(n+1, k)
        b[n] = 1
        f(n+1, k)
'''
'''
부분집합 원소의 합
def f(n, k, s):
    if n == k:
        
    else:
        f(n+1, k, s+A[n]) # 부분집합에 A[n] 포함
        f(n+1, k, s)
'''
'''
서로 다른 K개의 자연수의 집합에서 부분집합 원소의 합이 M인 경우의 수
def f(n, K, s, M):
    global cnt
    if s == M:  # 남은 원소 고려할 필요 없음(=> 자연수이므로)
        cnt += 1
        return
    elif n == K: # 남은 원소 없는 경우
        return   
    else:
        f(n+1, K, s+A[n], M)
        f(n+1, K, s, M)  
'''
# coaching > 상태트리 그려보기 !

# def f(n, s, d, m, m3):
#     global minV
#     if n > 12:
#         if minV > s:
#             minV = s
#     elif minV <= s: # 이미 최소비용과 같거나 넘어선 경우
#         return
#     else: # 이용일 수 0이면?
#         f(n+1, s+min(d*table[n], m), d, m, m3)
#         f(n+3, s+m3, d, m, m3) # 이용일 수가 0이어도 다음, 다다음달 고려해야하므로
#
# T = int(input())
# for tc in range(1, T+1):
#     d, m, m3, y = map(int, input().split())
#     table = [0] + list(map(int, input().split()))
#     minV = y
#     f(1, 0, d, m, m3)
#     print('#{} {}'.format(tc, minV))

# 1861

# def find(r, c):
#     global maxT, minN
#     dr = [-1, 0, 1, 0]
#     dc = [0, 1, 0, -1]
#     sr = r
#     sc = c
#     cnt = 1
#     for k in range(4):
#         nr = sr + dr[k]
#         nc = sc + dc[k]
#         while 0 <= nr < n and 0 <= nc < n:
#             if nr < 0 or nr >= n or nc < 0 or nc >= n: break
#             if room[nr][nc] - room[sr][sc] == 1:
#                 cnt += 1
#                 sr = nr
#                 sc = nc
#                 nr = sr + dr[k]
#                 nc = sc + dc[k]
#             else:
#                 break
#     if cnt == n**2:
#         maxT = cnt
#         minN = room[r][c]
#         return
#     if cnt > maxT:
#         maxT = cnt
#         minN = room[r][c]
#     elif cnt == maxT:
#         if minN > room[r][c]:
#             minN = room[r][c]
#     if r == (n-1) and c == (n-1):
#         return
#     else:
#         if 2 <= cnt:
#             if c+cnt < n:
#                 find(r, c+cnt)
#             else:
#                 if r != n-1:
#                     find(r+1, 0)
#                 else:
#                     return
#         else:
#             if c == n-1:
#                 find(r+1, 0)
#             else:
#                 find(r, c+1)
#
# for tc in range(int(input())):
#     n = int(input())
#     room = [list(map(int, input().split())) for _ in range(n)]
#     maxT = -1000000
#     minN = 1000000
#     find(0, 0)
#     print('#{} {} {}'.format(tc+1, minN, maxT))

# coaching

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
#             else:
#                 cnt = 1
#
#     print('#{} {} {}'.format(tc+1, minN, maxT))

# 1865

# for tc in range(int(input())):
#     n = int(input())
#     w = [list(map(int, input().split())) for _ in range(n)]
#     maxP = -100
#     f()

# coaching

'''
순열 만드는방법
def f(n, k):
    if n == k:
        print(p)
    else:
        for i in range(k):
            if used[i] == 0: # i번 원소가 사용되지 않았으면
                used[i] = 1 # 사용함으로 표시
                p[n] = A[i]
                f(n+1, k) # 다음 자리 결정하러 이동
                used[i] = 0 # 다른 자리에서 사용하도록 풀어줌

A = [1, 2, 3, 4, 5]
used = [0] * len(A)
p = 
'''

def dfs(x, s):
    global arr
    global maxV
    global used
    if s <= maxV or s == 0:  #  s < maxV : s가 곱해다가다 maxV보다 낮으면 그 윗자리 n-1로 다시 돌아가
        return               # 확률인 s는 곱해나갈수록 작아진다.
    if x == N:          # 모든 visited에 배정이 된경우
        if maxV < s:        # 지금까지 구해온 s 가 기존의 maxV보다 클경우
            maxV = s        # maxV 를 s 로 한다.
    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            dfs(x + 1, s * (arr[x][i]) * 0.01)
            used[i] = 0  # k 번째 사람이 다른일을 맡을수 있게 해준다.

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    maxV = 0
    dfs(0, 1)
    print("#{} {:.6f}".format(tc, maxV * 100))