n = input()
 
sequence = map(int, raw_input().split())
 
for i in xrange(n):
  if i == 0: 
    min = sequence[1] - sequence[0]
    max = sequence[n - 1] - sequence[0]
  elif i == (n - 1):
    min = sequence[n - 1] - sequence[n - 2]
    max = sequence[n - 1] - sequence[0]
  else:
    min = sequence[i] - sequence[i - 1]
    if sequence[i + 1] - sequence[i] < min:
      min = sequence[i + 1] - sequence[i]
    max = sequence[n - 1] - sequence[i]
    if sequence[i] - sequence[0] > max:
      max = sequence[i] - sequence[0]
    
  print str(min) + " " + str(max)