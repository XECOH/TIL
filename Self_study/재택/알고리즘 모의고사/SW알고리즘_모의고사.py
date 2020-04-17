def find(R, C):
    global ans
    dr = [-1, -1, -1, 0, 1, 1, 1, 0] # 8방 탐색
    dc = [-1, 0, 1, 1, 1, 0, -1, -1] # 8방 탐색
    constellation = [[R, C]] # 스택으로 구현
    maps[R][C] = -1 # 다시 찾지 않도록 값 변경
    while constellation: # 스택이 비게 되면 8방에 더 이상 별이 없다는 듯
        [cr, cc] = constellation.pop()
        for d in range(8):
            if cr + dr[d] >= 10 or cr + dr[d] < 0 or cc + dc[d] >= 10 or cc + dc[d] < 0 : continue # 맵의 인덱스를 벗어난 범위 일때
            if maps[cr + dr[d]][cc + dc[d]] == 1: # 8방 탐색 중 별이 있으면
                constellation += [[cr + dr[d], cc + dc[d]]] # 스택에 집어 넣고
                maps[cr + dr[d]][cc + dc[d]] = -1 # 다시 찾지 않도록 값 변경
    ans += 1 # 다 하고나면 별자리 하나를 찾았으므로 별자리 개수를 하나 올려 줌
    return

for tc in range(1, int(input())+1):
    maps = [list(map(int, input().split())) for _ in range(10)] # 맵 입력 받기
    ans = 0 # 별자리 개수
    for r in range(10):
        for c in range(10):
            if maps[r][c] == 1: # 별일 때만
                find(r, c) # 별자리 찾기
    print('#{} {}'.format(tc, ans))
