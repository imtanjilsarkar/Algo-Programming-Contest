def maximumToys(prices, k):
    prices.sort()    
    count = 0
    total = 0

    for p in prices:
        if total + p <= k:
            total += p
            count += 1
        else:
            break

    return count

nk = input().split()
while len(nk) < 2:
    nk += input().split()

n = int(nk[0])
k = int(nk[1])

arr = []
while len(arr) < n:
    arr += list(map(int, input().split()))

arr = arr[:n]

ans = maximumToys(arr, k)
print(ans)
