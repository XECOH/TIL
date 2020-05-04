for tc in range(1, int(input())+1):
    n = int(input())
    times = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x: x[0])
    print(times)
