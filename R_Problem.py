def find(par, x):
    while par[x] != x:
        par[x] = par[par[x]]
        x = par[x]
    return x

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

par = [i for i in range(n+1)]
extra_edges = [] 
for u, v in edges:
    pu = find(par, u)
    pv = find(par, v)
    if pu != pv:
        par[pu] = pv
    else:
        extra_edges.append((u, v))

reps = []
for i in range(1, n+1):
    if find(par, i) == i:
        reps.append(i)

if len(extra_edges) < len(reps) - 1:
    print(-1)
else:
    print(len(reps) - 1)
    for i in range(len(reps)-1):
        u_del, v_del = extra_edges[i]
        u_new = reps[i]
        v_new = reps[i+1]
        print(u_del, v_del, u_new, v_new)