for tc in range(1, int(input())+1):
    n = int(input())
    ingredients = [list(map(int, input().split())) for _ in range(n)]
    minS = 20000
    print('#{} {}'.format(tc, minS))