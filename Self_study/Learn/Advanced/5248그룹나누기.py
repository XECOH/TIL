def find(idx):
    global ans
    selected[idx] = 1
    Q = []
    for i in range(1, n+1):
        if i == idx: continue
        if applications[idx][i] == 1 and selected[i] == 0:
            selected[i] = 1
            Q.append(i)
    while Q:
        nidx = Q.pop(0)
        for j in range(1, n+1):
            if j == nidx: continue
            if applications[nidx][j] == 1 and selected[j] == 0:
                selected[j] = 1
                Q.append(j)
    ans += 1
    return

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    applications = [[0]*(n+1) for _ in range(n+1)]
    for i in range(0, m*2, 2):
        applications[nums[i]][nums[i+1]] = 1
        applications[nums[i+1]][nums[i]] = 1
    ans = 0
    selected = [0] * (n+1)
    for i in range(1, n+1):
        if selected[i] == 1: continue
        else:
            find(i)
    print('#{} {}'.format(tc, ans))