def binarysearch(arr, key):
    global ans
    l = 0
    h = N-1
    start = None
    while l <= h:
        m = (l + h) // 2
        if arr[m] == key:
            ans += 1
            break
        elif arr[m] > key:
            h = m - 1
            current = 'L'
        else:
            l = m + 1
            current = 'R'
        if start == current: break
        start = current
    return

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    ans = 0
    for b in B:
        binarysearch(A, b)
    print('#{} {}'.format(tc, ans))