def fjs(player):
    l = len(player)
    cnt = 0
    for i in range(l-1):
        if player[i+1] - player[i] != 1:
            cnt = 0
        else:
            cnt += 1
        if cnt >= 2:
            return 1
    return 0

def babyjin(player):
    l = len(player)
    i = 0
    while i < l:
        if player.count(player[i]) >= 3:
            return 1
        else:
            i += 1
    return 0

for tc in range(1, int(input())+1):
    cards = list(map(int, input().split()))
    i = 3
    while i < 7:
        p1 = sorted([cards[j] for j in range(0, i*2, 2)])
        p2 = sorted([cards[j] for j in range(1, i*2, 2)])
        r1 = fjs(p1)
        b1 = babyjin(p1)
        r2 = fjs(p2)
        b2 = babyjin(p2)

        i += 1

    if i == 7:
        print('#{} {}'.format(tc, 0))