#Para limpar a tela
from os import system

#criando uma função
def mostrar_menu():
  system('clear')
  print('off - sair')
  print('+ - somar')
  print('- - subtrair')
  print('* - multiplicar')
  print('/ - dividir')
  print('sen -  seno')
  print('cos - coseno')
  print('elevado - potencia')
  print("raiz - raiz")

def somar():
  numero1 = float(input("digite um numero:"))
  numero2 = float(input("digite outro numero:"))
  resultado = numero1 + numero2
  print("sua soma deu",resultado)

def subtrair():
  numero1 = float(input("digite um numero:"))
  numero2 = float(input("digite outro numero:"))
  resultado = numero1 - numero2
  print("sua subtração deu",resultado)

def multiplicar():
  numero1 = float(input("digite um numero:"))
  numero2 = float(input("digite outro numero:"))
  resultado = numero1 * numero2
  print("sua multiplicação deu",resultado)

def dividir():
  numero1 = float(input("digite um numero:"))
  numero2 = float(input("digite outro numero:"))
  resultado = numero1 / numero2
  print("seu divisão deu",resultado)


ligado = True

while ligado == True:
  mostrar_menu()
  opção = input("Opção:")
  if opção == 'off':
    ligado = False
  elif opção == '+':
    somar()
  elif opção == '-':
    subtrair()
  elif opção == '*':
    multiplicar()
  elif opção == '/':
    dividir()
  input('press enter to respect...')

print("até logo")
