# 1204
# from collections import Counter

#
# t = int(input())
# for _ in range(1, t+1):
#     c = int(input())
#     scores = list(map(int, input().split()))
#     for i in range(len(scores)):
#         if 0 <= scores[i] <= 100 and len(scores) == 100:
#             continue
#     f_score = Counter(scores).most_common(1)[0][0]
#     print(f'#{c} {f_score}')

# 1284
# t = int(input())
#
# for i in range(1, t+1):
#     water_choices = list(map(int, input().split()))
#     for j in range(len(water_choices)):
#         if 1 <= water_choices[j] <= 10000:
#             continue
#     A_charge = water_choices[0] * water_choices[4]
#     if water_choices[4] <= water_choices[2]:
#         B_charge = water_choices[1]
#     else:
#         B_charge = water_choices[1] + ( water_choices[4] - water_choices[2] ) * water_choices[3]
#     if A_charge > B_charge:
#         print(f'#{i} {B_charge}')
#     else:
#         print(f'#{i} {A_charge}')

# 1285 는 파이썬으로 논노

# 1288
# T = int(input())
# for i in range(1, T+1):
#     N = input()
#     k = 1
#     result = []
#     while True:
#         l = str(k * int(N))
#         for m in range(len(l)):
#             if int(l[m]) not in result:
#                 result.append(int(l[m]))
#                 result.sort()
#         if result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
#             res = k * int(N)
#             break
#         k += 1
#     print(f'#{i} {res}')

# 1859

for tc in range(int(input())):
    n = int(input())
    v = list(map(int, input().split()))



# 1926
# N = int(input())
# lst_N = []
# clap_N = [0] * N
# check_369 = ['3', '6', '9']
# result = [0] * N
# if 10 <= N <= 1000:
#     for i in range(1, N+1):
#         lst_N.append(i)
#     for i in range(len(lst_N)):
#         cnt = 0
#         for j in range(len(str(lst_N[i]))):
#             if str(lst_N[i])[j] in check_369:
#                 cnt += 1
#                 clap_N[i] = cnt
#     for i in range(N):
#         if clap_N[i] != 0:
#             result[i] = '-' * clap_N[i]
#         else:
#             result[i] = lst_N[i]
# for i in range(len(result)):
#     print(result[i], end=' ')

# 1940
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     acc_lst=[]
#     v_lst = []
#     for i in range(N):
#         acc_lst.append(list(map(int, input().split())))
#         v = 0
#     for i in range(len(acc_lst)):
#         if acc_lst[i][0] == 1:
#             v = acc_lst[i][1]
#             v_lst.append(v)
#         elif acc_lst[i][0] == 2:
#             v = -(acc_lst[i][1])
#             v_lst.append(v)
#         else:
#             v = 0
#             v_lst.append(v)
#     for i in range(1, len(v_lst)):
#         if v_lst[i-1] < 0 and v_lst[i-1] + v_lst[i] < 0:
#             v_lst[i-1] = 0
#         elif v_lst[i] < 0 and v_lst[i-1] + v_lst[i] > 0:
#             v_lst[i] += v_lst[i-1]
#         elif v_lst[i] == 0 and v_lst[i-1] > 0:
#             v_lst[i] += v_lst[i-1]
#         elif v_lst[i-1] > 0 and v_lst[i] > 0:
#             v_lst[i] += v_lst[i-1]
#         elif v_lst[i-1] > 0 and v_lst[i] < 0:
#             v_lst[i] += v_lst[i-1]
#     s = 0
#     for i in range(len(v_lst)):
#         s += v_lst[i]
#     print(f'#{tc} {s}')

# 1945
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     a = 0
#     b = 0
#     c = 0
#     d = 0
#     e = 0
#     factors = [2, 3, 5, 7, 11]
#     if 2 <= N <= 10000000:
#         while N != 1:
#             if N % 2 == 0:
#                 N /= 2
#                 a += 1
#             if N % 3 == 0:
#                 N /= 3
#                 b += 1
#             if N % 5 == 0:
#                 N /= 5
#                 c += 1
#             if N % 7 == 0:
#                 N /= 7
#                 d += 1
#             if N % 11 == 0:
#                 N /= 11
#                 e += 1
#     print(f'#{tc} {a} {b} {c} {d} {e}')

# 1946
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     t_l = []
#     result = []
#     ouput = 0
#     ans = ''
#     cnt = 0
#     ans_10 = []
#     for i in range(N):
#         data_input = list(input().split())
#         t_l.append(data_input)
#     for i in range(len(t_l)):
#         output = t_l[i][0] * int(t_l[i][1])
#         result.append(output)
#     print(result)
#     for i in range(len(result)):
#         ans += result[i]

#     print(f'#{tc}')
#     for i in range((len(ans)%10)+1):
#         ans_10.append(ans[10*i:10*i+10])
#         print(ans_10[i])

# 1948

# T = int(input())
# day_end = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
# mon = [0] * 12
# result = 0
# for i in range(1, len(mon)):
#     mon[0] = 1
#     mon[i] = mon[i-1] + day_end[i-1]
# for tc in range(1, T+1):
#     m1, d1, m2, d2 = list(map(int, input().split()))
#     s_i = mon[m1-1]+ d1-1
#     e_i = mon[m2-1]+ d2-1
#     result = e_i - s_i +1
#     print(f'#{tc} {result}')

# 1954

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     result = [[0 for _ in range(N)] for _ in range(N)]
#     dr = [-1, 0, 1, 0]
#     dc = [0, 1, 0, -1]
    
# coaching
# for i in range(N):
#     if i % 2 == 0:
#         for j in range(M):
#             print(arr[i][j], end = ' ')
#     else:
#         for j in range(M-1, -1, -1):
#             print(arr[i][j], end = ' ')

#     matrix = [[0 for _ in range(N)] for _ in range(N)]
#     matrix[0][0] = 1
#     num = 1
#     currentr = 0
#     currentc = 0
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
#     while num < N**2:
#         for i in range(4):
#             nc = currentc + dc[i]
#             nr = currentr + dr[i]
#             while 0 <= nr and nr < N and 0 <= nc and nc < N:
#                 if matrix[nr][nc] == 0:
#                     num += 1
#                     matrix[nr][nc] = num
#                     currentc = nc
#                     currentr = nr
#                     nc = currentc + dc[i]
#                     nr = currentr + dr[i]
#                 else:
#                     break
#
#     print('#{}'.format(tc))
#     for i in range(N):
#         print('{}'.format(' '.join(map(str, matrix[i]))))


# 1959

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     maxV = 0
#     if len(A) < len(B):
#         for i in range(abs(N-M)+1):
#             multiple = 0
#             for j in range(len(A)):
#                 multiple += A[j] * B[j+i]
#             if multiple > maxV:
#                 maxV = multiple
#     else:
#         for i in range(abs(N-M)+1):
#             multiple = 0
#             for j in range(len(B)):
#                 multiple += A[j+i] * B[j]
#             if multiple > maxV:
#                 maxV = multiple
#     print('#{} {}'.format(tc, maxV))

# 1961

# def rot90(list):
#     n = len(list)
#     rot_lst = [['0' for _ in range(n)] for _ in range(n)]
#     for x in range(n):
#         for y in range(n-1, -1, -1):
#             rot_lst[x][y] = list[y][x]
#     for x in range(n):
#         for y in range(1, int(n/2)+1):
#             rot_lst[x][y-1], rot_lst[x][-y] = rot_lst[x][-y], rot_lst[x][y-1]
#     return rot_lst


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     matrix = []
#     for i in range(N):
#         matrix.append(list(map(str, input().split())))
#     result1 = ''
#     result2 = ''
#     result3 = ''
#     for i in range(N):
#         for j in range(N):
#             result1 += rot90(matrix)[i][j]
#     for i in range(N):
#         for j in range(N):
#             result2 += rot90(rot90(matrix))[i][j]
#     for i in range(N):
#         for j in range(N):
#             result3 += rot90(rot90(rot90(matrix)))[i][j]
#     print(f'#{tc}')
#     for i in range(1, N+1):
#         print(result1[N*(i-1):N*i], result2[N*(i-1):N*i], result3[N*(i-1):N*i])

# 1970

# changes = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     counting = []
#     result = []
#     remain = N
#     for change in changes:
#         k = 0
#         while remain > 0:
#             k += 1
#             remain -= change * k
#         if k == 1:
#             counting.append(k-1)
#         else:
#             counting.append(k)
#         remain += change * k
#     print(counting)
# T = int(input())

# for tc in range(1, T + 1):

# for tc in range(1, T+1):

#     N = int(input())
#     counting = []
#     a = 0
#     b = 0
#     remain = N
#     for change in changes:
#         a = remain // change
#         counting.append(a)

#         if a == 0:
#             remain = remain
#         else:
#             remain -= change * a
#     print('#{} '.format(tc), end='')
#     for i in range(len(chages)):
#         print('{}'.format(changes[i]), end=' ')

#         if a == 0 :
#             remain = remain
#         else:
#             remain -= change * a
#     print('#{} '.format(tc), end= '')
#     for i in range(len(chages)):
#         print('{}'.format(changes[i]), end = ' ')

#     print()

# 1974

# def sdoku(list):
#     check = [i for i in range(1, 10)]
#     counting_w = [[0 for _ in range(9)] for _ in range(9)]
#     counting_h = [[0 for _ in range(9)] for _ in range(9)]
#     for i in range(9):
#         for j in range(9):
#             for k in range(9):
#                 if list[i][j] == check[k]:
#                     if counting_w[i][k] == 0:
#                         counting_w[i][k] += 1
#                     else:
#                         return 0
#     for i in range(9):
#         for j in range(9):
#             for k in range(9):
#                 if list[j][i] == check[k]:
#                     if counting_h[i][k] == 0:
#                         counting_h[i][k] += 1
#                     else:
#                         return 0
#
#     for i in range(3):
#         for j in range(3):
#             counting_c = [0 for _ in range(9)]
#             for k in range(3):
#                 for l in range(3):
#                     for m in range(9):
#                         if list[3*i+k][3*j+l] == check[m]:
#                             if counting_c[m] == 0:
#                                 counting_c[m] += 1
#                             else:
#                                 return 0
#     return 1
#
# T = int(input())
# for tc in range(1, T+1):
#     puzzle = []
#     for i in range(9):
#         puzzle.append(list(map(int, input().split())))
#     sdoku(puzzle)
#     print('#{} {}'.format(tc, sdoku(puzzle)))

# 1979

# T= int(input())
# for tc in range(1, T+1):
#     n, m = map(int, input().split())
#     matrix = []
#     for i in range(n):
#         matrix.append(list(map(int, input().split())))
#     dr = []
#     dc = []
#     for i in range(m):
#         dr.append(i+1)
#         dc.append(i+1)
#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             if matrix[i][j] == 1:
#                 cnt1 = 1
#                 if j == 0:
#                     for k in range(len(dc)):
#                         nc = j + dc[k]
#                         if 0 <= nc < n:
#                             if matrix[i][nc] == 1:
#                                 cnt1 += 1
#                             else:
#                                 break
#                         else:
#                             break
#                     if cnt1 == m:
#                         cnt += 1
#                 else:
#                     if matrix[i][j-1] != 1:
#                         for k in range(len(dc)):
#                             nc = j + dc[k]
#                             if 0 <= nc < n:
#                                 if matrix[i][nc] == 1:
#                                     cnt1 += 1
#                                 else:
#                                     break
#                             else:
#                                 break
#                         if cnt1 == m:
#                             cnt += 1
#
#     for i in range(n):
#         for j in range(n):
#             if matrix[j][i] == 1:
#                 cnt2 = 1
#                 if j == 0:
#                     for k in range(len(dr)):
#                         nr = j + dr[k]
#                         if 0 <= nr < n:
#                             if matrix[nr][i] == 1:
#                                 cnt2 += 1
#                             else:
#                                 break
#                         else:
#                             break
#                     if cnt2 == m:
#                         cnt += 1
#                 else:
#                     if matrix[j-1][i] != 1:
#                         for k in range(len(dr)):
#                             nr = j + dr[k]
#                             if 0 <= nr < n:
#                                 if matrix[nr][i] == 1:
#                                     cnt2 += 1
#                                 else:
#                                     break
#                             else:
#                                 break
#                         if cnt2 == m:
#                             cnt += 1
#     print('#{} {}'.format(tc, cnt))


# T= int(input())
# for tc in range(1, T+1):
#     n, m = map(int, input().split())
#     matrix = [list(map(int, input().split())) for _ in range(n)]
#     dr = [-1]
#     dc = [-1]
#     ans = [0, 0]
#     cnt = 0
#     for i in range(m-1):
#         ans.insert(1, 1)
#     for i in range(m):
#         dr.append(i+1)
#         dc.append(i+1)
#     for i in range(n):
#         for j in range(n):
#             temp = []
#             for k in range(len(dc)):
#                 if matrix[i][j] == 1:
#                     nj = j + dc[k]
#                     if 0 <= nj and nj < n:
#                         temp.append(matrix[i][nj])
#                     elif nj == n or nj < 0:
#                         temp.append(0)
#                 else:
#                     break
#             if temp == ans:
#                 cnt += 1
#     for i in range(n):
#         for j in range(n):
#             temp = []
#             for k in range(len(dr)):
#                 if matrix[j][i] == 1:
#                     nj = j + dr[k]
#                     if 0 <= nj and nj < n:
#                         temp.append(matrix[nj][i])
#                     elif nj == n or nj < 0:
#                         temp.append(0)
#                 else:
#                     break
#             if temp == ans:
#                 cnt += 1
#     print('#{} {}'.format(tc, cnt))



# 1986

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     lst = list(range(1, N+1))
#     for n in range(1, len(lst)):
#         if lst[n] % 2 == 0:
#             lst[n] *= -1
#     sum = 0
#     for n in lst:
#         sum += n
#     print(f'#{tc} {sum}')

# 1989

# T = int(input())
# def is_palindrome(word):
#     for i in range(1, round(len(word)/2)):
#         if word[i-1] == word[-i]:
#             return 1
#     return 0
# for tc in range(1, T+1):
#     word = input()
#     print(f'#{tc} {is_palindrome(word)}')

# 2001

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     matrix = []
#     for i in range(N):
#         matrix.append(list(map(int, input().split())))
#     max_sum = 0
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             sum = 0
#             for k in range(M):
#                 for l in range(M):
#                     sum += matrix[i+k][j+l]
#             if sum > max_sum:
#                 max_sum = sum
#     print('#{} {}'.format(tc, max_sum))

# 2005

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     triangle = [[] for _ in range(N)]
#     for i in range(N):
#         triangle[i].append(1)
#     for i in range(1, N):
#         triangle[i].append(1)
#     for i in range(2, N):
#         for j in range(1, len(triangle[i-1])):
#             sum = triangle[i-1][j-1] + triangle[i-1][j]
#             triangle[i].insert(j, sum)
#     print('#{}'.format(tc))
#     for row in triangle:
#         print(' '.join(map(str,row)))

# 2007

# T = int(input())
# for tc in range(1, T+1):
#     word = input()
#     cnt = 1
#     stan = word[0]
#     for i in range(1, len(word)):
#         if stan == word[i]:
#             if word[0:i+1] != word[i:2*i+1]:
#                 continue
#             else:
#                 cnt = i
#                 break
#     print(f'#{tc} {cnt}')