g1 = {}
g2 = {}
g3 = {}
media = {}

for i in range(9):
  group = int(input("Digite o numero do grupo"))
  nome = input("Digite o nome da pessoa")
  altura = float(input("Digite a altura da pessoa"))

  if group == 1 and len(g1) < 3:
    g1[nome] = altura
  elif group == 2 and len(g2) < 3:
    g2[nome] = altura
  else:
    if len(g3) < 3:
      g3[nome] = altura
soma = 0

for k,v in g1.values:
  soma += v
media[g1] = (round(soma / 3, 2))

for k,v in g2.values:
  soma += v
media[g2] = (round(soma / 3, 2))

for k,v in g3.values:
  soma += v
media[g3] = (round(soma / 3, 2))
   
print(media)

greater = 0
key = ''
for k,v in media.items:
  greater = v
  key = k
  if v > greater:
    greater = v
    key = k

print("A maior média de altura dos grupor foi {} {}".format(key.capitalize), greater)