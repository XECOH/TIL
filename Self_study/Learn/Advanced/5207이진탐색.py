def binarysearch(x, arr):
    c = (len(arr)-1) // 2
    if x == arr[c]:
        return
    left = arr[:c]
    right = arr[c+1:]
    if x < arr[c] and x in left:
        binarysearch(x, left)
    elif x > arr[c] and x in right:
        binarysearch(x, right)
    return -1

for tc in range(1, int(input())+1):
    ans = 0
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))
    for num in b:
        binarysearch(num, a)
        if == 0: ans += 1
    print('#{} {}'.format(tc, ans))