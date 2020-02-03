
# 1204
from collections import Counter
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
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     price_lst = list(map(int, input().split()))
#     expenditure = []
#     sum_price = 0
#     sell_price = 0
#     interest = 0
#     l_i = 0
#     l_i_lst = []
#     for i in range(1, len(price_lst)):
#         sum_price += price_lst[i-1]
#         sell_price = price_lst[i] * i 
#         if sell_price > sum_price:
#             l_i = i
#             l_i_lst.append(l_i)
    # for i in range(len(l_i_lst)):
    #     sum_price += price_lst[i]
    #     sell_price = price_lst[i] * i 
    # print(l_i_lst)
    # print(expenditure)
    # for i in range(len(expenditure)):
    #     result += expenditure[i]
    # print(f'#{tc} {result}')   

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
#     result = ['0'] * (N**2)
#     result[0] = '1'
#     result[N-1] = str(N)
#     result[N**2-1] = str(2*N - 1)
#     result[N**2 -N] = str(3*N - 2)
#     for i in range(1, N):
#         result[i] = str(i+1)
#     r_n = ' '.join(result)
#     for i in range(1, N+1):
#         print(r_n[2*N*(i-1):2*N*i])

# 1961
# def ro90(list):
#     result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#     for i in range(len(list)):
#         for j in range(len(list)):
#             if i == 0:
#                 list[0][j] = result[j][2]
#             elif i == 1:
#                 list[1][j] = result[j][1]
#             else:
#                 list[2][j] = result[j][0]
#     return result

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     matrix = []
#     for i in range(N):
#         matrix.append(list(map(int, input().split())))
#     print(ro90(matrix))


# 1970

changes = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counting = []
    result = []
    remain = N
    for change in changes:
        if change > N:
            counting.append(0)
            continue
        k = 0
        while remain > 0:
            k += 1
            remain -= change * k
        counting.append(k-1)
    print(counting)


# 1979

# T= int(input())
# for tc in range(1, T+1):
#     n, m = map(int, input().split())
#     matrix = []
#     for i in range(n):
#         matrix.append(list(map(int, input().split())))
#     dr = []