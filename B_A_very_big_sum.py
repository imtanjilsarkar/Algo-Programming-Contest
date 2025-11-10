def aVeryBigSum (ar):
  return sum(ar)

n = int(input())
ar = list(map(int, input().split()))
result = aVeryBigSum(ar)
print(result)