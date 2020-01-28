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

T = int(input())
L_n = []
result = []
for i in range(1, T+1):
    N = input()
    if 1 <= int(N) <= 10**6:
        for j in range(len(N)):
            L_n.append(N[j])
            result.append(L_n[j])

