def knapsack(N, K):
    bags = [[0 for _ in range(K+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, K+1):
            if v_list[i-1] > j:
                bags[i][j] = bags[i-1][j]
            else:
                bags[i][j] = max(c_list[i-1]+bags[i-1][j-v_list[i-1]], bags[i-1][j])
    return bags[N][K]

for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    v_list = []
    c_list = []
    for _ in range(n):
        v, c = map(int, input().split())
        v_list.append(v)
        c_list.append(c)
    print(f'#{tc} {knapsack(n, k)}')