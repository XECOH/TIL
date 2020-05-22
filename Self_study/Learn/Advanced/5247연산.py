from collections import deque

def operation():
    global ans, m, Q, checked
    while Q:
        num, cnt = Q.popleft()
        if num == m:
            ans = cnt
            return
        for i in range(4):
            result = 0
            if i == 0:
                result = num + 1
                if 0 < result <= 1000000 and checked[result] == 0:
                    checked[result] = 1
                    Q.append((result, cnt+1))
            elif i == 1:
                result = num - 1
                if 0 < result <= 1000000 and checked[result] == 0:
                    checked[result] = 1
                    Q.append((result, cnt+1))
            elif i == 2:
                result = num * 2
                if 0 < result <= 1000000 and checked[result] == 0:
                    checked[result] = 1
                    Q.append((result, cnt+1))
            else:
                result = num - 10
                if 0 < result <= 1000000 and checked[result] == 0:
                    checked[result] = 1
                    Q.append((result, cnt+1))

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    ans = 0
    checked = [0] * 1000001
    Q = deque()
    Q.append((n, 0))
    operation()
    print('#{} {}'.format(tc, ans))
