from collections import Counter

t = int(input())
for i in range(1, t+1):
    c = int(input())
    scores = list(map(int, input().split()))
    for i in range(1, c):
        for i in range(len(scores)):
            if 0 <= scores[i] <= 100 and len(scores) == 1000:
                continue
        mf = Counter(scores).most_common(1)[0][0]
        print(f'#{i} {mf}')





