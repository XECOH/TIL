def find(row, expense):
    global minE
    if row == n:
        if expense < minE:
            minE = expense
            return
    if expense > minE:
        return
    for i in range(n):
        if selected[i] == 0:
            selected[i] = 1
            find(row+1, expense+v[row][i])
            selected[i] = 0

for tc in range(1, int(input())+1):
    n = int(input())
    v = [list(map(int, input().split())) for _ in range(n)]
    minE = 1000000
    selected = [0] * n
    find(0, 0)
    print('#{} {}'.format(tc, minE))