import itertools

def taste(arr):
    global minD
    b = [ ing for ing in range(1, n+1) if ing not in arr ]
    l = len(arr)
    sa = 0
    sb = 0
    for i in range(l-1):
        for j in range(i+1, l):
            sa += synergy[arr[i]][arr[j]]
            sa += synergy[arr[j]][arr[i]]
            sb += synergy[b[i]][b[j]]
            sb += synergy[b[j]][b[i]]
    diff = abs(sa-sb)
    if minD > diff:
        minD = diff
    return

for tc in range(1, int(input())+1):
    n = int(input())
    synergy = [[0]*(n+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]
    minD = 100000000000000000
    a = list(itertools.combinations([i for i in range(1, n+1)], n//2))
    for i in range(len(a)):
        taste(a[i])
    print('#{} {}'.format(tc, minD))
