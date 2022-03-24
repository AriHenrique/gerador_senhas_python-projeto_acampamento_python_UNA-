import random

tamanhoLetras = int(input("Quantas letras você quer na sua senha? "))
tamanhoNumeros = int(input("E quantos números? "))
tamanhoSimbolos = int(input("E quantos símbolos?"))

print("Que tipo de senha você quer criar? ")
print("1 para letras, números e símbolos ")
print("2 para senha aleatória")

option = int(input("Opção: "))
senha = []

'''----------------------------------
poderia ter usado a biblioteca abaixo, porém o professor pediu da maneira que
enviou no exercício

letras = list(string.ascii_letters)
numeros = list(string.digits)
simbolos = list(string.punctuation)
-------------------------------------'''

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
          'o', 'p', 'q' ,'r', 's', 't', 'u', 'v', 'w', 'x' ,'y', 'z', 'A', 'B',
          'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
          'Q' ,'R', 'S', 'T', 'U', 'V', 'W', 'X' ,'Y', 'Z']

numeros = ['0','1','2','3','4','5','6','7','8','9']

simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

for i in range(tamanhoLetras):
  senha.append(random.choice(letras))

for i in range(tamanhoNumeros):
  senha.append(random.choice(numeros))

for i in range(tamanhoSimbolos):
  senha.append(random.choice(simbolos))

if option == 1:
  print("Senha = ", "".join(senha))
else:
  random.shuffle(senha)
  print("Senha = ", "".join(senha))
