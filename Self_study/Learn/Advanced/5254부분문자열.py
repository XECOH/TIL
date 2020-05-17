for tc in range(1, int(input())+1):
    N, string = map(str, input().split())
    strings = set()
    for i in range(len(string)):
        for j in range(i, len(string)):
            strings.add(string[i:j+1])
    strings = sorted(list(strings))
    print('#{} {} {}'.format(tc, strings[int(N)-1][0], len(strings[int(N)-1])))