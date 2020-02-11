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
#     s_i = 0
#     for i in range(len(original)):
#         if original[i] == 1:
#             s_i = i
#             break
#     cnt = 0
#     for i in range(s_i+1, len(now)):
#         now[s_i] = 1
#         now[i] = 1
#         cnt += 1

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
    multiple = []
    for i in range(N):
        for j in range(N):
            if i != j:
                if matrix[i] * matrix[j] not in multiple and matrix[i] * matrix[j] >= 10:
                    multiple.append(matrix[i]*matrix[j])
                else:
                    continue
    maxV = -1
    for i in range(len(multiple)):
        for j in range(len(str(multiple[i]))-1):
            k = 0
            while k < len(str(multiple[i])):
                if int(str(multiple[i])[j]) - int(str(multiple[i])[j]) <= 0:
                    k += 1
                else:
                    break
            if k == len(str(multiple[i]))-1:
                if maxV < multiple[i]:
                    maxV = multiple[i]
    print('#{} {}'.format(tc, maxV))


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