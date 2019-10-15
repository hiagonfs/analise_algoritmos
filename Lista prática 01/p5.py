a, b = map(int, input().split())
 
countYears = 0
 
for i in range(1, 64):
  m = pow(2, i)
  for j in range(i - 1):
    n = pow(2, j)
    calculate = m - n - 1 
    if calculate >= a and calculate <= b:
      countYears += 1
 
print(countYears)