def solve():
    import sys
    sys.setrecursionlimit(300000)
    input = sys.stdin.readline

    n, m = map(int, input().split())
    order = list(map(int, input().split()))
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    pos = [0]*(n+1)
    for i, x in enumerate(order):
        pos[x] = i
    for i in range(1, n+1):
        g[i].sort(key=lambda x: pos[x])

    vis = [False]*(n+1)
    seq = []

    def dfs(u):
        vis[u] = True
        seq.append(u)
        for v in g[u]:
            if not vis[v]:
                dfs(v)

    dfs(order[0])
    print(1 if seq == order else 0)


if __name__ == "__main__":
    solve()