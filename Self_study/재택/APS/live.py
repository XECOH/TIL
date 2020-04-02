def f(i, j):
    if i == j:
        return i
    else:
        l = f(i, (i+j)//2)
        r = f((i+j)//2+1, j)
        p = [l, r]
        return p[w[card[l]][card[r]]]

for tc in range(1, int(input())+1):
    n = int(input())
    card = [0] + list(map(int, input().split()))
    w = [[0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0]]
    print('#{} {}'.format(tc, f(1, n)))

def find(n, k, s):
    global minS
    if n == k:
        if s < minS:
            minS = s
    elif minS <= s:
        return
    else:
        for i in range(k):
            if cols[i] == 0:
                cols[i] = 1
                find(n+1, k, s+arr[n][i])
                cols[i] = 0
                
for tc in range(1, int(input())+1):
    minS = 1000000000
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cols = [0] * n
    find(0, n, 0)
    print('#{} {}'.format(tc, minS))