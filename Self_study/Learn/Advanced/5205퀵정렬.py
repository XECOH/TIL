for tc in range(1, int(input())+1):
    n = int(input())
    l = list(map(int, input().split()))
    print('#{} {}'.format(tc, ans[n//2]))