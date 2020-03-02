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

def find(r, c, e):
    global maxT, minN
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    sr = r
    sc = c
    for k in range(4):
        nr = sr + dr[k]
        nc = sc + dc[k]
        cnt = 1
        while 0 <= nr < e and 0 <= nc < e:
            if nr < 0 or nr >= e or nc < 0 or nc >= e: break
            if room[nr][nc] - room[sr][sc] == 1:
                cnt += 1
                sr = nr
                sc = nc
                nr = sr + dr[k]
                nc = sc + dc[k]
                if nr < 0 or nr >= e or nc < 0 or nc >= e:
                    if cnt > maxT:
                        maxT = cnt
                        minN = room[r][c]
                    elif cnt == maxT:
                        if minN > room[r][c]:
                            minN = room[r][c]
                    break
            else:
                if cnt > maxT:
                    maxT = cnt
                    minN = room[r][c]
                elif cnt == maxT:
                    if minN > room[r][c]:
                        minN = room[r][c]
                break
    if r == (e-1):
        return
    else:
        if c == (e-1):
            find(r+1, 0, e)
        else:
            find(r, c+1, e)


for tc in range(int(input())):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    maxT = 1
    minN = 1000000
    find(0, 0, n)
    print('#{} {} {}'.format(tc+1, minN, maxT))