def pipe(sr, sc, er, ec):
    global cnt
    if er == n and ec == n:
        cnt += 1
    elif er == n:
        return
    else:
        dr = [0, 1, 1] # 오른쪽 옆, 오른쪽 대각선 아래, 아래
        dj = [1, 1, 0]
        for d in range(3):



n = int(input())
home = [[0]*(n+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]
cnt = 0
pipe(1, 1, 1, 2)
print(cnt)