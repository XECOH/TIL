ans = [[1]] + [[1, 1] for _ in range(69)]
i = 2
while i < 70:
    for j in range(1, i):
        ans[i].insert(j, (ans[i-1][j-1] + ans[i-1][j]))
    i += 1

for tc in range(1, int(input())+1):
    n, a, b = map(int, input().split())
    print('#{} {}'.format(tc, ans[n][a])