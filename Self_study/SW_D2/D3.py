# 1217

T = 10
for tc in range(1, T+1):
    N = int(input())
    n, m = map(int, input().split())
    result = n ** m
    print('#{} {}'.format(tc, result))

# 3431

T = int(input())
for tc in range(1, T+1):
    L, U, X = map(int, input().split())
    if X < L:
        result = L - X
    elif L <= X <= U
        result = 0
    elif X > U :
        result = -1
    print('#{} {}'.format(tc, result))

# 4406

T = int(input())
for tc in range(1, T+1):
    vowels = 'aeiou'
    words = input()
    result = ''
    for word in words:
        if word not in vowels:
            result += word
    print('#{} {}'.format(tc, result))

# 8658

T = int(input())
for tc in range(1, T+1):
    list = [list(map(int, input().split()))]
    max = 0
    min = 1
    for i in range(10):
        sum = 0
        for j in range(len(str(list[i]))):
            sum = str(list[i])[j]
            if sum < min :
                min = sum
            elif sum > max:
                max = sum
    print('#{} {} {}'.format(tc, max, min))