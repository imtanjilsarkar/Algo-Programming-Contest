from collections import deque

def bfs(n, edges, s):
    graph = [[] for i in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    dist = [-1] * (n+1)
    dist[s] = 0
    q = deque([s])
    
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 6
                q.append(neighbor)
    
    return [dist[i] for i in range(1, n+1) if i != s]

q = int(input())
for i in range(q):
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for i in range(m)]
    s = int(input())
    print(' '.join(map(str, bfs(n, edges, s))))