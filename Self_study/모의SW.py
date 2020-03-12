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

# 4013

for tc in range(1, int(input())+1):
    k = int(input())
    magnets = [[0]*9]+[[0]+list(map(int, input().split())) for _  in range(4)]
    rotation = [0]*5
    for _ in range(k):
        m, r = map(int, input().split())
        rotation[m] = r
        i = 0
        while i < 3:
            if m+i+1 < 5 and magnets[m+i][3] != magnets[m+i+1][7] and rotation[m+i] != 0:
                rotation[m+i+1] = -rotation[m+i]
            if 0 < m-i-1 and magnets[m-i][7] != magnets[m-i-1][3] and rotation[m-i] != 0:
                rotation[m-i-1] = -rotation[m-i]
            i += 1
        for i in range(1, 5):
            if rotation[i] != 0:
                if rotation[i] == 1:
                    st = magnets[i].pop()
                    magnets[i].insert(1, st)
                else:
                    st = magnets[i].pop(1)
                    magnets[i].append(st)
        rotation = [0]*5
    point = 0
    for j in range(1, 5):
        point += (magnets[j][1] * (2**(j-1)))
    print('#{} {}'.format(tc, point))