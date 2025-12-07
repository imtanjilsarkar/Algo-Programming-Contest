def solve():
    import sys
    sys.setrecursionlimit(300000)
    input = sys.stdin.readline

    n, k = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    if k == 1:
        print(1 if n == 1 else 0)
        return

    mod = 10**9 + 7
    from collections import deque
    q = deque([1])
    vis = [False]*(n+1)
    vis[1] = True
    res = k
    c = k-1
    while q:
        u = q.popleft()
        cnt = c if u == 1 else c-1
        for v in g[u]:
            if not vis[v]:
                if cnt <= 0:
                    print(0)
                    return
                res = (res * cnt) % mod
                cnt -= 1
                vis[v] = True
                q.append(v)
    print(res)


if __name__ == "__main__":
    solve()