def quickSort(arr):
    p = arr[0]   

    left = []
    equal = []
    right = []

    for x in arr:
        if x < p:
            left.append(x)
        elif x == p:
            equal.append(x)
        else:
            right.append(x)
    return left + equal + right

n = int(input())
arr = list(map(int, input().split()))

result = quickSort(arr)

print(*result)
