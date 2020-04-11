# 1
def is_palindrome(list): # 회문인지 확인하는 함수인듯
    for i in range(1, int(len(list)/2)+1):
        if list[i-1] == list[-i]:
            continue
        else:
            return False
            break
    return True

T = 10
for tc in range(1, T+1):
    l = int(input())
    board = [list(map(str, input())) for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(8-l+1):
            tempr = [] # 가로 확인
            for k in range(l):
                tempr.append(board[i][j+k])
            if is_palindrome(tempr):
                cnt += 1
            tempc = [] # 세로 확인
            for k in range(l):
                tempc.append(board[j+k][i])
            if is_palindrome(tempc):
                cnt += 1
    print('#{} {}'.format(tc, cnt))

# 2
for tc in range(1, 11):
    cnt = 0
    l = int(input()) # 찾아야하는 회문의 길이
    wordstable = [list(input()) for _ in range(8)]
    for i in range(8): # 세로를 가로로 만들어 행으로 추가
        temp = []
        for j in range(8):
            temp += wordstable[j][i]
        wordstable += [temp]

    for i in range(16):
        for j in range(8-l+1):
            words = wordstable[i][j:j+l]
            if words == words[::-1]:
                cnt += 1

    print('#{} {}'.format(tc, cnt))

# 3
for tc in range(1, 11):
    cnt = 0
    l = int(input()) # 찾아야하는 회문의 길이
    wordstable = [list(input()) for _ in range(8)]
    for i in range(8): # 가로 확인
        for j in range(8-l+1):
            words = wordstable[i][j:j+l]
            if words == words[::-1]:
                cnt += 1
    for i in range(8): # 세로 확인
        for j in range(8-l+1):
            words = ''
            for k in range(l):
                words += wordstable[j+k][i]
            if words == words[::-1]:
                cnt += 1

    print('#{} {}'.format(tc, cnt))