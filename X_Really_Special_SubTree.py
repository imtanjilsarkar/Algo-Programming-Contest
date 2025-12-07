def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort(key=lambda e: (e[0], e[0] + e[1] + e[2]))

    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return False
        if rank[a] < rank[b]:
            parent[a] = b
        elif rank[a] > rank[b]:
            parent[b] = a
        else:
            parent[b] = a
            rank[a] += 1
        return True

    total = 0
    taken = 0
    for w, u, v in edges:
        if union(u, v):
            total += w
            taken += 1
            if taken == n - 1:
                break
    print(total)

if __name__ == "__main__":
    solve()