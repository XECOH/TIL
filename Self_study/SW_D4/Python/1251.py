from collections import deque

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

def make_set(x):
    parent[x] = x
    rank[x] = 0

def union(x, y):
    root1 = find_set(x)
    root2 = find_set(y)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

for tc in range(1, int(input())+1):
    n = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    e = float(input())
    parent = {}
    rank = {}
    graph = deque()
    for i in range(n):
        make_set(i)
    for i in range(n-1):
        for j in range(i+1, n):
            graph.append((i, j, (((xs[i]-xs[j])**2)+((ys[i]-ys[j])**2))*e))
    graph = sorted(graph, key= lambda x: x[2])
    mst = set()
    ans = 0
    while len(mst) < n-1:
        (n1, n2, cost) = graph.popleft()
        if find_set(n1) != find_set(n2):
            union(n1, n2)
            mst.add((n1, n2))
            ans += cost
    print(f'#{tc} {round(ans)}')
