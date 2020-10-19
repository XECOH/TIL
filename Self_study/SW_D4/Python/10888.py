from itertools import combinations

def f(r):
    global n, maps, stores, answer
    if r > len(stores): return
    combi = list(combinations(stores, r))
    for c in combi:
        sums = []
        if len(list(c)) == 1:
            for i in range(n):
                for j in range(n):
                    if maps[i][j] == 1:
                        sums.append(abs(c[0][0]-i)+abs(c[0][1]-j))
            answer = min(sum(sums)+maps[c[0][0]][c[0][1]], answer)
        else:
            for i in range(n):
                for j in range(n):
                    if maps[i][j] == 1:
                        temp = []
                        for k in list(c):
                            temp.append(abs(k[0]-i)+abs(k[1]-j))
                        sums.append(min(temp))
            for k in list(c):
                sums.append(maps[k[0]][k[1]])
            answer = min(sum(sums), answer)
    f(r+1)

for tc in range(1, int(input())+1):
    n = int(input())
    answer = 10000000000
    maps = [ list(map(int, input().split())) for _ in range(n) ]
    stores = []
    for r in range(n):
        for c in range(n):
            if maps[r][c] > 1:
                stores.append([r, c])
    f(1)
    print(f'#{tc} {answer}')