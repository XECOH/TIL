def merge(L, R):
    global p
    ans = [0] * (len(L)+len(R))
    if L[-1] > R[-1]:
        p += 1
    l, r = 0, 0
    i = 0
    while len(L) != l  and len(R) != r:
        if L[l] < R[r]:
            ans[i] = L[l]
            l += 1
            i += 1
        else:
            ans[i] = R[r]
            i += 1
            r += 1
    if len(L) != l:
        while len(L) != l:
            ans[i] = L[l]
            i += 1
            l += 1
    if len(R) != r:
        while len(R) != r:
            ans[i] = R[r]
            i += 1
            r += 1
    return ans

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    c = len(arr)//2
    left = mergesort(arr[:c])
    right = mergesort(arr[c:])
    return merge(left, right)

for tc in range(1, int(input())+1):
    n = int(input())
    l = list(map(int, input().split()))
    p = 0
    merged = mergesort(l)
    print('#{} {} {}'.format(tc, merged[n//2], p))