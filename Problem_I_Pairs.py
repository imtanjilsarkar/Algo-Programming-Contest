def pairs(k, arr):
    s = set(arr)  
    count = 0

    for x in arr:
        if x + k in s:
            count += 1

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
ans = pairs(k, arr)
print(ans)
