
# Calculadora de Soma
# Este programa solicita dois números inteiros e calcula a soma entre eles.

# Solicita o primeiro valor ao usuário
notaum = int(input("Digite o primeiro valor: "))

# Solicita o segundo valor ao usuário
notadois = int(input("Digite o segundo valor: "))

# Soma os dois valores informados
s = notaum + notadois

# Exibe o resultado da soma utilizando format()
print("A soma entre {} e {} vale {}".format(notaum, notadois, s))
