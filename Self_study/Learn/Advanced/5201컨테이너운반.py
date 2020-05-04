for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    w = sorted(list(map(int, input().split())), reverse = True)
    t = sorted(list(map(int, input().split())), reverse = True)
    W = 0
    for i in range(m):
        j = 0
        q = len(w)
        while j < q:
            if w[j] <= t[i]:
                W += w[j]
                w.pop(j)
                q = len(w)
                break
            else:
                j += 1
    print('#{} {}'.format(tc, W))