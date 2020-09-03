numero_secreto = 9
palpite = 0

while numero_secreto != palpite:
 palpite = int(input("De um palpite:"))

 if palpite == numero_secreto:
  print("you win")
 elif palpite > numero_secreto:
  print("Fale um numero menor!")
 elif palpite < numero_secreto:
  print("fale um numero maior!")
 else:
  print("deu ruim")
