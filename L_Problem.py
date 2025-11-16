def luckBalance(k, contests):
    total = 0
    important = []

    for L, T in contests:
        if T == 0:
            total += L
        else:
            important.append(L)

    important.sort(reverse=True)

    for i in range(len(important)):
        if i < k:
            total += important[i]
        else:
            total -= important[i]

    return total

nk = input().split()
while len(nk) < 2:
    nk += input().split()

n = int(nk[0])
k = int(nk[1])

contests = []
for _ in range(n):
    L, T = map(int, input().split())
    contests.append([L, T])

ans = luckBalance(k, contests)
print(ans)
