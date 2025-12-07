def solve():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        g[v].append((u, w))
    start = int(input().strip())

    INF = 10**18
    dist = [INF] * (n + 1)
    used = [False] * (n + 1)
    dist[start] = 0
    total = 0

    for _ in range(n):
        u = -1
        best = INF
        for i in range(1, n + 1):
            if not used[i] and dist[i] < best:
                best = dist[i]
                u = i
        if u == -1:
            break
        used[u] = True
        total += dist[u]
        for v, w in g[u]:
            if not used[v] and w < dist[v]:
                dist[v] = w

    print(total)

if __name__ == "__main__":
    solve()