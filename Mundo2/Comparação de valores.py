
# Comparador de Valores
# Este programa compara dois números inteiros
# e informa qual é o maior ou se são iguais.

# Solicita o primeiro valor
primeiro_valor = int(input("Digite o primeiro valor: "))

# Solicita o segundo valor
segundo_valor = int(input("Digite o segundo valor: "))

# Verifica se o primeiro valor é maior
if primeiro_valor > segundo_valor:
    print("O primeiro valor é maior que o segundo.")

# Verifica se o segundo valor é maior
elif segundo_valor > primeiro_valor:
    print("O segundo valor é maior que o primeiro.")

# Se nenhuma condição anterior for verdadeira, são iguais
else:
    print("Os valores são iguais.")
