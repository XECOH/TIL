def quicksort(arr, left, right):
    if left < right:
        pivot = hoare_partition(arr, left, right)
        quicksort(arr, left, pivot-1)
        quicksort(arr, pivot+1, right)

def hoare_partition(arr, left, right):
    l = left
    r = right
    pivot = arr[left]
    while l <= r:
        while l <= r and arr[l] <= pivot:
            l += 1
        while l <= r and arr[r] >= pivot:
            r -= 1
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
    arr[left], arr[r] = arr[r], arr[left]
    return r

for tc in range(1, int(input())+1):
    n = int(input())
    a = list(map(int, input().split()))
    quicksort(a, 0, n-1)
    print('#{} {}'.format(tc, a[n//2]))