def rotate():
    global grid
    newarr = [[0 for _ in range(int(n))] for _ in range(int(n))]
    for i in range(int(n)):
        for j in range(int(n)):
            newarr[j][int(n)-i-1] = grid[i][j]
    grid = newarr

for tc in range(1, int(input())+1):
    n, d = input().split()
    grid = [list(map(int, input().split())) for _ in range(int(n))]
    result = []
    if d == 'left':
        rotate()
        rotate()
    elif d == 'up':
        rotate()
    elif d == 'down':
        rotate()
        rotate()
        rotate()
    for i in range(int(n)):
        st = [j for j in grid[i] if j != 0]
        for k in range(len(st)-1, 0, -1):
            if st[k] == st[k-1]:
                st[k] *= 2
                st[k-1] = 0
            else: continue
        temp = [j for j in st if j != 0]
        t = len(temp)
        while t != int(n):
            temp.insert(0, 0)
            t += 1
        result.append(temp)
    grid = [result[i] for i in range(int(n))]

    if d == 'left':
        rotate()
        rotate()
    elif d == 'up':
        rotate()
        rotate()
        rotate()
    elif d == 'down':
        rotate()

    print('#{}'.format(tc))
    for k in range(int(n)):
        print(' '.join(map(str, grid[k])))