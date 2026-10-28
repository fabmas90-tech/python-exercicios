
# Comparador de Três Números
# Este programa recebe três números inteiros e identifica
# qual deles é o maior, desde que não haja empate.

# Importa o módulo time para adicionar pausas
import time

# Solicita o primeiro número
a = int(input("Escreva o primeiro número: "))
print("Guardando número...")
time.sleep(1)

# Solicita o segundo número
b = int(input("Escreva o segundo número: "))
print("Guardando número...")
time.sleep(2)

# Solicita o terceiro número
c = int(input("Escreva o terceiro número: "))
print("Guardando número...")
time.sleep(2)

# Exibe uma mensagem antes de apresentar o resultado
print("Aguarde o resultado... estou checando se \n{} é maior que {}".format(a, b),
      "e se {} é maior que {}".format(c, b))
time.sleep(1)

# Compara os três números para identificar o maior
if a > b and a > c:
    print("O maior número é {}".format(a))

elif b > a and b > c:
    print("O maior é {}".format(b))

elif c > a and c > b:
    print("O maior é {}".format(c))
