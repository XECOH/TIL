def backtrack(idx, remain, cnt):
    global N, minC, stops
    remain -= 1
    if idx == N:
        if cnt < minC:
            minC = cnt
        return
    if cnt > minC:
        return
    backtrack(idx+1, stops[idx], cnt+1)
    if remain > 0:
        backtrack(idx+1, remain, cnt)

for tc in range(1, int(input())+1):
    stops = list(map(int, input().split()))
    N = stops[0]
    minC = 10000000
    backtrack(2, stops[1], 0)
    print('#{} {}'.format(tc, minC))