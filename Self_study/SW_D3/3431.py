for tc in range(1, int(input())+1):
    l, u, x = map(int, input().split()) # l분 이상 u분 이하 운동해야 하는데, x분 만큼 운동
    if x < l: # 최소보다 작으면 최소만큼 더 운동해야 하고
        print('#{} {}'.format(tc, l-x))
    elif l <= x <= u: # 그 사이에 있으면 운동 안해도 되고
        print('#{} {}'.format(tc, 0))
    else: # 그렇지 않은 경우는 이미 더 한거
        print('#{} {}'.format(tc, -1))