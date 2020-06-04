for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    friends = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        friends[a][b], friends[b][a] = 1, 1
    ans = 0
    given = [0]*(n+1)
    st = []
    for i in range(2, n+1):
        if 1 not in friends[i]: break
        if friends[1][i] == 1:
            given[i] = 1
            st.append(i)
            ans += 1
    while st:
        f = st.pop(0)
        for j in range(2, n+1):
            if given[j] != 1 and friends[f][j] == 1:
                given[j] = 1
                ans += 1
    print(f'#{tc} {ans}')