import sys,heapq
def solve():
    input=sys.stdin.readline
    MOD=10**9+7
    n,m,k=map(int,input().split())
    g=[[] for _ in range(n+1)]
    edges=[]
    for _ in range(m):
        a,b,c=map(int,input().split())
        g[a].append((b,c))
        g[b].append((a,c))
        edges.append((a,b,c))
    def dijkstra(src):
        INF=10**30
        dist=[INF]*(n+1)
        dist[src]=0
        h=[(0,src)]
        while h:
            d,u=heapq.heappop(h)
            if d!=dist[u]: continue
            for v,w in g[u]:
                nd=d+w
                if nd<dist[v]:
                    dist[v]=nd
                    heapq.heappush(h,(nd,v))
        return dist
    d1=dijkstra(1)
    d2=dijkstra(n)
    total=d1[n]
    vs=[i for i in range(1,n+1) if d1[i]+d2[i]==total]
    if not vs:
        print(0,0)
        return
    vs.sort(key=lambda x:d1[x])
    idx={v:i for i,v in enumerate(vs)}
    mv=len(vs)
    dag=[[] for _ in range(mv)]
    for u,v,w in edges:
        if d1[u]+w+d2[v]==total and d1[u]+w==d1[v] and u in idx and v in idx:
            dag[idx[u]].append(idx[v])
        if d1[v]+w+d2[u]==total and d1[v]+w==d1[u] and v in idx and u in idx:
            dag[idx[v]].append(idx[u])
    P=[[0]*mv for _ in range(mv)]
    for s in range(mv):
        dp=[0]*mv
        dp[s]=1
        for u in range(s,mv):
            if dp[u]==0: continue
            for v in dag[u]:
                dp[v]+=dp[u]
        for t in range(s,mv):
            P[s][t]=dp[t]
    h=[[0]*(k+1) for _ in range(mv)]
    cnt=[[0]*(k+1) for _ in range(mv)]
    for i in range(mv):
        if P[0][i] and P[i][mv-1]:
            h[i][1]=P[0][i]*P[i][mv-1]
            cnt[i][1]=1
    for c in range(2,k+1):
        for i in range(mv):
            best=0
            ways=0
            for j in range(i):
                if h[j][c-1]==0: continue
                if P[j][i]==0: continue
                val=(h[j][c-1]//P[j][mv-1])*P[j][i]*P[i][mv-1]
                if val>best:
                    best=val
                    ways=cnt[j][c-1]
                elif val==best and best>0:
                    ways=(ways+cnt[j][c-1])%MOD
            h[i][c]=best
            cnt[i][c]=ways%MOD
    best=0
    ways=0
    for i in range(mv):
        if h[i][k]>best:
            best=h[i][k]
            ways=cnt[i][k]
        elif h[i][k]==best and best>0:
            ways=(ways+cnt[i][k])%MOD
    print(best, ways%MOD)

if __name__=="__main__":
    solve()