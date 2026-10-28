
# Verificador de Números Pares e Ímpares
# Este programa percorre um intervalo de números
# e informa se cada número é par ou ímpar.

# Solicita o início do intervalo
i = int(input("Qual é o início? "))

# Solicita o final do intervalo
f = int(input("Qual é o final? "))

# Percorre os números do início até antes do final
for c in range(i, f):

    # Verifica se o resto da divisão por 2 é diferente de zero
    if c % 2 != 0:
        print(c, "é ímpar")

    # Se o resto da divisão por 2 for zero, o número é par
    elif c % 2 == 0:
        print(c, "é par")
