# 5174

for tc in range(1, int(input())+1):
    e, n = map(int, input().split())
    child1 = [0] * (e+2)
    child2 = [0] * (e+2)
    nods = list(map(int, input().split()))
    for i in range(0, e*2, 2):
        if child1[nods[i]] == 0:
            child1[nods[i]] = nods[i+1]
        else:
            child2[nods[i]] = nods[i+1]
    cnt = 1
    n1 = n
    n2 = n
    while True:
        if child1[n1] != 0:
            cnt += 1
            n1 = child1[n1]
        if child2[n2] != 0:
            cnt += 1
            n2 = child2[n2]
        if child1[n1] == 0 and child2[n2] == 0: break
    print('#{} {}'.format(tc, cnt))