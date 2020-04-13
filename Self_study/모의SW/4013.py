for tc in range(1, int(input())+1):
    k = int(input())
    magnets = [[0]*9]+[[0]+list(map(int, input().split())) for _  in range(4)]
    rotation = [0]*5
    for _ in range(k):
        m, r = map(int, input().split())
        rotation[m] = r
        i = 0
        while i < 3:
            if m+i+1 < 5 and magnets[m+i][3] != magnets[m+i+1][7] and rotation[m+i] != 0:
                rotation[m+i+1] = -rotation[m+i]
            if 0 < m-i-1 and magnets[m-i][7] != magnets[m-i-1][3] and rotation[m-i] != 0:
                rotation[m-i-1] = -rotation[m-i]
            i += 1
        for i in range(1, 5):
            if rotation[i] != 0:
                if rotation[i] == 1:
                    st = magnets[i].pop()
                    magnets[i].insert(1, st)
                else:
                    st = magnets[i].pop(1)
                    magnets[i].append(st)
        rotation = [0]*5
    point = 0
    for j in range(1, 5):
        point += (magnets[j][1] * (2**(j-1)))
    print('#{} {}'.format(tc, point))