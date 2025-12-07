def solve():
    import sys
    input = sys.stdin.readline

    n = int(input().strip())
    adj = [[] for _ in range(n + 1)]
    degsum = 0
    ok = True

    for i in range(1, n + 1):
        data = list(map(int, input().split()))
        if not data:
            ok = False
            continue
        k = data[0]
        lst = data[1:]
        if len(lst) != k:
            ok = False

        for v in lst:
            if v < 1 or v > n or v == i:
                ok = False
        adj[i] = lst
        degsum += len(lst)

    if not ok:
        print(-1)
        return
    if degsum % 2 == 1:
        print(-1)
        return

    idx = [0] * (n + 1)
    nxt = [0] * (n + 1)
    for i in range(1, n + 1):
        if idx[i] < len(adj[i]):
            nxt[i] = adj[i][idx[i]]


    q = []
    def push_if_ready(u):
        v = nxt[u]
        if v == 0:
            return
        if nxt[v] == u:
            a, b = (u, v) if u < v else (v, u)
            q.append((a, b))

    for i in range(1, n + 1):
        push_if_ready(i)

    edges = []
    head = 0
    while head < len(q):
        u, v = q[head]
        head += 1

        if nxt[u] != v or nxt[v] != u:
            continue

        edges.append((u, v))
        idx[u] += 1
        idx[v] += 1
        nxt[u] = adj[u][idx[u]] if idx[u] < len(adj[u]) else 0
        nxt[v] = adj[v][idx[v]] if idx[v] < len(adj[v]) else 0


        push_if_ready(u)
        push_if_ready(v)


    for i in range(1, n + 1):
        if idx[i] != len(adj[i]):
            print(-1)
            return


    if len(edges) != degsum // 2:
        print(-1)
        return

    out = []
    for a, b in edges:
        out.append(f"{a} {b}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()