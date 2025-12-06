from collections import deque

def bfs(start, graph, n):
    dist = [None] * (n + 1)
    dist[start] = 0
    q = deque([start])
    while q:
        node = q.popleft()
        for nei in graph[node]:
            if dist[nei] is None:
                dist[nei] = dist[node] + 1
                q.append(nei)
    return dist

n, m = map(int, input().split())
S, A, B = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

ds = bfs(S, graph, n)
da = bfs(A, graph, n)
db = bfs(B, graph, n)

shortest_SA = ds[A]
shortest_SB = ds[B]

max_shared = 0

for city in range(1, n+1):
    if ds[city] + da[city] == shortest_SA and ds[city] + db[city] == shortest_SB:
        max_shared = max(max_shared, ds[city])

print(max_shared)