def fjs(player):
    player = list(set(player))
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

def triplet(player):
    l = len(player)
    for i in range(l):
        if player.count(player[i]) >= 3:
            return 1
    return 0

for tc in range(1, int(input())+1):
    ans = 0
    cards = list(map(int, input().split()))
    i = 3
    while i < 7:
        p1 = sorted([cards[j] for j in range(0, i*2, 2)])
        r1 = fjs(p1)
        b1 = triplet(p1)
        if r1 != 0 or b1 != 0:
            ans = 1
            break
        p2 = sorted([cards[j] for j in range(1, i*2, 2)])
        r2 = fjs(p2)
        b2 = triplet(p2)
        if r2 != 0 or b2 != 0:
            ans = 2
            break
        i += 1
    print('#{} {}'.format(tc, ans))