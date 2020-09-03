numero_secreto = 9

palpite = int(input("De um palpite:"))

if palpite == numero_secreto:
  print("you win")
else:
  if palpite > numero_secreto:
    print("Fale um numero menor!")
  else:
    print("fale um numero maior!")
