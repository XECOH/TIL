def find(end, l, cnt):
    global maxT
    for i in range(l, n):
        s = times[i][0]
        if s >= end:
            find(times[i][1], i+1, cnt+1)
    if cnt > maxT : maxT = cnt
    return

for tc in range(1, int(input())+1):
    n = int(input())
    times = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x: (x[0], x[1]))
    maxT = 0
    for i in range(n):
        e = times[i][1]
        t = 1
        for j in range(i+1, n):
            s = times[j][0]
            if s >= e:
                find(times[j][1], j+1, t+1)
    print('#{} {}'.format(tc, maxT))