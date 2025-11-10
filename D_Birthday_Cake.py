def birthdayCakeCandles (candles):
  tallest = max(candles)
  count_tallst = candles.count(tallest)
  return count_tallst

n = int(input().strip())
candles = list(map(int, input().split()))
result = birthdayCakeCandles(candles)
print(result)