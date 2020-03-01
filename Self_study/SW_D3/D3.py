# 1217

# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     n, m = map(int, input().split())
#     result = n ** m
#     print('#{} {}'.format(tc, result))

# 3431

# T = int(input())
# for tc in range(1, T+1):
#     L, U, X = map(int, input().split())
#     if X < L:
#         result = L - X
#     elif L <= X <= U:
#         result = 0
#     elif X > U :
#         result = -1
#     print('#{} {}'.format(tc, result))

# 4406

# T = int(input())
# for tc in range(1, T+1):
#     vowels = 'aeiou'
#     words = input()
#     result = ''
#     for word in words:
#         if word not in vowels:
#             result += word
#     print('#{} {}'.format(tc, result))

# 8658

# T = int(input())
# for tc in range(1, T+1):
#     list = [list(map(int, input().split()))]
#     max = 0
#     min = 1
#     for i in range(10):
#         sum = 0
#         for j in range(len(str(list[i]))):
#             sum = str(list[i])[j]
#             if sum < min :
#                 min = sum
#             elif sum > max:
#                 max = sum
#     print('#{} {} {}'.format(tc, max, min))

# 5431

# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     students = [i for i in range(1, N+1)]
#     submit = list(map(int, input().split()))
#     for j in range(K):
#         students.remove(submit[j])
#     print('#{} '.format(tc), end ='')
#     for k in range(len(students)):
#         print(students[k], end= ' ')
#     print()

# 5549

# T = int(input())
# for tc in range(1, T+1):
#     num = int(input())
#     if num % 2:
#         result = 'Odd'
#     else:
#         result = 'Even'
#     print('#{} {}'.format(tc, result))

# 6692

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     calculate = []
#     avg_salary = 0
#     for i in range(N):
#         p, x = map(float, input().split())
#         avg_salary += float(p) * x
#     print('#{} {}'.format(tc, float(avg_salary)))

# 1215

# def is_palindrome(list):
#     for i in range(1, int(len(list)/2)+1):
#         if list[i-1] == list[-i]:
#             continue
#         else:
#             return False
#             break
#     return True
#
# T = 10
# for tc in range(1, T+1):
#     l = int(input())
#     board = [list(map(str, input())) for _ in range(8)]
#     cnt = 0
#     for i in range(8):
#         for j in range(8-l+1):
#             tempr = []
#             for k in range(l):
#                 tempr.append(board[i][j+k])
#             if is_palindrome(tempr):
#                 cnt += 1
#             tempc = []
#             for k in range(l):
#                 tempc.append(board[j+k][i])
#             if is_palindrome(tempc):
#                 cnt += 1
#     print('#{} {}'.format(tc, cnt))

# 1230

# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     secretcode = []
#     for i in range(N):
#         secretcode.append(input().split())
#     ordernumber = int(input())
#     order = [input().split() for _ in range(ordernumber)]
#     for i in range(ordernumber):
#         if order[i] == 'I':
#             for j in range(order[i+2]):
#                 secretcode.insert(order[i+1]+j, order[i+j])
#         elif order[i] == 'A':
#
#         elif order[i] == 'D':

# 3131
#
# prime = []
# for i in range(2, 10**6+1):
#     for j in range(1, i+1):
#         while j <= i:
#             if i % j == 0:
#                 if i != j:
#                     break
#                 else:
#                     prime.append(i)
#                     break
#             elif i % j != 0:
#                 break
# for i in range(len(prime)):
#     print(prime[i], end= ' ')

# 1213

# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     searching = input()
#     sentences = input()
#     cnt = 0
#     for i in range(len(sentences)-len(searching)+1):
#         if sentences[i:i+len(searching)] == searching:
#             cnt += 1
#     print('#{} {}'.format(tc, cnt))

# 3314

# T = int(input())
# for tc in range(1, T+1):
#     scores = list(map(int, input().split()))
#     for i in range(5):
#         if scores[i] < 40:
#             scores[i] = 40
#     sum = 0
#     for score in scores:
#         sum += score
#     print('#{} {}'.format(tc, int(sum/5)))

# 2805

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     farm = [list(map(int, input())) for _ in range(N)]
#     profit = 0
#     for i in range(N):
#         for j in range(N):
#             if i == 0 or i == N-1:
#                 profit += farm[i][int(N/2)]
#             elif i == int(N/2):
#                 profit += farm[i][j]

# 3456

# T = int(input())
# for tc in range(1, T+1):
#     a, b, c = map(int, input().split())
#     d = 0
#     if a == b and b == c:
#         d = a
#     else:
#         if a == b:
#             d = c
#         elif a == c:
#             d = b
#         elif b == c:
#             d = a
#     print('#{} {}'.format(tc, d))

# 4466

# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     scores = list(map(int, input().split()))
#     scores.sort(reverse=True)
#     sum = 0
#     for i in range(K):
#         sum += scores[i]
#     print('#{} {}'.format(tc, sum))

# 3142

# T = int(input())
# for tc in range(1, T+1):
#     n, m = map(int, input().split())
#     for x in range(m+1):
#         for y in range(m+1):
#             if 2*x + y == n and x + y == m:
#                 twinhorn = x
#                 unicorn = y
#     print('#{} {} {}'.format(tc, unicorn, twinhorn))

# 5162

# T = int(input())
# for tc in range(1, T+1):
#     A, B, C = map(int, input().split())
#     total = 0
#     if A <= B:
#         total += C // A
#         if (C % A) >= B:
#             total += (C % A) // B
#     else:
#         total += C // B
#         if (C % B) >= A:
#             total += (C % B) // A
#     print('#{} {}'.format(tc, total))

# 5515

# T = int(input())
# day_end = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
# mon = [0] * 12
# day = [4, 5, 6, 0, 1, 2, 3] * 52
# day.append(4)
# day.append(5)
# for i in range(1, len(mon)):
#     mon[0] = 1
#     mon[i] = mon[i-1] + day_end[i-1]
# for tc in range(1, T+1):
#     m, d = map(int, input().split())
#     date = mon[m-1]+ d-1
#     print('#{} {}'.format(tc, day[date-1]))

# 1221

# T = int(input())
# for tc in range(1, T+1):
#     TC, l = map(str, input().split())
#     strings = list(map(str, input().split()))
#     num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     alien = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
#     for i in range(int(l)):
#         for j in range(len(alien)):
#             if strings[i] == alien[j]:
#                 strings[i] = num[j]
#     strings.sort()
#     print('#{}'.format(tc))
#     for i in range(int(l)):
#         for j in range(len(alien)):
#             if strings[i] == num[j]:
#                 strings[i] = alien[j]
#     for i in range(int(l)):
#         print('{}'.format(strings[i]), end= ' ')

# 4299

# T = int(input())
# for tc in range(1, T+1):
#     D, H, M = map(int, input().split())
#     if D == 11 and H <= 11 and M < 11:
#         result = -1
#     elif D == 11 and H < 11:
#         result = -1
#     elif H >= 11 and M >= 11:
#         result = (D - 11) * 1440 + (H - 11) * 60 + M - 11
#     elif D > 11 and H < 11 and M >= 11:
#         result = (D - 12) * 1440 + (24 - 11 + H) * 60 + M - 11
#     elif H >= 11 and M < 11:
#         result = (D - 11) * 1440 + (H - 12) * 60 + 60 - (11 - M)
#     elif H < 11 and M < 11:
#         result = (D - 12) * 1440 + (24 - 12 + H) * 60 + 60 - (11 - M)
#     print('#{} {}'.format(tc, result))

# 1225

# T = 10
# for tc in range(1, 10):
#     N = int(input())

# 1234

# T = 1
# for tc in range(1, T+1):
#     l, nums = map(int, input().split())
#     while True:
#         s_nums = str(nums)
#         for i in range(len(s_nums)-1):
#             if s_nums[i] == s_num[i+1]:
#                 s_nums.remove(s_nums[i])
#                 s_nums.remove(s_nums[i])
#         for i in range():
#             if s_nums[]

# 1860

# T = int(input())
# for tc in range(1, T+1):
#     n, m, k = map(int, input().split())
#     customer = list(map(int, input().split()))
#     customer.sort()
#     if m > customer[0]:
#         result = 'Impossible'

# 3408

# for tc in range(int(input())):
#     n = int(input())
#     s1 = (n*(n+1))// 2
#     s2 = n**2
#     s3 = n**2 + n
#     print('#{} {} {} {}'.format(tc+1, s1, s2, s3))

# 3499

# T = int(input())
# for tc in range(1, T+1):
#     l = int(input())
#     card= list(input().split())

# 3750

# ans = list()
# for tc in range(int(input())):
#     nums = input()
#     f = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     if int(nums) < 10:
#         ans.append(int(nums))
#     else:
#         sum = 0
#         for i in range(len(nums)):
#             sum += int(nums[i])
#         if sum >= 10:
#             result = f[(sum%9)-1]
#             ans.append(result)
#         else:
#             result = sum
#             ans.append(result)
#
# j = 1
# for i in ans:
#     print('#{} {}'.format(j, i))
#     j += 1


# 4676

# T = int(input())
# for tc in range(1, T+1):
#     words = list(input())
#     h = int(input())
#     hi = list(map(int, input().split()))
#     counting = [0] * (len(words)+1)
#     for i in hi:
#         for j in range(len(words)+1):
#             if i == j:
#                 counting[j] += 1
#     expand = 0
#     for i in range(len(words)+1):
#         if counting[i] != 0:
#             words.insert(i + expand, '-' * counting[i])
#             expand += 1
#         else:
#             continue
#     print('#{} {}'.format(tc, ''.join(words)))

# 5215

# for tc in range(int(input())):
#     n, l = map(int, input().split())
#     ing = [list(map(int, input().split())) for _ in range(n)]
#     maxT = 0
#     for i in range(1<<n):
#         cal = 0
#         T = 0
#         for j in range(n):
#             if i&(1<<j):
#                 cal += ing[j][1]
#                 T += ing[j][0]
#             if maxT < T and cal <= l:
#                 maxT = T
#     print('#{} {}'.format(tc+1, maxT))

# 5601

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     print('#{} '.format(tc), end= '')
#     for i in range(N):
#         print('{}'.format('1'+'/'+str(N)), end = ' ')
#     print()

# 5607

# for tc in range(int(input())):
#     n, r = map(int, input().split())
#     result1 = 1
#     result2 = 1
#     for i in range(1, n+1):
#         result1 *= i
#     for j in range(1, r+1):
#         result2 *= ((i * (n-i)) ** (1234567891-2))
#
#     print('#{} {}'.format(tc+1, ))

# 5688

# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     i = 1
#     result = -1
#     while i <= 10**6:
#         if i ** 3 != n:
#             i += 1
#             continue
#         else:
#             result = i
#             break
#     print('#{} {}'.format(tc, result))

# 5948

# T = int(input())
# for tc in range(1, T+1):
#     nums = list(map(int, input().split()))
#     sum = 0
#     sums = []
#     for i in range(5):
#         sum += nums[i]
#         for j in range(6):
#             if j > i:
#                 sum += nums[j]
#                 for k in range(2, 7):
#                     if k > j:
#                         sum += nums[k]
#                         if sum not in sums:
#                             sums.append(sum)
#                         sum -= nums[k]
#                 sum -= nums[j]
#         sum = 0
#     sums.sort(reverse=True)
#     print('#{} {}'.format(tc, sums[4]))

# 1228

# T = 10
# for tc in range(1, T+1):
#     f1 = int(input())
#     s = list(map(int, input().split()))
#     t = int(input())
#     f4 = list(map(str, input().split()))
#     for i in range(len(f4)):
#         if f4[i] == 'I':
#             for j in range(int(f4[i+2])):
#                 s.insert(int(f4[i+1])+j, int(f4[i+3+j]))
#         else:
#             continue
#     print('#{} '.format(tc), end= '')
#     for i in range(10):
#         print('{}'.format(s[i]), end= ' ')

# 1225

# T = 10
# for tc in range(1, T+1):
#     n = int(input())
#     codes = list(map(int, input().split()))
#     a = 1
#     while a !=0:
#         for i in range(1, 6):
#             a = codes[0] - i
#             if a <= 0:
#                 a = 0
#                 codes[0] = a
#             else:
#                 codes[0] = a
#                 codes.append(a)
#                 codes.remove(a)
#     codes.remove(0)
#     codes.append(0)
#     print('#{} '.format(tc), end= '')
#     for i in range(8):
#         print('{}'.format(codes[i]), end=' ')
#     print()

# 1229

# T = 1
# for tc in range(1, T+1):
#     f1 = int(input())
#     s = list(map(int, input().split()))
#     t = int(input())
#     f4 = list(map(str, input().split()))
#     for i in range(len(f4)):
#         if f4[i] == 'I':
#             for j in range(int(f4[i+2])):
#                 s.insert(int(f4[i+1])+j, int(f4[i+3+j]))
#         elif f4[i] == 'D':
#             for j in range(int(f4[i+2])):
#                 s.pop(int(f4[i+1]))
#         else:
#             continue
#     print('#{} '.format(tc), end= '')
#     for i in range(10):
#         print('{}'.format(s[i]), end= ' ')
#     print()

# 5789

# for tc in range(int(input())):
#     n, q = map(int, input().split())
#     box = [0] * (n+1)
#     order = [list(map(int, input().split())) for _ in range(q)]
#     for i in range(q):
#         for j in range(order[i][0], order[i][1]+1):
#             box[j] = i+1
#     box.pop(0)
#     print('#{} {}'.format(tc+1, ' '.join(map(str, box))))

# 1289

# for tc in range(int(input())):
#     original = list(map(int, input()))
#     present = [0] * len(original)
#     cnt = 0
#     while original != present:
#         for i in range(len(original)):
#             if original[i] != present[i]:
#                 for j in range(i, len(original)):
#                     present[j] = 1 - present[j]
#                 cnt += 1

#     print('#{} {}'.format(tc+1, cnt))

# 5603

# for tc in range(int(input())):
#     n = int(input())
#     hay = list(int(input()) for _ in range(n))
#     sum = 0
#     for i in range(n):
#         sum += hay[i]
#     avg = sum // n
#     cnt = 0
#     for i in hay:
#         if i > avg:
#             cnt += (i-avg)
#     print('#{} {}'.format(tc+1, cnt))

# 3975

# ans = list()
# for tc in range(int(input())):
#     a, b, c, d = map(int, input().split())
#     alice = a / b
#     bob = c / d
#     if alice > bob:
#         result= 'ALICE'
#     elif alice < bob:
#         result = 'BOB'
#     elif alice == bob:
#         result = 'DRAW'
#     ans.append(result)
#
# j = 1
# for i in ans:
#     print('#{} {}'.format(j, i))
#     j = j+1

# 6019

# for tc in range(int(input())):
#     d, a, b, f = map(int, input().split())
#     h = d / (a + b)
#     result = h * f
#     print('#{} {}'.format(tc+1, result))

# 3376
#
# for tc in range(int(input())):
#     n = int(input())
#     padoban = [1, 1, 1, 2, 2]
#     for i in range(5, n):
#         padoban.append(padoban[i-3] + padoban[i-2])
#     print('#{} {}'.format(tc+1, padoban[n-1]))

# 1244

#for tc in range(int(input())):
#    nums, t = map(int, input().split())
#    nums = list(map(int, str(nums)))
#    for i in range(t):



    # print('#{} {}'.format(tc+1, ''.join(map(str, nums))))

# 3809

# for tc in range(int(input())):
#     n = int(input())
#     nums = list(map(int, input().split()) for _ in range(n//20))


# 2817

# for tc in range(int(input())):
#     n, k = map(int, input().split())
#     nums = list(map(int, input().split()))
#     cnt = 0
#     for i in range(1<<n):
#         sum = 0
#         for j in range(n):
#             if i&(1<<j):
#                 sum += nums[j]
#             if sum == k:
#                 cnt += 1
#     print('#{} {}'.format(tc+1, cnt))

# 4522

# for tc in range(int(input())):
#     given = input()
#     result = 'Exist'
#     for i in range(1, (len(given)//2)+1):
#         if given[i-1] == '?' or given[-i] == '?':
#             continue
#         elif given[i-1] != '?' or given[-i] != '?' and given[i-1] != given[-i]:
#             result = 'Not exist'
#             break
#     print('#{} {}'.format(tc+1, result))

# 3304
#
# for tc in range(int(input())):
#     s1, s2 = input().split()
#

# 3233

# for tc in range(int(input())):
#     a, b = map(int, input().split())
#     if b > a//2:
#         result = 1
#     else:
#         result = (a // b) ** 2
#     print('#{} {}'.format(tc+1, result))

# 4371

# for tc in range(int(input())):
#     n = int(input())
#     port = list(int(input()) for _ in range(n))
#     d = [port[1]-port[0]]
#     for i in range(2, n):
#         j = len(d)
#         k = 0
#         while k < j:
#             if (port[i]-port[0]) % d[k] == 0:
#                 break
#             else:
#                 k += 1
#         if k == j:
#             d.append(port[i]-port[0])
#     print('#{} {}'.format(tc+1, len(d)))

# 4789

# for tc in range(int(input())):
#     nums = list(map(int, input()))
#     ap = nums[0]
#     cnt = 0
#     for i in range(1, len(nums)):
#         if ap >= i:
#             ap += nums[i]
#         else:
#             ap += nums[i]
#             cnt += 1
#             ap += 1
#     print('#{} {}'.format(tc+1, cnt))

# 7675

# for tc in range(int(input())):
#     n = int(input())
#     sen = list(input().split())
#     u = [chr(i) for i in range(65, 91)]
#     nums = '1234567890'
#     ans = [0] * n
#     cnt = 0
#     i = 0
#     for s in sen:
#         ucnt = 0
#         for j in range(len(s)):
#             if s[j] in u:
#                 ucnt += 1
#             if s[j] in nums:
#                 ucnt = 0
#                 break
#         if ucnt == 1:
#             cnt += 1
#         if s[-1] == '!' or s[-1] == '.' or s[-1] == '?':
#             ans[i] += cnt
#             i += 1
#             cnt = 0
#     print('#{} {}'.format(tc+1, ' '.join(map(str, ans))))


# 2806

# def check(j):
#     global cnt
#     if promising() ==:
#
#     elif c == n:
#         cnt += 1
#         return
#     else:
#
#
#
# def promising(j):
#     for i in range():
#
#
#
# for tc in range(int(input())):
#     n = int(input())
#     c = [0] * (n+1)
#     cnt = 0
#     check(1)
#     print('#{} {}'.format(tc+1, cnt))

# 6485

# for tc in range(int(input())):
#     n = int(input())
#     bus = list(list(map(int, input().split())) for _ in range(n))
#     p = int(input())
#     stops = list(int(input()) for _ in range(p))
#     total = [0] * 5001
#     for i in range(n):
#         for j in range(bus[i][0], bus[i][1]+1):
#             total[j] += 1
#     print('#{} '.format(tc+1), end= '')
#     for i in range(p):
#         print('{}'.format(total[stops[i]]), end = ' ')
#     print()

# 1873

# for TC in range(int(input())):
#     h, w = map(int, input().split())
#     field = [ list(input()) for _ in range(h)]
#     n = int(input())
#     given = input()
#     tank = [0, '>', '<', 'v', '^']
#     for i in range(h):
#         for j in range(w):
#             if field[i][j] in tank:
#                 tr = i
#                 tc = j
#     field[tr][tc] = tank.index(field[tr][tc])
#     dr = [0, 0, 0, 1, -1]
#     dc = [0, 1, -1, 0, 0]
#     for o in given:
#         if o == 'S':
#             cr = tr
#             cc = tc
#             d = field[tr][tc]
#             while True:
#                 nr = cr+dr[d]
#                 nc = cc+dc[d]
#                 if nr < 0 or nr >= h or nc < 0 or nc >= w: break
#                 if field[nr][nc] == '-' or field[nr][nc] == '.':
#                     cr = nr
#                     cc = nc
#                     continue
#                 elif field[nr][nc] == '*':
#                     field[nr][nc] = '.'
#                     break
#                 elif field[nr][nc] == '#':
#                     break
#         elif o == 'R':
#             field[tr][tc] = 1
#             if tc+dc[1] < w and field[tr+dr[1]][tc+dc[1]] == '.':
#                 field[tr+dr[1]][tc+dc[1]] = 1
#                 field[tr][tc] = '.'
#                 tr = tr+dr[1]
#                 tc = tc+dc[1]
#         elif o == 'L':
#             field[tr][tc] = 2
#             if 0 <= tc+dc[2] and field[tr+dr[2]][tc+dc[2]] == '.':
#                 field[tr+dr[2]][tc+dc[2]] = 2
#                 field[tr][tc] = '.'
#                 tr = tr+dr[2]
#                 tc = tc+dc[2]
#         elif o == 'D':
#             field[tr][tc] = 3
#             if tr+dr[3] < h and field[tr+dr[3]][tc+dc[3]] == '.':
#                 field[tr+dr[3]][tc+dc[3]] = 3
#                 field[tr][tc] = '.'
#                 tr = tr+dr[3]
#                 tc = tc+dc[3]
#         elif o == 'U':
#             field[tr][tc] = 4
#             if 0 <= tr+dr[4] and field[tr+dr[4]][tc+dc[4]] == '.':
#                 field[tr+dr[4]][tc+dc[4]] = 4
#                 field[tr][tc] = '.'
#                 tr = tr+dr[4]
#                 tc = tc+dc[4]
#     field[tr][tc] = tank[field[tr][tc]]
#     print('#{} '.format(TC+1), end='')
#     for i in range(h):
#         print('{}'.format(''.join(field[i])))

# 1860

# for tc in range(int(input())):
#     n, m, k = map(int, input().split())
#     c = list(map(int, input().split()))
#     t = [0] * (max(c)+1)
#     for s in c:
#         t[s] += 1
#     b = 0
#     result = 'Possible'
#     for i in range(len(t)):
#         if i > 0 and i % m == 0:
#             b += k
#         b -= t[i]
#         if b < 0:
#             result = 'Impossible'
#             break
#     print('#{} {}'.format(tc+1, result))

# 4831

# for tc in range(int(input())):
#     k, n, m = map(int, input().split())
#     s = list(map(int, input().split()))
#     st = list()
#     for i in s:
#         if n-k <= i:
#             st.append(i)
#             while st:
#                 a = st[-1]
#                 if a-k <= 0:
#                     st.insert(0, 0)
#                     break
#                 temp = []
#                 for j in range(s.index(a)-1, -1, -1):
#                     if a-k > s[j]:
#                         temp = s[j+1:]
#                         if temp[0] == a: break
#                         else:
#                             st.append(temp[0])
#                             temp = []
#                             a = st[-1]
#                 if len(st) == 1: st.pop()
#         if st != [] and st[0] == 0: break
#         elif st == []: continue
#     if len(st) == 0:
#         print('#{} {}'.format(tc+1, 0))
#     else:
#         print('#{} {}'.format(tc+1, len(st)-1))

# 1244

# for tc in range(int(input())):
#     arr = list(map(str, input().split()))
#     nums = [int(arr[0][i]) for i in range(len(arr[0]))]
#     print(nums)

# 3304

# for tc in range(int(input())):
#     str1, str2 = input().split()
#     st = []
#     for i in range(len(str1)):
#         for j in range(len(str2)):
#             if str1[i] == str2[j]:
#                 st.append(str1[i])
#                 break
#             elif str1[i] not in str2:
#                 break
#     print('#{} {}'.format(tc+1, len(st)))

# 5642

# for tc in range(int(input())):
#     n = int(input())
#     nums = list(map(int, input().split()))
#     st = []
#     for i in range(n):
#         st.append(nums[i])
#         for j in range(1, n):

# 3307

# for tc in range(int(input())):
#     n = int(input())
#     nums = list(map(int, input().split()))
#     maxl = 0
#     for i in range(n):
#         if nums[i] == max(nums) : continue
#         st = []
#         st.append(nums[i])
#         j = nums.index(st[-1]) + 1
#         while j < n:
#             if st[-1] <= nums[j]:
#                 st.append(nums[j])
#                 j = nums.index(st[-1]) + 1
#             else:
#                 j += 1
#         if maxl < len(st):
#             maxl = len(st)
#     print('#{} {}'.format(tc+1, maxl))

# 6190

def monotoneincreasing(x):
    x = str(x)
    i = len(x)
    while i > 1:
        if int(x[i-1]) >= int(x[i-2]):
            i -= 1
        else:
            return False
    return True

for tc in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    maxV = -1
    for i in range(n):
        for j in range(i+1, n):
            num = nums[i]*nums[j]
            if num >= 10 and monotoneincreasing(num) and num > maxV:
                maxV = num
            elif num < 10:
                maxV = num
    print('#{} {}'.format(tc+1, maxV))

