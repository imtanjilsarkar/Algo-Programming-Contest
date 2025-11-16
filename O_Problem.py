def journeyToMoon(n, astronaut):
    graph = [[] for _ in range(n)]
    for a, b in astronaut:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * n
    countries = []

    def dfs(u):
        stack = [u]
        size = 0
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                size += 1
                for v in graph[node]:
                    if not visited[v]:
                        stack.append(v)
        return size

    for i in range(n):
        if not visited[i]:
            countries.append(dfs(i))

    total_pairs = 0
    sum_sizes = 0
    for c in countries:
        total_pairs += c * (n - c)
    return total_pairs // 2 

n, p = map(int, input().split())
astronaut = []
for _ in range(p):
    a, b = map(int, input().split())
    astronaut.append([a, b])

ans = journeyToMoon(n, astronaut)
print(ans)
