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

def synergy(s, r):
    global diff
    check = [0]*(n+1)
    for _ in range(r):
        check[1] = 1
        i = 2
        while i < n+1:
            check[i] = 1


for tc in range(int(input())):
    n = int(input())
    diff = 1000000000000000000
    table = [[0]*(n+1)]+[[0]+list(map(int, input().split())) for _ in range(n)]
    repeat = 1
    for i in range((n//2)-1):
        repeat *= (n-1)-i
        repeat /= (n//2)-1-i
    synergy(1, int(repeat))

# 2105

# for tc in range(int(input())):
#     n = int(input())
#     region = [list(map(int, input().split())) for _ in range(n)]
#     maxD = -1
#     di = [1, 1, -1, -1]
#     dj = [1, -1, -1, 1]
#     for i in range(n):
#         for j in range(n):
#             for k in range(4):

# 5653

# for tc in range(int(input())):
#     n, m, k = map(int, input().split())
#     grid = [list(map(int, input().split())) for _ in range(n)]
    
# 1953

# for tc in range(int(input())):
#     n, m, r, c, l = map(int, input().split())
#     base = [list(map(int, input().split())) for _ in range(n)]
#     check = [[0]*m for _ in range(n)]
#     cnt = 0
#     for 
#     print('#{} {}'.format(tc+1, cnt))

# 2382

for tc in range(int(input())):
    n, m, k = map(int, input().split())
    