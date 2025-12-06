def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve():
    N, K, M = map(int, input().split())

    ans = 0
    for L in range(1, K + 1):
        n = N - L + 1
        d = L + 1

        terms = [n + t for t in range(L + 1)]

        i = 0
        while d > 1 and i <= L:
            g = gcd(terms[i], d)
            if g > 1:
                terms[i] //= g
                d //= g
            else:
                i += 1


        prod = 1 % M
        for t in terms:
            prod = (prod * (t % M)) % M

        ans = (ans + prod) % M

    print(ans % M)

if __name__ == "__main__":
    solve()