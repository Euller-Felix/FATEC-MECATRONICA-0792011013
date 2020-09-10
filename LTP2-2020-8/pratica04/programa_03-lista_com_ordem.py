temperaturas = []

print(temperaturas)

contador = 0
while contador < 5:
  temperatura = float(input('\ninforme uma temperatura:'))
  temperaturas.append(temperatura)
  print(temperaturas)
  contador += 1

maior = max(temperaturas)
print("a maior temperatura",maior)

menor = min(temperaturas)
print("a menor temperatura",menor)

media = sum(temperaturas)/ len(temperaturas)
print("a temperatura media é", media)
print("temperatura media: %.3f" % media)
#colocar a lista em ordem
temperaturas.sort()
print("ordem crecente das temperaturas")
print(temperaturas)

temperaturas.sort(reverse=True)
print("ordem decrecente das temperaturas")
print(temperaturas)
