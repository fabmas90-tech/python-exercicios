
# Calculadora de Antecessor e Sucessor
# Este programa recebe um número inteiro e identifica
# seu antecessor e seu sucessor.

# Solicita um número ao usuário
numero = int(input("Digite um número: "))

# Calcula e exibe o antecessor e o sucessor do número
print("O número antecessor é {} e o número sucessor é {}".format(
    numero - 1,
    numero + 1
))
