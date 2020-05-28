def find(x):
    cnt = 1
    nodes= [bt[x]]
    while nodes:
        node = nodes.pop(0)
        cnt += len(node)
        if len(node) == 1:
            nodes.append(bt[node[0]])
        elif len(node) == 2:
            nodes.append(bt[node[0]])
            nodes.append(bt[node[1]])
    return cnt

def parent(arr, x):
    while True:
        l = len(arr)
        for i in range(1, e+1):
            if x in bt[i]:
                arr.append(i)
                x = i
                nl = len(arr)
        if l == nl: break
    return arr

for tc in range(1, int(input())+1):
    v, e, n1, n2 = map(int, input().split())
    bt = { i:[] for i in range(1, v+1) }
    t = list(map(int, input().split()))
    for i in range(0, e*2, 2):
        bt[t[i]].append(t[i+1])
    for num in parent([], n1):
        if num in parent([], n2):
            ans = num
            break

    print(f'#{tc} {ans} {find(ans)}')