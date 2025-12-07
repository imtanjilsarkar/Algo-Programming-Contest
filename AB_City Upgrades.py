def feasible(x, n, k, R):
    used = 0
    i = 0
    while i < n:
        used += 1
        if used > k:
            return False
        limit = x[i] + R
        j = i
        while j + 1 < n and x[j + 1] <= limit:
            j += 1
        center = x[j]
        cover = center + R
        i = j
        while i + 1 < n and x[i + 1] <= cover:
            i += 1
        i += 1
    return True

def solve():
    n, k = map(int, input().split())
    xs = list(map(int, input().split()))
    xs.sort()
    if k >= n:
        print(0)
        return
    lo, hi = 0, xs[-1] - xs[0]
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(xs, n, k, mid):
            hi = mid
        else:
            lo = mid + 1
    print(lo)

if __name__ == "__main__":
    solve()