padrao = "hello"
 
texto = input()
 
i = 0
index = 0
deslocamento = 0
 
while i <= (len(texto) - 1):
  if texto[i] == padrao[index]:
    index += 1
    deslocamento += 1
  i += 1
  if deslocamento == 5:
    print("YES")
    break
 
if deslocamento < 5: print("NO")