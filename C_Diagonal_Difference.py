def diagonalDifference (ar):
  n = len(ar)
  first_dig_sum = 0
  second_dig_sum = 0
  for i in range(n):
    first_dig_sum +=ar[i][i]
    second_dig_sum +=ar[i][n-i-1]
    deff = abs(first_dig_sum - second_dig_sum)
  return deff

n = int(input().strip())
ar = [list(map(int,input().split())) for i in range(n)]
print(diagonalDifference (ar))