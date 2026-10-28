
# Calculadora de Dobro, Triplo e Raiz Quadrada
# Este programa recebe um número inteiro e calcula seu dobro,
# seu triplo e sua raiz quadrada.

# Solicita um número ao usuário
numero = int(input("Digite um número: "))

# Calcula e exibe o dobro, o triplo e a raiz quadrada
print(
    "O dobro de {} vale {}, o triplo vale {} e a raiz quadrada é {:.2f}".format(
        numero,
        numero * 2,
        numero * 3,
        numero ** (1 / 2)
    )
)
