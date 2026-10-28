
# Classificador de Categorias de Natação
# Este programa calcula a idade do atleta a partir do ano de nascimento
# e define sua categoria conforme as faixas estabelecidas no exercício.

# Solicita o ano de nascimento
ano_de_nascimento = int(input("Digite o ano de nascimento: "))

# Calcula a idade usando 2026 como ano de referência
idade = 2026 - ano_de_nascimento

# Classifica o atleta de acordo com a idade
if idade <= 9:
    print("Você tem {} anos de idade, você é da categoria mirim".format(idade))

elif idade <= 14:
    print("Você tem {} anos de idade, você é da categoria infantil".format(idade))

elif idade <= 19:
    print("Você tem {} anos de idade, você é da categoria junior".format(idade))

elif idade <= 20:
    print("Você tem {} anos de idade, você é da categoria Sênior".format(idade))

else:
    print("Você tem {} anos de idade, você é da categoria Master".format(idade))
