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
#     elif L <= X <= U
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

# 1230

# T = 1
# for tc in range(1, T+1):
#     n = int(input())
#     code = list(map(int, input().split()))
#     o = int(input())
#     order = list(map(str, input().split()))
#     for i in range(len(order)):
#         if order[i] != 'I' and order[i] != 'D' and order[i] != 'A':
#             order[i] = int(order[i])
#     print(order)
#     for i in range(len(order)):
#         if order[i] == 'I':
#             code.insert(order[i+1], order[i+3:i+3+order[i+2]])
#         elif order[i] == 'A':
#             code.append(order[i+2:i+2+(order[i+2])])
#         elif order[i] == 'D':
#             code.remove(order[i+1]-1)
#         else:
#             continue
#     print(code)

# 1289

# T = int(input())
# for tc in range(1, T+1):
#     original = input()
#     now = '0' * len(original)


# 3131

# n=10**6
# a = [False,False] + [True]*(n-1)
# primes=[]
#
# for i in range(2,n+1):
#     if a[i]:
#         primes.append(i)
#     for j in range(2*i, n+1, i):
#         a[j] = False
# for i in range(len(primes)):
#    print(primes[i], end=' ')

# 4698

# n = 10**6
#
# c = [False, False] + [True] * (n - 1)
# primelist = []
#
# for i in range(2, n + 1):
#     if c[i]:
#         primelist.append(i)
#         for j in range(2 * i, n + 1, i):
#             c[j] = False
#
# T = int(input())
# for tc in range(1, T+1):
#     d, a, b = map(int, input().split())
#     cnt = 0
#     for i in primelist:
#         if a <= i <= b and str(d) in str(i):
#             cnt += 1
#     print('#{} {}'.format(tc, cnt))

# 5986

# n = 1000
#
# c = [False, False] + [True] * (n - 1)
# primelist = []
#
# for i in range(2, n + 1):
#     if c[i]:
#         primelist.append(i)
#         for j in range(2 * i, n + 1, i):
#             c[j] = False
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     cnt = 0
#     for x in range(len(primelist)):
#         for y in range(x, len(primelist)):
#             for z in range(y, len(primelist)):
#                 if primelist[x] + primelist[y] + primelist[z] == N:
#                     cnt += 1
#
#     print('#{} {}'.format(tc, cnt))

# 3750
# def f(n):
#     if len(n) > 1:
#         sum = 0
#         for i in range(len(n)):
#             sum += int(n[i])
#         n = str(sum)
#         if len(n) > 1:
#             return f(n)
#         else:
#             return int(n)
#     else:
#         return int(n)
#
# T = int(input())
# for tc in range(1, T+1):
#     n = input()
#     print('#{} {}'.format(tc, f(n)))

# 5607

# T = int(input())
# for tc in range(1, T+1):
#     n, r = map(int, input().split())
#     temp = 1
#     if r == 0:
#         result = 1
#     if r > n // 2:
#         r = n - r
#     for i in range(r):
#         temp *= n-i
#         temp /= r-i
#         result = temp % 1234567891
#     print('#{} {}'.format(tc, result))

# 6190

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = list(map(int, input().split()))
    mm = []
    multiple = [i for i in range(10, 30000**2+1)]
    for i in range(N):
        for j in range(N):
            if i != j:
                t = matrix[i] * matrix[j]
                if t not in mm:
                    mm.append(t)

    for i in multiple:
        for j in range(len(str(i))-1):
            if int(str(i)[j]) - int(str(i)[j+1]) > 0:
                multiple.remove(i)
            else:
                continue

# 1216
#
# T = 1
# for tc in range(1, T+1):
#     N = int(input())
#     words = [list(map(str, input())) for _ in range(100)]
#     cntr = 0
#     result = []
#     for i in range(100):
#         for j in range(100):
#             temp = ''
#             for k in range(100):
#                 if j + k <= 99:
#                     temp += words[i][j+k]
#                     if temp == temp[::-1]:
#                         if len(temp) > cntr:
#                             cntr = len(temp)
#                     else:
#                         continue
#     cnth = 0
#     for i in range(100):
#         for j in range(100):
#             temp = ''
#             for k in range(100):
#                 if j + k <= 99:
#                     temp += words[j+k][i]
#                     if temp == temp[::-1]:
#                         if len(temp) > cnth:
#                             cnth = len(temp)
#                     else:
#                         continue
#     if cntr > cnth:
#         print('#{} {}'.format(tc, cntr))
#     else:
#         print('#{} {}'.format(tc, cnth))

# 1230

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
#         elif f4[i] == 'D':
#             for j in range(int(f4[i+2])):
#                 s.pop(int(f4[i+1]))
#         elif f4[i] == 'A':
#             for j in range(int(f4[i+1])):
#                 s.append(int(f4[i+2])+j)
#         else:
#             continue
#     print('#{} '.format(tc), end= '')
#     for i in range(10):
#         print('{}'.format(s[i]), end= ' ')
#     print()

# 1234

# T = 10
# for tc in range(1, T+1):
#     l, s = input().split()
#     s = list(map(int, s))
#     st = list()
#     for i in range(int(l)):
#         if not st or st[-1] != s[i]:
#             st.append(s[i])
#         elif st and st[-1] == s[i]:
#             st.pop()
#     print('#{} {}'.format(tc, ''.join(map(str, st))))


# 4676

# T = int(input())
# for tc in range(1, T+1):
#     s = list(input())
#     n = int(input())
#     li = list(map(int, input().split()))
#     cnt = [0 for _ in range(len(s))]
#     for i in range(n):
#         for j in range(1, len(cnt)+1):
#             if li[i] == j:
#                 cnt[j-1] += 1
#     li.sort()
#     li=list(set(li))
#     for i in range(len(li)):
#         s.insert(li[i], (cnt[li[i]]) * '-')
#     print(s)

# 3975

# T = int(input())
# for tc in range(1, T+1):
#     a, b, c, d = map(int, input().split())
#     alice = a / b
#     bob = c / d
#     if alice == bob:
#         print('#{} {}'.format(tc, 'DRAW'))
#     elif alice > bob:
#         print('#{} {}'.format(tc, 'ALICE'))
#     else:
#         print('#{} {}'.format(tc, 'BOB'))

# 1240

# T = int(input())
# num = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
# for tc in range(1, T+1):
#     n, m = map(int, input().split())
#     code = [list(map(int, input())) for _ in range(n)]
#     ncode = []
#     nncode = []
#     sri = 0
#     for i in range(n):
#         if 1 in code[i]:
#             sri = i
#             break
#     sci = 0
#     for i in range(m-1, -1, -1):
#         if code[sri][i] == 1:
#             sci = i
#             break
#     ncode = code[sri][sci-55:sci+1]
#     for i in range(8):
#         for j in range(10):
#             if ''.join(map(str, ncode[7*i:7*(i+1)])) == num[j]:
#                 nncode.append(j)
#
#     check = 0
#     if (((nncode[0]+nncode[2]+nncode[4]+nncode[6])*3 + nncode[1]+ nncode[3] + nncode[5]) % 10 + nncode[7]) % 10 == 0:
#         for i in nncode:
#             check += i
#     else:
#         check = 0

    # print('#{} {}'.format(tc, check))

# 2948

# T = int(input())
# for tc in range(1, T+1):
#     n, m = map(int, input().split())
#     nl = list(map(str, input().split()))
#     ml = list(map(str, input().split()))
#     tl = list(set(nl+ml))
#     result = n+m - len(tl)
#     print('#{} {}'.format(tc, result))

# 3233

# T = int(input())
# for tc in range(1, T+1):
#     a, b = map(int, input().split())

# 3282

# T = int(input())
# for tc in range(1, T+1):
#     n, k = map(int, input().split())
#     items = [list(map(int, input().split())) for _ in range(n)]
#     maxV = 0
#     for i in range(n):
#         temp = 0
#         for j in range(i+1, n):
#             if (items[i][0] + items[j][0]) <= k:
#                 temp += items[i][1] + items[j][1]
#                 if temp > maxV:
#                     maxV = temp
#                     temp = 0
#     print('#{} {}'.format(tc, maxV))