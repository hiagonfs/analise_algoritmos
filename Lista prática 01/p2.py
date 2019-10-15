n = int(input())
 
maximo = 100000
 
custo = 0
 
for d in range(n):
  a, p = input().split() 
  if int(p) < maximo: maximo = int(p)
  custo += maximo * int(a) 
 
print(custo)