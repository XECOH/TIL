def find(w, h, d):
    global ans
    visited[w] = 1
    if d > ans:
        return
    if visited.count(1) == h+1:
        if d+distance[w][1] < ans:
            ans = d+distance[w][1]
        return
    for i in range(n+2):
        if i == 1 or visited[i] == 1: continue
        find(i, h, d+distance[w][i])
        visited[i] = 0

for tc in range(1, int(input())+1):
    n = int(input())
    coordinates = list(map(int, input().split()))
    distance = [[0]*(n+2) for _ in range(n+2)]
    for i in range(n+2):
        for j in range(n+2):
            if i == j: continue
            else: distance[i][j] = abs(coordinates[i*2]-coordinates[j*2]) + abs(coordinates[i*2+1]-coordinates[j*2+1])
    ans = 100000000000
    visited = [0] * (n+2)
    find(0, n, 0)
    print(f'#{tc} {ans}')