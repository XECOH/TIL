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
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price_lst = list(map(int, input().split()))
    expenditure = []
    sum_price = 0
    sell_price = 0
    interest = 0
    for i in range(1, len(price_lst)+1):
        if price_lst[i-1] <= 10000 and 2 <= N <=1000000:
            sum_price += price_lst[i-1]
            sell_price = price_lst[i] * i 
            if sell_price > sum_price:
                interest = sell_price - sum_price
                expenditure.append(interest)
            
    print(expenditure)
    if expenditure[0] < 0:    
        result = 0
    else:
        result = expenditure[0]
    print(f'#{tc} {result}')   
