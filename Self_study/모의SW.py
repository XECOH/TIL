# 5658

# for tc in range(int(input())):
#     n, k = map(int, input().split())
#     six = input()
#     ans = []
#     for i in range(n//4):
#         for j in range(0, n, n//4):
#             if six[j+(n*i):j+(n*i)+(n//4)] not in ans:
#                 ans.append(six[j+(n*i):j+(n*i)+(n//4)])
#         six += six[i+1:n] + six[0:i+1]
#     result = [int(i, 16) for i in ans]
#     result.sort(reverse = True)
#     print('#{} {}'.format(tc+1, result[k-1]))

# 4012

for tc in range(int(input())):
    n = int(input())
    table = [[0]*(n+1)]+[[0]+list(map(int, input().split())) for _ in range(n)]
    diff = 1000000000
    print('#{} {}'.format(tc+1, diff))

