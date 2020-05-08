def merge(L, R):
    global p
    ans = []
    if L[-1] > R[-1]:
        p += 1
    while len(L) > 0 and len(R) > 0:
        if L[0] < R[0]:
            ans += [L.pop(0)]
        else:
            ans += [R.pop(0)]
    if len(L) > 0:
        ans += L
    if len(R) > 0:
        ans += R
    return ans

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    c = len(arr)//2
    left = arr[:c]
    right = arr[c:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)

for tc in range(1, int(input())+1):
    n = int(input())
    l = list(map(int, input().split()))
    p = 0
    merged = mergesort(l)
    print('#{} {} {}'.format(tc, merged[n//2], p))