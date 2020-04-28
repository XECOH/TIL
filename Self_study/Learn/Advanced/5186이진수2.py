for tc in range(1, int(input())+1):
    n = float(input())
    ans = ''
    t = -1
    while True:
        if len(ans) >= 13:
            ans = 'overflow'
            break
        if n >= 2**t:
            ans += '1'
            n -= 2**t
            t -= 1
        else:
            ans += '0'
            t -= 1
        if n == 0: break
    print('#{} {}'.format(tc, ans))