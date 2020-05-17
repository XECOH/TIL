for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    arteries = [list(map(int, input().split())) for _ in range(E)]
    print('#{} {}'.format(tc,))