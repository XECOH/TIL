for tc in range(1, int(input())+1):
    n, h = map(str, input().split())
    nums = [ str(num) for num in range(0, 10) ]
    ans = ''
    for num in h:
        if num in nums:
            ans += '0'*(4-(len(bin(int(num)))-2))+bin(int(num))[2:]
        else:
            ans += bin(int(num, 16))[2:]
    print('#{} {}'.format(tc, ans))