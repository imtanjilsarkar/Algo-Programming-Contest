def solve():
    N, Q = map(int, input().split())
    words = [input().strip() for _ in range(N)]
    words.sort()
    pos = {}
    for i, w in enumerate(words, 1):
        pos[w] = i
    out = []
    for _ in range(Q):
        w, xs = input().split()
        x = int(xs)
        rank = pos[w]
        page = (rank - 1) // x + 1
        out.append(str(page))
    print("\n".join(out))

if __name__ == "__main__":
    solve()
